import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

RANDOM_STATE = 42
TARGET_COL = "Price"
