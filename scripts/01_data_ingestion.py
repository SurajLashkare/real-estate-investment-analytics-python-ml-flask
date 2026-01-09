import pandas as pd 
from config import DATA_DIR, PROCESSED_DIR
import os

os.makedirs(PROCESSED_DIR, exist_ok=True)

files = {
    "apartment": "apartment.csv",
    "crime": "Crime_Rate.csv",
    "rent": "House_Rent_Dataset.csv",
    "real_estate": "Real_Estate_Data.csv",
    "weather": "Weather_Events_India.csv"
}

datasets = {}

for name, file in files.items():
    path = os.path.join(DATA_DIR, file)
    datasets[name] = pd.read_csv(path)
    print(f"{name} loaded: {datasets[name].shape}")

pd.to_pickle(datasets, os.path.join(PROCESSED_DIR, "raw_datasets.pkl"))
print("Data ingestion completed")
