import pandas as pd

ufc_stats = "http://ufcstats.com/statistics/fighters?char=*&page=all"
df = pd.read_html(ufc_stats)[0]
df.reset_index(drop=True, inplace=True)
df.to_csv("../output/2_ufc_fighters_cleaned.csv", index=False)
