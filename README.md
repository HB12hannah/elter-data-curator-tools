<p>
  <img src="assets/eLTER-IMAGE-eLTER_logo-v01.svg" alt="eLTER Project Logo" width="300" height="auto"/>
</p>

# eLTER Data Curator Tools

This repository provides usage documentation and basic, unfinished Bash scripts 
to help eLTER data stewards and curators automate querying and downloading of
unpublished dataset drafts from the
[eLTER Digital Asset Registry (DAR)](https://dar.elter-ri.eu/).

![EUPL--1.2](https://img.shields.io/badge/license-EUPL--1.2-orange)
![BASH-v5.2.21](https://img.shields.io/badge/BASH-v5.2.21-orange)

## Description

The [USAGE.md](./USAGE.md) document provides examples of queries that use `curl`
to create table-based reports. It also offers tips on authenticating with
session cookies or DAR access tokens.

[elter-dar-query.sh](./elter-dar-query.sh) is a short script that queries
unpublished draft records using the DAR API. It requires a list of
draft dataset IDs in a file called `eLTER-Data-Call-2025-Uploads.md`,
which is stored alongside the script. Currently, the script must be edited
to adjust the JSON fields to be queried.

The [elter-dar-download.sh](./elter-dar-download.sh) script is designed to
download multiple data files from DAR records. Currently, you must edit the
script to include a list of dataset IDs at the beginning.

## Table of Contents

Add a table of contents at the beginning of the `README.md` file.

- [Installation and usage](#installation-and-usage)
- [Authors](#authors)
- [License](#license)
- [Dependencies](#dependencies)
- [Citation](CITATION.cff)
- [Acknowledgments](#acknowledgments)

## Installation and usage

1. Create a DAR access token and save it to [.elter-dar-access-token](.elter-dar-access-token)
2. Create a list of draft dataset IDs like described in [USAGE.md](./USAGE.md) and save it to a file
   called `eLTER-Data-Call-2025-Uploads.md` in this directory.
3. Run [elter-dar-query.sh](elter-dar-query.sh):
   ```bash
   $ ./elter-dar-query.sh > output.csv
   ```
4. Edit [elter-dar-download.sh](elter-dar-download.sh) and add some data set IDs you want to download.
5. Run [elter-dar-download.sh](elter-dar-download.sh):
   ```bash
   $ ./elter-dar-download.sh
   ```

To be continued...

## Authors

|                                                                  Author                                                                   |                                   Affiliation                                   | ORCID |                         e-mail                         |
|:-----------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:| :---: |:------------------------------------------------------:|
| <p><img src="https://avatars.githubusercontent.com/u/643697?v=4" width="30" height="auto"/></p> [Martin Abbrent](https://github.com/maab) | [ Helmholtz Centre for Environmental Research - UFZ](https://ror.org/000h6jb29) | [0000-0003-1252-9107](https://orcid.org/0000-0003-1252-9107) | [martin.abbrent\@ufz.de](mailto:martin.abbrent@ufz.de) |

## License

This project is licensed under the [EUPL
License](https://eupl.eu/) - see the [LICENSE](LICENSE) file for
details.

## Dependencies

This project uses the  
[eLTER boilerplate README](https://github.com/eLTER-RI/boilerplate-readme).

## Acknowledgments

<p align="center">
  <a href="https://elter-ri.eu/elter-ppp">
    <img src="assets/eLTER-IMAGE-PPP_logo-v01.svg" alt="eLTER PLUS Logo" width="175" height="auto"/>
  </a> <a href="https://elter-ri.eu/elter-plus">
    <img src="assets/eLTER-IMAGE-PLUS_logo-v01.svg" width="175" height="auto"/>
  </a> <a href="https://elter-ri.eu/elter-enrich">
    <img src="assets/eLTER-IMAGE-EnRich_logo-v01.svg" alt="eLTER EnRich Logo" width="175" height="auto"/>
  </a>
</p>
