# Data Dictionary

This project uses a reduced column set from the diabetes hospital encounter dataset so the analysis stays focused on readmission risk.

| Column | Type | Description | Keep Reason |
| --- | --- | --- | --- |
| `age` | categorical | Patient age band | Useful for risk segmentation |
| `gender` | categorical | Patient gender | Basic demographic comparison |
| `race` | categorical | Patient race | Demographic context |
| `admission_type_id` | categorical | Hospital admission type code | Core encounter severity context |
| `time_in_hospital` | numeric | Number of days in the hospital | Strong proxy for complexity |
| `num_medications` | numeric | Number of medications used | Captures treatment intensity |
| `number_emergency` | numeric | Prior emergency visits | Strong utilization signal |
| `number_inpatient` | numeric | Prior inpatient visits | Strong utilization signal |
| `A1Cresult` | categorical | A1C test result category | Diabetes control signal |
| `insulin` | categorical | Insulin medication status | Treatment signal |
| `readmitted` | categorical | Readmission bucket (`NO`, `>30`, `<30`) | Main outcome source |
| `admission_type` | categorical | Decoded admission type label | Tableau-friendly category |
| `readmitted_30` | binary | 1 if readmitted within 30 days, else 0 | Final target variable |
| `prior_inpatient_group` | categorical | Grouped prior inpatient visits | Easier dashboard story |
| `prior_emergency_group` | categorical | Grouped prior emergency visits | Easier dashboard story |
| `medication_burden_group` | categorical | Grouped medication count | Easier dashboard story |
| `stay_length_group` | categorical | Grouped time in hospital | Easier dashboard story |

## Excluded Early

| Column | Reason |
| --- | --- |
| `weight` | About 96.9% missing |
| `payer_code` | High missingness |
| `medical_specialty` | High missingness |
| individual drug columns | Too many low-value columns for the first pass |
