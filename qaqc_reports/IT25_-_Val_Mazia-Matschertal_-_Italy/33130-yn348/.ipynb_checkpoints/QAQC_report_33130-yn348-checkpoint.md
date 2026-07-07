---
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
 
This QA & QC report summarizes the validation, completeness, and conformity assessment of the data submission from the **eLTER site - Country**, as part of the **eLTER data mobilization initiative**.\
The QA & QC aimed to verify dataset integrity, completeness, schema compliance, and unit consistency with eLTER standards.
 
 
------------------------------------------------------------------------
 
## 2. Basic information
 
- **Site:** [eLTER site], Country
- **Responsible person:** Alessandro Zandonai (Eurac Research)
  - **e-mail:** Alessandro.Zandonai@eurac.edu
- **Dataset creator:** Alessandro Zandonai (Eurac Research)
  - **e-mail:** Alessandro.Zandonai@eurac.edu
- **Submitted data:** 
    - `SOGEO_001`: [link](add the link to DAR here)
 
- **Dataset ID**: ?
 
- **Promised Standard Observations:**  <span style="color: rgb(0,200,0);">`SOXXX_XXX`</span>.
- **Promised temporal coverage:** `YYYY-MM-DD to YYYY-MM-DD`
 
 
------------------------------------------------------------------------
 
## 3. Submission overview
- **Number of files submitted:** 12 
 
- **File format:** <span style="color: rgb(0,200,0);">*format*</span>
- **Separated files per type (e.g. DATA, METHOD, STATION):** <span style="color: rgb(0,200,0);">Yes</span>
- **Dataset name**:
    - `SOGEO_001`
        - Mazia-Matschertal, 2014-2017, soil water potential (swp), soil temperature (ts), and volume water content (vwc)
            
    
- **File(s) name(s):**
    - `SOGEO_001`
        - IT_ValMazia-Matschertal_SOIL_swp_20_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_swp_5_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_ts_20_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_ts_2_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_ts_5_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_vwc_20_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_vwc_2_2014-2017_V20251027_data.csv
        - IT_ValMazia-Matschertal_SOIL_vwc_5_2014-2017_V20251027_data.csv
            - **Naming convention followed:** <span style="color: rgb(255,155,0);">*?*</span>
    
         
- **Data format:** 
    - `SOGEO_001`: *Long-format*
    
- **Number of rows:** 
    - `SOGEO_001`: 1322864
    
- **Number of columns:** 
    - `SOGEO_001`: 7
    
- **Temporal coverage:** 
    - `SOGEO_001`: 2014-04-09 to 2016-12-31
    
 
- **Temporal resolution:** 
        - prommissed resolution (in DAR): 
 
 | Variable in the dataset | Average Resolution | Regularity |
|:------------------:|:----------:|:----------:|
| <span style="color: rgb(0,0,0);">`swp`</span> | 15 minutes | <span style="color: rgb(0,200,0);">`regularly`</span> |
| <span style="color: rgb(0,0,0);">`ts`</span> | 15 minutes | <span style="color: rgb(0,200,0);">`mostly regularly`</span> |
| <span style="color: rgb(0,0,0);">`vwc`</span> | 15 minutes | <span style="color: rgb(0,200,0);">`mostly regularly`</span> |

 
- **Information on variables correctly presented in `METHOD` and `STATION` files/sheets:** <span style="color: rgb(0,200,0);">*Yes*</span>
- **Number of Standard Observations covered:** *1*
- **Total number of variables provided:** 3
  - **Variables belonging to targeted standard observations:** *?*
- **Data volume:** *139.48 MB* 
 
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
 
QA & QC validation was performed on the dataset structure and contents.\
The following summarizes the validation outcomes:
 
- Add things
 
 
------------------------------------------------------------------------
 
## 6. File encoding
 
| File | Encoding |
|:-------------------------------------- |:--------:|
| IT_ValMazia-Matschertal_SOIL_swp_20_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_swp_5_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_ts_20_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_ts_2_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_ts_5_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_vwc_20_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_vwc_2_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_vwc_5_2014-2017_V20251027_data.csv | <span style="color: rgb(200,0,0);">`ascii`</span> |
| IT_ValMazia-Matschertal_SOIL_2014-2017_V20251027_method.csv | <span style="color: rgb(200,0,0);">`UTF-8-SIG`</span> |
| IT_ValMazia-Matschertal_SOIL_2014-2017_V20251027_station.csv | <span style="color: rgb(200,0,0);">`UTF-8-SIG`</span> |
| IT_ValMazia-Matschertal_SOIL_2014-2017_V20251027_reference.csv | <span style="color: rgb(200,0,0);">`UTF-8-SIG`</span> |
| IT_ValMazia-Matschertal_SOIL_2014-2017_V20251027_license.txt | <span style="color: rgb(200,0,0);">`ascii`</span> |

 
------------------------------------------------------------------------
 
## 7. Overall assessment
 
The submission meets eLTER QA & QC standards for most of the time, but **minor modifications** are required before publishing the dataset in DAR.
 
------------------------------------------------------------------------
 
**QA & QC performed by:** eLTER Data Mobilization Team\
**Date:** 2026-07-07\
**Tools Used:** R ([*pointblank*](https://rstudio.github.io/pointblank/) *package*), manual inspection.
 
------------------------------------------------------------------------
