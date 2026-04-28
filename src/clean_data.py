"""Command-line entry point for generating the cleaned diabetes dataset."""

import pandas as pd

from data_utils import build_clean_dataset, load_mapping_sections
from project_config import IDS_MAPPING_PATH, PROCESSED_DATA_PATH, RAW_DATA_PATH


def main() -> None:
    raw_df = pd.read_csv(RAW_DATA_PATH)
    mappings = load_mapping_sections(IDS_MAPPING_PATH)
    clean_df = build_clean_dataset(raw_df, mappings)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    clean_df.to_csv(PROCESSED_DATA_PATH, index=False)

    print(f"Saved cleaned dataset to: {PROCESSED_DATA_PATH}")
    print(f"Shape: {clean_df.shape[0]} rows x {clean_df.shape[1]} columns")


if __name__ == "__main__":
    main()
