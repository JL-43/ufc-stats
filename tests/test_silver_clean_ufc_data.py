# test_silver_clean_ufc_data.py
import pytest
import pandas as pd
from src import silver_clean_ufc_data as clean_data


def test_convert_height_in_feet_string_to_cm_double():
    # Test a normal case
    height_in_feet = "6' 2\""
    expected_height_in_cm = 187.96
    actual_height_in_cm = clean_data.convert_height_in_feet_string_to_cm_double(
        height_in_feet
    )
    assert actual_height_in_cm == pytest.approx(
        expected_height_in_cm
    ), "Conversion of height in feet to cm failed for normal case"

    # Test a corner case
    height_in_feet = "0"
    expected_height_in_cm = 0.0
    actual_height_in_cm = clean_data.convert_height_in_feet_string_to_cm_double(
        height_in_feet
    )
    assert actual_height_in_cm == pytest.approx(
        expected_height_in_cm
    ), "Conversion of height in feet to cm failed for corner case"
