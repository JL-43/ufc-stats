## 1_scrape_ufc_fighters.py
# import pandas as pd
# from pandas import DataFrame

import pyspark.pandas as ps
from pyspark.pandas import DataFrame
import pyspark
from delta import configure_spark_with_delta_pip

builder = (
    pyspark.sql.SparkSession.builder.appName("bronze_scrape_ufc_fighters")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()


def scrape_fighter_data(url: str) -> DataFrame:
    df = ps.read_html(url)[0]
    df.reset_index(drop=True, inplace=True)

    return df


if __name__ == "__main__":
    ufc_stats_url: str = "http://ufcstats.com/statistics/fighters?char=*&page=all"
    bronze_df: DataFrame = scrape_fighter_data(ufc_stats_url)
    bronze_df.to_delta("../output/1_ufc_fighters_scraped", index=False)

    read_df: DataFrame = ps.read_delta("../output/1_ufc_fighters_scraped")

    # print(read_df.head())


# data = spark.range(0, 5)
# data.write.format("delta").save("./tmp/delta-table")
