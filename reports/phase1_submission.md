# Phase 1 Submission Draft

## Capstone Title

Reducing 30-Day Readmission Risk for Diabetic Patients

## Problem Statement

Hospitals often struggle to identify which diabetic patients are most likely to be readmitted within 30 days after discharge. This project uses historical hospital encounter data to determine the strongest factors associated with short-term readmission and to recommend targeted follow-up actions for high-risk groups.

## Primary Dataset

- Name: Diabetes 130-US hospitals dataset
- Files:
  - `data/raw/diabetic_data.csv`
  - `data/raw/IDS_mapping.csv`
- Size: 101,766 rows and 50 columns
- Why selected:
  - meets the minimum dataset requirement by a wide margin
  - strongly fits a healthcare analytics problem
  - contains a clear business outcome through the `readmitted` field

## Backup Datasets

### Backup 1

- Name: CDC BRFSS Annual Survey Data
- Source: https://www.cdc.gov/brfss/annual_data/annual_data.htm
- Why it works:
  - very large public health dataset
  - strong feature set for diabetes and risk factor analysis
  - official source with documentation

### Backup 2

- Name: AHRQ MEPS Full-Year Consolidated Data Files
- Source: https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp/
- Why it works:
  - official healthcare dataset
  - person-level utilization and expenditure data
  - large enough for a capstone with many possible health questions

## Narrow Analysis Scope

To keep the project valuable and manageable, the initial analysis will focus on these columns:

- `age`
- `gender`
- `race`
- `admission_type_id`
- `time_in_hospital`
- `num_medications`
- `number_emergency`
- `number_inpatient`
- `A1Cresult`
- `insulin`
- `readmitted`

## Initial Hypothesis

Patients with higher prior utilization, longer hospital stays, and more complex medication patterns are more likely to be readmitted within 30 days.

## Planned Deliverables

- cleaned dataset in `data/processed/clean_diabetes.csv`
- cleaning notebook in `notebooks/02_cleaning.ipynb`
- EDA notebook in `notebooks/03_eda.ipynb`
- statistical analysis notebook in `notebooks/04_statistical_analysis.ipynb`
- Tableau Public dashboard
- final report
- presentation deck

## Proposed KPIs

- 30-day readmission rate
- readmission rate by age group
- readmission rate by admission type
- readmission rate by prior inpatient visits
- readmission rate by prior emergency visits
- readmission rate by insulin status
- average length of stay for readmitted vs non-readmitted patients

## Business Value

The final output will help hospitals understand which patient groups deserve stronger discharge planning, medication review, and post-discharge outreach to reduce avoidable readmissions.
