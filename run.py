# run.py
from src import bronze_scrape_ufc_fighters
from src import silver_clean_ufc_data
import pyspark.pandas as ps
from pyspark.pandas import DataFrame

import pyspark

# from delta import configure_spark_with_delta_pip
from delta.pip_utils import configure_spark_with_delta_pip

builder = (
    pyspark.sql.SparkSession.builder.appName("main_app")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()


def main():
    # Step 1: Scrape data
    ufc_stats_url = "http://ufcstats.com/statistics/fighters?char=*&page=all"
    bronze_df = bronze_scrape_ufc_fighters.scrape_fighter_data(ufc_stats_url)
    bronze_df.to_delta("./output/1_ufc_fighters_scraped")
    print("Bronze delta written")

    # Step 2: Clean data
    bronze_df = ps.read_delta("./output/1_ufc_fighters_scraped")
    silver_df = silver_clean_ufc_data.clean_fighter_data(bronze_df)
    silver_df.to_delta("./output/2_ufc_fighters_cleaned")
    print("Silver delta written")

    # Further steps can be added here when they are implemented
    print("Finished running")


if __name__ == "__main__":
    main()
    spark.stop()
