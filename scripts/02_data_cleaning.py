import pandas as pd 
from config import PROCESSED_DIR
import os

raw_path = os.path.join(PROCESSED_DIR, "raw_datasets.pkl")
datasets = pd.read_pickle(raw_path)

df = datasets["real_estate"]

df.columns = df.columns.str.strip()
df = df.drop_duplicates()

df["City"] = df["City"].fillna("Unknown")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df[df["Price"].notna()]

df.to_csv(os.path.join(PROCESSED_DIR, "clean_real_estate.csv"), index=False)
print("Data cleaning completed")
