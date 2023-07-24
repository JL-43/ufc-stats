from src import bronze_scrape_ufc_fighters
from src import silver_clean_ufc_data
import pandas as pd


def main():
    # Step 1: Scrape data
    ufc_stats_url = "http://ufcstats.com/statistics/fighters?char=*&page=all"
    bronze_df = bronze_scrape_ufc_fighters.scrape_fighter_data(ufc_stats_url)
    bronze_df.to_csv("./output/1_ufc_fighters_scraped.csv", index=False)
    print("Bronze csv written")

    # Step 2: Clean data
    bronze_df = pd.read_csv("./output/1_ufc_fighters_scraped.csv")
    silver_df = silver_clean_ufc_data.clean_fighter_data(bronze_df)
    silver_df.to_csv("./output/2_ufc_fighters_cleaned.csv", index=False)
    print("Silver csv written")

    # Further steps can be added here when they are implemented
    print("Finished running")


if __name__ == "__main__":
    main()
