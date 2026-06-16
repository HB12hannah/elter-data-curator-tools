#!/bin/bash

set -euo pipefail

######################## KONFIGURATION ########################################
# Einzelne IDs hier eintragen und --single Flag nutzen
# Kommentar entfernen um IDs zu aktivieren:
#SINGLE_IDS=(
  #"xpwd0-rxm33"
  # "00512-sfy70"
  # "00mt9-nz066"
  # "01dzn-t0j73"
#)
###############################################################################

show_help() {
  sed -n '3,16p' "$0"
}

######################## 0) Runtime checks ####################################
for cmd in curl jq xargs; do
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "Error: '$cmd' is required but not installed." >&2
    exit 1
  }
done

######################## 1) Parse CLI arguments ################################
APIKEY=""
DATASETID=""
EXISTING_ACTION=""
DOWNLOAD_ALL=true
DOWNLOAD_SINGLE=false

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IDS_FILE="${BASE_DIR}/eLTER-Data-Call-2025-Uploads.md"
DOWNLOAD_DIR="${BASE_DIR}/downloads_IDs"

for arg in "$@"; do
  case "$arg" in
    --apikey=*)   APIKEY=${arg#*=} ;;
    --existing=*) EXISTING_ACTION=${arg#*=} ;;
    --all)        DOWNLOAD_ALL=true ;;
    --single)     DOWNLOAD_SINGLE=true ;;
    -h|--help)    show_help; exit 0 ;;
    *)
      if [[ -z $DATASETID ]]; then
        DATASETID=$arg
      else
        echo "Unknown argument: $arg" >&2
        exit 1
      fi
      ;;
  esac
done

# Token aus Datei lesen falls kein --apikey angegeben
if [[ -z $APIKEY ]]; then
  APIKEY=$(grep -Ev "^\s*(#|$)" "${BASE_DIR}/.elter-dar-access-token" | head -n1)
fi

if [[ -n $EXISTING_ACTION && $EXISTING_ACTION != "skip" && $EXISTING_ACTION != "overwrite" ]]; then
  echo "Error: --existing must be 'skip' or 'overwrite'." >&2
  exit 1
fi

######################## 2) IDs sammeln ########################################
if [[ $DOWNLOAD_ALL == true ]]; then
  mapfile -t DATASET_IDS < <(grep -Ev "^\s*(#|$)" "${IDS_FILE}")
  echo "Modus: ALLE — ${#DATASET_IDS[@]} IDs aus ${IDS_FILE}"

elif [[ $DOWNLOAD_SINGLE == true ]]; then
  DATASET_IDS=("${SINGLE_IDS[@]}")
  echo "Modus: SINGLE — ${#DATASET_IDS[@]} IDs aus SINGLE_IDS Liste"

elif [[ -n $DATASETID ]]; then
  DATASET_IDS=("$DATASETID")
  echo "Modus: EINZELN — ${DATASETID}"

else
  show_help
  exit 1
fi

TOTAL=${#DATASET_IDS[@]}

######################## 3) Download Funktion ##################################
download_file() {
  local url=$1
  local name=$2
  local apikey=$3

  echo "  - downloading $name"
  if [[ -n $apikey ]]; then
    curl -# -L -H "Authorization: Bearer $apikey" -o "$name" "$url"
  else
    curl -# -L -o "$name" "$url"
  fi
  echo "  - finished    $name"
}

export -f download_file

######################## 4) Loop über alle IDs #################################
COUNT=0
DOWNLOADED=0
SKIPPED=0
FAILED=0

for DATASETID in "${DATASET_IDS[@]}"; do
  COUNT=$((COUNT + 1))

  # Site-Name vom DAR holen
  SITE_NAME=$(curl -fsSL \
    -H "Authorization: Bearer ${APIKEY}" \
    "https://dar.elter-ri.eu/api/datasets/${DATASETID}/draft" | \
    jq -r '.metadata.siteReferences[0].siteName // "UNKNOWN"' | \
    tr ' ' '_' | tr '/' '-' | tr -d ',()' | sed 's/__*/_/g')

  TARGET_DIR="${DOWNLOAD_DIR}/${SITE_NAME}/${DATASETID}"

  # Skip check
  if [[ $EXISTING_ACTION == "skip" && -d $TARGET_DIR && -n "$(ls -A $TARGET_DIR 2>/dev/null)" ]]; then
    echo "[${COUNT}/${TOTAL}] Skip: ${DATASETID} (${SITE_NAME})"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  # Overwrite
  if [[ $EXISTING_ACTION == "overwrite" && -d $TARGET_DIR ]]; then
    rm -rf "$TARGET_DIR"
  fi

  echo "[${COUNT}/${TOTAL}] Download: ${DATASETID} (${SITE_NAME})"

  # Dateiliste holen
  DAR_DRAFT_URL="https://dar.elter-ri.eu/api/datasets/${DATASETID}/draft/files"
  curl_opts=(-fsSL)
  [[ -n $APIKEY ]] && curl_opts+=(-H "Authorization: Bearer $APIKEY")

  json=$(curl "${curl_opts[@]}" "$DAR_DRAFT_URL") || {
    echo "  FEHLER: Metadaten nicht abrufbar für ${DATASETID}" >&2
    FAILED=$((FAILED + 1))
    continue
  }

  file_count=$(jq '.entries | length' <<<"$json")
  if [[ $file_count -eq 0 ]]; then
    echo "  Keine Dateien gefunden für ${DATASETID}"
    FAILED=$((FAILED + 1))
    continue
  fi

  echo "  ${file_count} Datei(en) gefunden – starte parallelen Download"
  mkdir -p "$TARGET_DIR"

  # Paralleler Download
  (
    cd "$TARGET_DIR"
    jq -j '.entries[] | .links.content, "\u0000", .key, "\u0000"' <<<"$json" |
      xargs -0 -P"$(nproc)" -n2 bash -c 'download_file "$1" "$2" "'"$APIKEY"'"' _
  )

  # Rekursiv ZIPs entpacken
  find "$TARGET_DIR" -name "*.zip" | while read -r inner_zip; do
    echo "  Entpacke: $(basename ${inner_zip})"
    unzip -q "${inner_zip}" -d "${inner_zip%.*}"
    rm "${inner_zip}"
  done

  echo "[${COUNT}/${TOTAL}] ✓ Fertig: ${DATASETID}"
  DOWNLOADED=$((DOWNLOADED + 1))

done

######################## 5) Zusammenfassung ####################################
echo ""
echo "================================"
echo "Download summary"
echo "================================"
echo "Downloaded: ${DOWNLOADED}"
echo "Skipped:    ${SKIPPED}"
echo "Failed:     ${FAILED}"
