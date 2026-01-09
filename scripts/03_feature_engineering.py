import pandas as pd
from config import PROCESSED_DIR
import os

df = pd.read_csv(os.path.join(PROCESSED_DIR, "clean_real_estate.csv"))

df["price_per_sqft"] = df["Price"] / df["Area_sqft"]
df["rental_yield_pct"] = (df["Avg_Rent"] * 12 / df["Price"]) * 100

df["investment_score"] = (
    df["price_per_sqft"].rank(pct=True) * 0.5 +
    df["rental_yield_pct"].rank(pct=True) * 0.5
)

df.to_csv(os.path.join(PROCESSED_DIR, "master_dataset.csv"), index=False)
print("Feature engineering completed")
