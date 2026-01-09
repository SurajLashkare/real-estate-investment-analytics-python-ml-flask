import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from config import PROCESSED_DIR, MODEL_DIR, TARGET_COL, RANDOM_STATE
import os

os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(PROCESSED_DIR, "master_dataset.csv"))

features = ["Area_sqft", "price_per_sqft", "rental_yield_pct"]
X = df[features]
y = df[TARGET_COL]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

model = RandomForestRegressor(random_state=RANDOM_STATE)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(MODEL_DIR, "real_estate_price_model.pkl"))
print("Model trained and saved")
