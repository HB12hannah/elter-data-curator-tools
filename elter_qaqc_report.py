from __future__ import annotations
from pathlib import Path
from datetime import datetime
 
 
def build_report(
    info: dict,
    df_station,
    df_method,
    df_data,
    filepaths: dict,
    temporal_summary,
    total_size_bytes: float,
    encoding_results: "dict[str, str]",
    variable_col: str = "VARIABLE",
) -> str:
    """
    Generates the Markdown report text (structure = original template). 
    All parameters correspond 1:1 to the objects present in the notebook.
    """
 
    so_code = info.get("Dataset Type") or "SOXXX_XXX"
    creators = ", ".join(info.get("Creators", [])) or "?"
    creator_emails = ", ".join(info.get("Creator emails", [])) or "?"
    orgs = ", ".join(info.get("Organizations", [])) or "?"
    dataset_id = info.get("Dataset ID") or "?"
 
    # ---------------- 3: Submission overview ----------------
    n_files = sum(len(v) if isinstance(v, list) else (1 if v else 0) for v in filepaths.values())
    n_rows = len(df_data)
    n_cols = len(df_data.columns)
    data_format = "Long-format" if variable_col in df_data.columns else "Wide-format"
 
    data_files = filepaths.get("data") or []
    if isinstance(data_files, str):
        data_files = [data_files]
    file_name_lines = "\n".join(f"        - {Path(p).name}" for p in data_files) or "        - ?"
 
    method_ok = {"variable", "meth_descr"}.issubset({c.strip().lower() for c in df_method.columns})
    station_required = {"site_code", "station_code", "stype", "lat", "lon", "altitude"}
    station_ok = station_required.issubset({c.strip().lower() for c in df_station.columns})
    meta_ok = method_ok and station_ok
    meta_status_color = "0,200,0" if meta_ok else "255,155,0"
    meta_status_text = "Yes" if meta_ok else "?"
 
    # take it from summary-DataFrame
    res_rows = ""
    for var_name, row in temporal_summary.iterrows():
        res_rows += (
            f"| <span style=\"color: rgb(0,0,0);\">`{var_name}`</span> | {row.get('Resolution', '?')} | "
            f"<span style=\"color: rgb(0,200,0);\">`{row.get('Regularity', '?')}`</span> |\n"
        )
 
    from_dates = temporal_summary["From"].tolist() if "From" in temporal_summary.columns else []
    to_dates = temporal_summary["To"].tolist() if "To" in temporal_summary.columns else []
    from_overall = min(from_dates) if from_dates else "?"
    to_overall = max(to_dates) if to_dates else "?"
 
    n_variables = df_data[variable_col].nunique() if variable_col in df_data.columns else n_cols
 
    # ---------------- 6: File encoding ----------------
    encoding_rows = ""
    for fname, enc in encoding_results.items():
        enc_display = enc if enc else "unknown"
        encoding_rows += f"| {fname} | <span style=\"color: rgb(200,0,0);\">`{enc_display}`</span> |\n"
 
    report = f"""---
editor_options: 
  markdown: 
    wrap: 72
---
 
![](https://s3.desy.de/hackmd/uploads/ce5dae96-15a0-43df-8311-e82856fbb24e.png)
 
 
# Quality Assurance (QA) and Quality Control (QC) Report (copie for new report)
 
### [eLTER site](actual link), Country
 
**eLTER Data Mobilization 2025**
 
------------------------------------------------------------------------
## 1. Purpose
 
This QA & QC report summarizes the validation, completeness, and conformity assessment of the data submission from the **eLTER site - Country**, as part of the **eLTER data mobilization initiative**.\\
The QA & QC aimed to verify dataset integrity, completeness, schema compliance, and unit consistency with eLTER standards.
 
 
------------------------------------------------------------------------
 
## 2. Basic information
 
- **Site:** [eLTER site], (actual link) Country
- **Responsible person:** {creators} ({orgs})
  - **e-mail:** {creator_emails}
- **Dataset creator:** {creators} ({orgs})
  - **e-mail:** {creator_emails}
- **Submitted data:** 
    - `{so_code}`: [link](add the link to DAR here)
 
- **Dataset ID**: {dataset_id}
 
- **Promised Standard Observations:**  <span style="color: rgb(0,200,0);">`SOXXX_XXX`</span>.
- **Promised temporal coverage:** `YYYY-MM-DD to YYYY-MM-DD`
 
 
------------------------------------------------------------------------
 
## 3. Submission overview
- **Number of files submitted:** {n_files} 
 
- **File format:** <span style="color: rgb(0,200,0);">*format*</span>
- **Separated files per type (e.g. DATA, METHOD, STATION):** <span style="color: rgb(0,200,0);">Yes</span>
- **Dataset name**:
    - `{so_code}`
        - {info.get('Title', '?')}
            
    
- **File(s) name(s):**
    - `{so_code}`
{file_name_lines}
            - **Naming convention followed:** <span style="color: rgb(255,155,0);">*?*</span>
    
         
- **Data format:** 
    - `{so_code}`: *{data_format}*
    
- **Number of rows:** 
    - `{so_code}`: {n_rows}
    
- **Number of columns:** 
    - `{so_code}`: {n_cols}
    
- **Temporal coverage:** 
    - `{so_code}`: {from_overall} to {to_overall}
    
 
- **Temporal resolution:** 
        - prommissed resolution (in DAR): 
 
 | Variable in the dataset | Average Resolution | Regularity |
|:------------------:|:----------:|:----------:|
{res_rows}
 
- **Information on variables correctly presented in `METHOD` and `STATION` files/sheets:** <span style="color: rgb({meta_status_color});">*{meta_status_text}*</span>
- **Number of Standard Observations covered:** *1*
- **Total number of variables provided:** {n_variables}
  - **Variables belonging to targeted standard observations:** *?*
- **Data volume:** *{total_size_bytes / (1024*1024):.2f} MB* 
 
------------------------------------------------------------------------
 
## 4. Data coverage and completeness
 
### Data coverage summary
 
| Standard Observation | Targeted in the call | Variables provided | From | To |
|:--:|:-:|:----------:|:----:|:-:|
| <span style="color: rgb(0,200,0);">`SOXXX_XXX`</span> | Yes | ![100%](https://img.shields.io/badge/6/6-100%25-brightgreen) |  YYYY-MM-DD | YYYY-MM-DD |
 
 
 
### Data completeness summary
 
The table below displays the alignment between the eLTER standard observations 
and variables available in the dataset.
 
| Sphere        | Standard Observation | Variable                       | Equivalence in the dataset | Delivered |
|:-------------:|:--------------------:|:------------------------------:|:--------------------------:|:---------:|
| *Xsphere*  | <span style="color: rgb(0,200,0);">`SOXXX_XXX`</span>                              | `data`    | `data`                          | Yes       |
|    |    | `data`   |  `data`  |    |
 
------------------------------------------------------------------------
 
 
## 5. Validation
 
QA & QC validation was performed on the dataset structure and contents.\\
The following summarizes the validation outcomes:
 
- Add things
 
 
------------------------------------------------------------------------
 
## 6. File encoding
 
| File | Encoding |
|:-------------------------------------- |:--------:|
{encoding_rows}
 
------------------------------------------------------------------------
 
## 7. Overall assessment
 
The submission meets eLTER QA & QC standards for most of the time, but **minor modifications** are required before publishing the dataset in DAR.
 
------------------------------------------------------------------------
 
**QA & QC performed by:** eLTER Data Mobilization Team\\
**Date:** {datetime.now().strftime('%Y-%m-%d')}\\
**Tools Used:** R ([*pointblank*](https://rstudio.github.io/pointblank/) *package*), manual inspection.
 
------------------------------------------------------------------------
"""
    return report