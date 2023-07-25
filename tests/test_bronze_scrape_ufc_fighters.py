## test_bronze_scrape_ufc_fighters.py
# import pandas as pd
# from pandas import DataFrame

import pyspark.pandas as ps
from pyspark.pandas import DataFrame
import pyspark
from delta import configure_spark_with_delta_pip
from src import bronze_scrape_ufc_fighters

builder = (
    pyspark.sql.SparkSession.builder.appName("test_bronze_scrape_ufc_fighters")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)


def test_scrape_fighter_data():
    url: str = "http://ufcstats.com/statistics/fighters?char=a&page=all"
    df: DataFrame = bronze_scrape_ufc_fighters.scrape_fighter_data(url)
    assert isinstance(df, ps.DataFrame)
    assert len(df) > 0
