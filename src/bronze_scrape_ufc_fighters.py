# 1_scrape_ufc_fighters.py
import pandas as pd
from pandas import DataFrame


def scrape_fighter_data(url: str) -> DataFrame:
    df = pd.read_html(url)[0]
    df.reset_index(drop=True, inplace=True)

    return df


if __name__ == "__main__":
    ufc_stats_url = "http://ufcstats.com/statistics/fighters?char=*&page=all"
    bronze_df = scrape_fighter_data(ufc_stats_url)
    bronze_df.to_csv("../output/2_ufc_fighters_cleaned.csv", index=False)
