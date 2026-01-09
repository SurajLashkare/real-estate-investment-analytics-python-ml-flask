import pandas as pd
from config import PROCESSED_DIR
import os

df = pd.read_csv(os.path.join(PROCESSED_DIR, "master_dataset.csv"))

summary = df.groupby("City")["Price"].agg(["mean", "median", "count"]).reset_index()
summary.to_csv(os.path.join(PROCESSED_DIR, "city_price_summary.csv"), index=False)

print("EDA summary generated")
