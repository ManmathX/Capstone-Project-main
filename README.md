# NST DVA Capstone 2 - Project Repository

Newton School of Technology | Data Visualization & Analytics  
A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

## Before You Start

- Rename the repository using the format `SectionName_TeamID_ProjectName`.
- Fill in the project details and team table below.
- Add the raw dataset to `data/raw/`.
- Complete the notebooks in order from `01` to `05`.
- Publish the final dashboard and add the public link in `tableau/dashboard_links.md`.
- Export the final report and presentation as PDFs into `reports/`.

## Quick Start

If you are working locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

If you are working in Google Colab:

- Upload or sync the notebooks from `notebooks/`
- Keep the final `.ipynb` files committed to GitHub
- Export any cleaned datasets into `data/processed/`

## Project Overview

| Field | Details |
| --- | --- |
| Project Title | Reducing 30-Day Readmission Risk for Diabetic Patients |
| Sector | Healthcare |
| Team ID | To be filled by team |
| Section | To be filled by team |
| Faculty Mentor | To be filled by team |
| Institute | Newton School of Technology |
| Submission Date | To be filled by team |

## Team Members

| Role | Name | GitHub Username |
| --- | --- | --- |
| Project Lead | To be filled | To be filled |
| Data Lead | To be filled | To be filled |
| ETL Lead | To be filled | To be filled |
| Analysis Lead | To be filled | To be filled |
| Visualization Lead | To be filled | To be filled |
| Strategy Lead | To be filled | To be filled |
| PPT and Quality Lead | To be filled | To be filled |

## Business Problem

Hospitals often struggle to identify which diabetic patients are most likely to be readmitted within 30 days after discharge. This project uses historical U.S. hospital encounter data to identify the strongest factors associated with short-term readmission. The analysis supports hospital operations teams in prioritizing follow-up and discharge planning for high-risk segments.

### Core Business Question

Which patient and encounter patterns best indicate 30-day readmission risk for diabetic patients?

### Decision Supported

This analysis supports targeted intervention decisions, including risk-tiered discharge plans and early post-discharge follow-up.

## Dataset

| Attribute | Details |
| --- | --- |
| Source Name | UCI Diabetes 130-US hospitals dataset |
| Direct Access Link | [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) |
| Row Count | 101,766 |
| Column Count | 50 raw columns (17 cleaned columns used in analysis) |
| Time Period Covered | 1999 to 2008 |
| Format | CSV |

### Key Columns Used

| Column Name | Description | Role in Analysis |
| --- | --- | --- |
| `age` | Patient age group | Segmentation and dashboard filter |
| `admission_type` | Decoded admission type | Driver analysis and filter |
| `time_in_hospital` | Number of stay days | KPI and statistical testing |
| `num_medications` | Medication count | Treatment complexity signal |
| `number_emergency` | Prior emergency visits | High-risk segmentation |
| `number_inpatient` | Prior inpatient visits | High-risk segmentation |
| `insulin` | Insulin status | Treatment pattern comparison |
| `readmitted_30` | 30-day readmission flag | Primary target variable |

For full column definitions, see `data/data_dictionary.md`.

## KPI Framework

| KPI | Definition | Formula / Computation |
| --- | --- | --- |
| 30-day Readmission Rate | % of encounters readmitted within 30 days | `mean(readmitted_30) * 100` |
| Average Length of Stay | Average days admitted | `mean(time_in_hospital)` |
| Average Medication Count | Average medication load | `mean(num_medications)` |
| Readmission by Prior Inpatient Group | Segment risk by prior inpatient usage | `groupby(prior_inpatient_group).mean(readmitted_30)` |
| Readmission by Prior Emergency Group | Segment risk by prior emergency usage | `groupby(prior_emergency_group).mean(readmitted_30)` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

## Tableau Dashboard

| Item | Details |
| --- | --- |
| Dashboard URL | Paste Tableau Public link in `tableau/dashboard_links.md` |
| Executive View | KPI summary and readmission distribution |
| Operational View | Segment drill-down by utilization and treatment factors |
| Main Filters | Age group, gender, race, admission type, insulin status |

Store dashboard screenshots in `tableau/screenshots/` and document the public links in `tableau/dashboard_links.md`.

## Key Insights

1. 30-day readmission rate is approximately 11.16%.
2. Prior inpatient history is the strongest risk signal.
3. Prior emergency history also materially increases risk.
4. Longer hospital stays show higher readmission tendency.
5. Higher medication burden aligns with elevated readmission risk.
6. Insulin status groups show measurable risk variation.
7. Admission type contributes to meaningful readmission segmentation.
8. Readmission risk is concentrated in specific subgroups, enabling targeted interventions.

## Recommendations

| # | Insight | Recommendation | Expected Impact |
| --- | --- | --- | --- |
| 1 | Prior inpatient risk concentration | Introduce risk-tiered discharge checklist for high-utilization patients | Reduced avoidable 30-day readmissions |
| 2 | Prior emergency segment risk | Trigger mandatory early follow-up for high emergency-history patients | Better continuity of care |
| 3 | Medication burden signal | Add focused medication reconciliation before discharge | Lower medication-related returns |
| 4 | Non-uniform risk across segments | Prioritize care coordination resources to top-risk groups | Improved intervention ROI |

## Repository Structure

```text
SectionName_TeamID_ProjectName/
|
|-- README.md
|-- requirements.txt
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|   `-- data_dictionary.md
|
|-- notebooks/
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   `-- 04_statistical_analysis.ipynb
|
|-- scripts/
|   `-- .gitignore
|
|-- tableau/
|   `-- .gitignore
|
|-- dashboard/
|   `-- tableau_dashboard_plan.md
|
|-- presentation/
|   `-- deck_outline.md
|
|-- reports/
|   |-- final_report_outline.md
|   |-- phase1_submission.md
|   `-- submission_checklist.md
|
|-- src/
|   |-- clean_data.py
|   |-- data_utils.py
|   `-- project_config.py
|
|-- docs/
|   `-- .gitignore
`-- .venv/                           # local virtual env (not required for submission)
```

## Analytical Pipeline

1. Define - Sector selected, problem statement scoped, mentor approval obtained.
2. Extract - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. Clean and Transform - Pipeline built in `notebooks/02_cleaning.ipynb` and optionally `scripts/etl_pipeline.py`.
4. Analyze - EDA and statistical analysis in notebooks `03` and `04`.
5. Visualize - Interactive Tableau dashboard built and published.
6. Recommend - 3-5 data-backed recommendations delivered.
7. Report - Final report and presentation exported as PDFs in `reports/`.

## Tech Stack

| Tool | Status | Purpose |
| --- | --- | --- |
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, KPI computation |
| Google Colab | Supported | Cloud notebook execution |
| Tableau Public | Mandatory | Dashboard design and publishing |
| GitHub | Mandatory | Version control and contribution audit |
| SQL | Optional | Initial extraction only if documented |

Recommended Python libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

## Evaluation Rubric

| Area | Marks | Focus |
| --- | --- | --- |
| Problem Framing | 10 | Clear and well-scoped business question |
| Data Quality and ETL | 15 | Thorough and documented cleaning pipeline |
| Analysis Depth | 25 | Correct statistical methods and insights |
| Dashboard and Visualization | 20 | Interactive and decision-relevant dashboard |
| Business Recommendations | 20 | Actionable and well-reasoned recommendations |
| Storytelling and Clarity | 10 | Professional and coherent communication |
| Total | 100 |  |

## Submission Checklist

### GitHub Repository

- [ ] Public repository uses naming convention `SectionName_TeamID_ProjectName`
- [ ] All notebooks committed in `.ipynb` format
- [ ] `data/raw/` contains original unedited dataset
- [ ] `data/processed/` contains cleaned output
- [ ] `tableau/` contains dashboard assets and links (or published URL reference)
- [ ] `data/data_dictionary.md` is complete
- [ ] `README.md` includes complete project details
- [ ] All members have visible commits and pull requests

### Tableau Dashboard

- [ ] Published on Tableau Public with accessible URL
- [ ] At least one interactive filter included
- [ ] Dashboard directly addresses the business problem

### Project Report

- [ ] Final report exported as PDF into `reports/`
- [ ] Includes executive summary, context, problem statement, and ETL methodology
- [ ] Includes EDA insights, statistical results, and dashboard explanation
- [ ] Includes 8-12 key insights and 3-5 actionable recommendations
- [ ] Contribution matrix matches GitHub history

### Presentation Deck

- [ ] Final presentation exported as PDF into `reports/`
- [ ] Includes title, problem, analysis, dashboard, recommendations, limitations, next steps

### Individual Assets

- [ ] DVA-oriented resume updated with this capstone
- [ ] Portfolio/case-study entry added

## Contribution Matrix

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Member 1 | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support |
| Member 2 | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support |
| Member 3 | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support |
| Member 4 | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support |
| Member 5 | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support |
| Member 6 | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support | Owner / support |

Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.

Team Lead Name: _____________________________  
Date: _______________

## Academic Integrity

All analysis, code, and recommendations in this repository must be the original work of the listed team members. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual contribution evidence may result in individual grade adjustments.

Newton School of Technology - Data Visualization & Analytics | Capstone 2
