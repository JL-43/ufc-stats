## test_silver_clean_ufc_data.py
# import pandas as pd

import pyspark.pandas as ps
from pyspark.pandas import DataFrame
import pyspark
from delta import configure_spark_with_delta_pip
from src import silver_clean_ufc_data as clean_data
import pytest

builder = (
    pyspark.sql.SparkSession.builder.appName("test_silver_clean_ufc_data")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()


def test_convert_height_in_feet_string_to_cm_double():
    # Test a normal case
    height_in_feet: str = "6' 2\""
    expected_height_in_cm: float = 187.96
    actual_height_in_cm: float = clean_data.convert_height_in_feet_string_to_cm_double(
        height_in_feet
    )
    assert actual_height_in_cm == pytest.approx(
        expected_height_in_cm
    ), "Conversion of height in feet to cm failed for normal case"

    # Test a corner case
    height_in_feet: str = "0"
    expected_height_in_cm: float = 0.0
    actual_height_in_cm: float = clean_data.convert_height_in_feet_string_to_cm_double(
        height_in_feet
    )
    assert actual_height_in_cm == pytest.approx(
        expected_height_in_cm
    ), "Conversion of height in feet to cm failed for corner case"


spark.stop()
