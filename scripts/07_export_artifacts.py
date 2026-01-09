import os
from config import PROCESSED_DIR, MODEL_DIR

assert os.path.exists(os.path.join(PROCESSED_DIR, "master_dataset.csv"))
assert os.path.exists(os.path.join(MODEL_DIR, "real_estate_price_model.pkl"))

print("App artifacts verified and ready")
