# test_bronze_scrape_ufc_fighters.py
import pandas as pd
from pandas import DataFrame
from src import bronze_scrape_ufc_fighters


def test_scrape_fighter_data():
    url: str = "http://ufcstats.com/statistics/fighters?char=a&page=all"
    df: DataFrame = bronze_scrape_ufc_fighters.scrape_fighter_data(url)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
