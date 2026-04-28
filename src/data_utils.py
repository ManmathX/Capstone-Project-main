"""Utility functions for cleaning and preparing the diabetes dataset."""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

from project_config import READMISSION_TARGET_MAP, SELECTED_COLUMNS


def load_mapping_sections(mapping_path: Path) -> dict[str, dict[str, str]]:
    """Parse the IDS mapping file into section-based lookup dictionaries."""
    sections: dict[str, dict[str, str]] = {}
    current_section: str | None = None

    with mapping_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if not row:
                continue

            left = row[0].strip() if len(row) > 0 and row[0] else ""
            right = row[1].strip() if len(row) > 1 and row[1] else ""

            if not left and not right:
                continue

            if right == "description":
                current_section = left
                sections[current_section] = {}
                continue

            if current_section and left:
                sections[current_section][left] = right

    return sections


def group_prior_inpatient(value: int) -> str:
    if value == 0:
        return "0"
    if value == 1:
        return "1"
    if value == 2:
        return "2"
    return "3+"


def group_prior_emergency(value: int) -> str:
    if value == 0:
        return "0"
    if value == 1:
        return "1"
    return "2+"


def group_medication_burden(value: int) -> str:
    if value <= 10:
        return "0-10"
    if value <= 20:
        return "11-20"
    if value <= 30:
        return "21-30"
    return "31+"


def group_stay_length(value: int) -> str:
    if value <= 2:
        return "1-2 days"
    if value <= 4:
        return "3-4 days"
    if value <= 7:
        return "5-7 days"
    return "8+ days"


def build_clean_dataset(
    raw_df: pd.DataFrame,
    mappings: dict[str, dict[str, str]],
) -> pd.DataFrame:
    """Return a focused analysis dataset with derived fields."""
    clean_df = raw_df.copy()
    clean_df = clean_df.replace("?", pd.NA)
    clean_df = clean_df[SELECTED_COLUMNS].copy()

    numeric_columns = [
        "admission_type_id",
        "time_in_hospital",
        "num_medications",
        "number_emergency",
        "number_inpatient",
    ]
    for column in numeric_columns:
        clean_df[column] = pd.to_numeric(clean_df[column], errors="coerce")

    admission_mapping = mappings.get("admission_type_id", {})
    clean_df["admission_type"] = (
        clean_df["admission_type_id"]
        .fillna(-1)
        .astype(int)
        .astype(str)
        .map(admission_mapping)
        .fillna("Unknown")
    )

    clean_df["readmitted_30"] = clean_df["readmitted"].map(READMISSION_TARGET_MAP)
    clean_df["prior_inpatient_group"] = clean_df["number_inpatient"].apply(group_prior_inpatient)
    clean_df["prior_emergency_group"] = clean_df["number_emergency"].apply(group_prior_emergency)
    clean_df["medication_burden_group"] = clean_df["num_medications"].apply(group_medication_burden)
    clean_df["stay_length_group"] = clean_df["time_in_hospital"].apply(group_stay_length)

    return clean_df
