# 2_clean_ufc_data.py
import pandas as pd
from pandas import DataFrame


def convert_height_in_feet_string_to_cm_double(height_in_feet: str) -> float:
    if len(height_in_feet) < 2:  # exception if height is 0
        return 0.0

    height_in_feet_cleaned = height_in_feet.replace("'", "").replace('"', "")

    feet = height_in_feet_cleaned.split()[0]
    inches = height_in_feet_cleaned.split()[1]

    # 1 foot = 30.48 cm
    feet_to_cm = float(feet) * 30.48

    # 1 inch = 2.54 cm
    inch_to_cm = float(inches) * 2.54

    total_height = feet_to_cm + inch_to_cm

    return total_height


def convert_reach_in_inches_string_to_cm_double(reach_in_inches: str) -> float:
    if len(reach_in_inches) < 2:  # exception if height is 0
        return 0.0

    reach_in_inches_cleaned = reach_in_inches.replace('"', "")

    # 1 inch = 2.54 cm
    inch_to_cm = float(reach_in_inches_cleaned) * 2.54
    total_reach = inch_to_cm

    return total_reach


def clean_fighter_data(df: DataFrame) -> DataFrame:
    # remove first row
    df = df[1:]
    # replace NaN with 0
    df = df.fillna(0)
    # replace '--' string with 0
    df = df.replace(to_replace="--", value="0", regex=True)
    # clean weight & height columnds
    df["Wt."] = df["Wt."].replace(to_replace=" lbs.", value="", regex=True)
    df["Ht."] = df["Ht."].apply(convert_height_in_feet_string_to_cm_double)
    df["Reach"] = df["Reach"].apply(convert_reach_in_inches_string_to_cm_double)
    df = df.rename(
        columns={
            "Wt.": "Weight in lbs",
            "Ht.": "Height in cm",
            "Reach": "Reach in inches",
        }
    )

    return df


if __name__ == "__main__":
    bronze_df = pd.read_csv("../output/1_ufc_fighters_scraped.csv")
    silver_df = clean_fighter_data(bronze_df)
    silver_df.to_csv("../output/2_ufc_fighters_cleaned.csv", index=False)
