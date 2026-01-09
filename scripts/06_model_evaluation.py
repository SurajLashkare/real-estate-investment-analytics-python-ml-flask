import pandas as pd
import joblib
from sklearn.metrics import r2_score, mean_squared_error
from config import PROCESSED_DIR, MODEL_DIR
import numpy as np
import os

df = pd.read_csv(os.path.join(PROCESSED_DIR, "master_dataset.csv"))
model = joblib.load(os.path.join(MODEL_DIR, "real_estate_price_model.pkl"))

X = df[["Area_sqft", "price_per_sqft", "rental_yield_pct"]]
y = df["Price"]

preds = model.predict(X)

print("R2:", r2_score(y, preds))
print("RMSE:", np.sqrt(mean_squared_error(y, preds)))
