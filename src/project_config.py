"""Project-level constants for the capstone workflow."""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = ROOT_DIR / "data" / "raw" / "diabetic_data.csv"
IDS_MAPPING_PATH = ROOT_DIR / "data" / "raw" / "IDS_mapping.csv"
PROCESSED_DATA_PATH = ROOT_DIR / "data" / "processed" / "clean_diabetes.csv"

SELECTED_COLUMNS = [
    "age",
    "gender",
    "race",
    "admission_type_id",
    "time_in_hospital",
    "num_medications",
    "number_emergency",
    "number_inpatient",
    "A1Cresult",
    "insulin",
    "readmitted",
]

READMISSION_TARGET_MAP = {
    "NO": 0,
    ">30": 0,
    "<30": 1,
}

CATEGORICAL_COLUMNS = [
    "age",
    "gender",
    "race",
    "admission_type",
    "A1Cresult",
    "insulin",
    "prior_inpatient_group",
    "prior_emergency_group",
    "medication_burden_group",
    "stay_length_group",
]

NUMERIC_COLUMNS = [
    "time_in_hospital",
    "num_medications",
    "number_emergency",
    "number_inpatient",
]
