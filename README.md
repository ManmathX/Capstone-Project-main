# Diabetes Readmission Capstone

This repository is set up for Capstone 2 using the UCI diabetes hospital encounters dataset. The project is intentionally scoped to a small set of high-signal columns so the analysis stays clear, defensible, and useful.

## Project Goal

Identify which patient and encounter factors are associated with readmission within 30 days for diabetic patients, then translate those findings into practical hospital recommendations for follow-up and discharge planning.

## Problem Statement

Hospitals need a simple way to identify diabetic patients who are more likely to return within 30 days. This project analyzes historical U.S. hospital encounter data to find the strongest readmission drivers and highlight high-risk patient segments that deserve early intervention.

## Dataset Plan

### Primary Dataset

- Dataset: `data/raw/diabetic_data.csv`
- Supporting mapping file: `data/raw/IDS_mapping.csv`
- Source: UCI diabetes readmission dataset
- Size: 101,766 rows and 50 columns
- Why it works: exceeds the minimum capstone requirement and directly supports a healthcare readmission story

### Backup Datasets

- Backup 1: [CDC BRFSS Annual Survey Data](https://www.cdc.gov/brfss/annual_data/annual_data.htm)
- Backup 2: [AHRQ MEPS Full-Year Consolidated Data Files](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp/)

These are listed as official backup options for Phase 1. They are not needed unless you decide to change direction.

## Focused Column Scope

The full dataset has 50 columns, but this capstone should start with a smaller set of features that tell a strong story.

### Keep These Raw Columns

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

### Derived Fields Created During Cleaning

- `admission_type`
- `readmitted_30`
- `prior_inpatient_group`
- `prior_emergency_group`
- `medication_burden_group`
- `stay_length_group`

### Exclude These Early

- `weight` because it is mostly missing
- `payer_code` because missingness is high
- `medical_specialty` because missingness is high
- most individual drug columns because they add noise without improving the core story

## Why This Scope Feels Valuable

This narrowed dataset still supports a meaningful hospital use case:

- overall 30-day readmission is about 11.2%
- patients with 3 or more prior inpatient visits have much higher readmission rates
- patients with repeated emergency visits are also noticeably higher risk
- longer hospital stays and heavier medication burden also show useful segmentation patterns

That gives you a clear recommendation angle: hospitals should prioritize follow-up for patients with repeated prior utilization and more complex current encounters.

## Repository Structure

```text
Capstone-Project-main/
|-- data/
|   |-- raw/
|   |   |-- diabetic_data.csv
|   |   `-- IDS_mapping.csv
|   |-- processed/
|   `-- data_dictionary.md
|-- notebooks/
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   `-- 04_statistical_analysis.ipynb
|-- src/
|   |-- clean_data.py
|   |-- data_utils.py
|   `-- project_config.py
|-- reports/
|   |-- final_report_outline.md
|   |-- phase1_submission.md
|   `-- submission_checklist.md
|-- dashboard/
|   `-- tableau_dashboard_plan.md
|-- presentation/
|   `-- deck_outline.md
|-- requirements.txt
`-- README.md
```

## Execution Order

### Phase 1

1. Review `reports/phase1_submission.md`
2. Confirm the primary dataset and backup datasets
3. Finalize the problem statement in the README and submission file
4. Commit the raw files already placed in `data/raw`

### Phase 2

1. Run the cleaning notebook or `src/clean_data.py`
2. Save the processed file to `data/processed/clean_diabetes.csv`
3. Complete EDA in `notebooks/03_eda.ipynb`
4. Complete statistical testing in `notebooks/04_statistical_analysis.ipynb`
5. Build the Tableau dashboard using `dashboard/tableau_dashboard_plan.md`
6. Finish the report and deck using the outlines in `reports/` and `presentation/`

## Quick Start

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Generate the cleaned analysis file:

```bash
python src/clean_data.py
```

Launch notebooks:

```bash
jupyter notebook
```

## Deliverables Checklist

- Phase 1 project framing completed
- Primary dataset committed
- Two backup datasets listed
- Cleaning notebook prepared
- EDA notebook prepared
- Statistical analysis notebook prepared
- Tableau dashboard plan prepared
- Final report outline prepared
- Presentation deck outline prepared

## Official Dates

- Capstone release: April 13, 2026
- Final Phase 2 submission deadline: April 28, 2026

## Recommended Final Story

Keep the final story simple:

1. Which diabetic patient segments have the highest 30-day readmission risk?
2. Which utilization and treatment patterns are most associated with readmission?
3. What should hospitals do differently for those high-risk segments?
