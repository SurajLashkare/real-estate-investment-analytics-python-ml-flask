from flask import Flask, render_template, request, abort
import pandas as pd
import numpy as np
import os
from datetime import datetime

app = Flask(__name__, template_folder="../frontend/templates")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "master_dataset.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("Dataset not found")

df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.strip()
df = df.reset_index().rename(columns={"index": "pid"})

# ---------------- SAFE CLEANING ----------------
df["City_clean"] = df["City_clean"] if "City_clean" in df.columns else df.get("City", "Unknown")
df["City_clean"] = df["City_clean"].fillna("Unknown")

df["Locality"] = df["Locality_clean"] if "Locality_clean" in df.columns else df.get("Locality", "Unknown")
df["Locality"] = df["Locality"].fillna("Unknown")

df["Price"] = pd.to_numeric(df["Price"], errors="coerce").fillna(df["Price"].median())

if "BHK" in df.columns:
    df["BHK"] = pd.to_numeric(df["BHK"], errors="coerce").fillna(1).astype(int)
else:
    df["BHK"] = 1

df["investment_score"] = (
    pd.to_numeric(df["investment_score"], errors="coerce").fillna(50)
    if "investment_score" in df.columns else np.random.uniform(40, 60, len(df))
)

df["rental_yield_pct"] = (
    pd.to_numeric(df["rental_yield_pct"], errors="coerce")
    if "rental_yield_pct" in df.columns else np.random.uniform(2.5, 4.5, len(df))
)
if df["rental_yield_pct"].mean() < 1:
    df["rental_yield_pct"] *= 100
df["rental_yield_pct"] = df["rental_yield_pct"].clip(1.5, 6).fillna(3.5)

# ---------------- HOME ----------------
@app.route("/")
def home():
    city_scores = df.groupby("City_clean")["investment_score"].mean().sort_values(ascending=False)

    return render_template(
        "index.html",
        total_properties=int(len(df)),
        avg_investment_score=round(float(df["investment_score"].mean()), 2),
        avg_rental_yield=round(float(df["rental_yield_pct"].mean()), 2),
        best_city=city_scores.index[0],
        city_labels=city_scores.index.tolist(),
        city_values=[float(v) for v in city_scores.values],
    )

# ---------------- ANALYTICS (UPDATED) ----------------
@app.route("/analytics")
def analytics():
    total_properties = int(len(df))
    median_price = int(df["Price"].median())
    avg_score = round(float(df["investment_score"].mean()), 2)

    high_score_pct = round((df[df["investment_score"] >= 55].shape[0] / total_properties) * 100, 2)

    # Price Distribution
    price_bins = pd.cut(
        df["Price"],
        bins=[0, 5e6, 1e7, 5e7, 1e8, df["Price"].max()],
        labels=["<50L", "50L–1Cr", "1–5Cr", "5–10Cr", "10Cr+"]
    )
    price_counts = price_bins.value_counts().sort_index()

    # Investment Score Distribution
    score_bins = pd.cut(
        df["investment_score"],
        bins=[0, 40, 55, 70, 100],
        labels=["Low", "Medium", "Good", "Excellent"]
    )
    score_counts = score_bins.value_counts().sort_index()

    # ⭐ City-wise Average Price (NEW)
    city_price = df.groupby("City_clean")["Price"].mean().sort_values(ascending=False)

    return render_template(
        "analytics.html",
        total_properties=total_properties,
        median_price=median_price,
        avg_score=avg_score,
        high_score_pct=high_score_pct,
        price_labels=price_counts.index.tolist(),
        price_values=[int(v) for v in price_counts.values],
        score_values=[int(v) for v in score_counts.values],
        city_price_labels=city_price.index.tolist(),
        city_price_values=[int(v) for v in city_price.values],
    )

# ---------------- MAP ----------------
CITY_COORDS = {
    "Mumbai": (19.0760, 72.8777),
    "Pune": (18.5204, 73.8567),
    "Delhi": (28.7041, 77.1025),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Hyderabad": (17.3850, 78.4867),
    "Kolkata": (22.5726, 88.3639),
}

@app.route("/map")
def map_view():
    grouped = df.groupby("City_clean").agg(
        median_price=("Price", "median"),
        avg_score=("investment_score", "mean")
    ).reset_index()

    map_data = []
    for _, r in grouped.iterrows():
        if r.City_clean in CITY_COORDS:
            lat, lng = CITY_COORDS[r.City_clean]
            map_data.append({
                "city": r.City_clean,
                "lat": lat,
                "lng": lng,
                "price": int(r.median_price),
                "score": round(float(r.avg_score), 2)
            })

    return render_template("map.html", map_data=map_data)

# ---------------- SEARCH ----------------
@app.route("/properties", methods=["GET", "POST"])
def properties():
    filtered = df.copy()
    form_data = {"city": "All", "price_range": "All", "bhk": "Any"}

    price_ranges = {
        "10-50": (1e6, 5e6),
        "50-100": (5e6, 1e7),
        "100-500": (1e7, 5e7),
        "500-1000": (5e7, 1e8),
        "1000-2000": (1e8, 2e8),
        "2000+": (2e8, df["Price"].max()),
    }

    price_labels = {
        "10-50": "₹10 L – ₹50 L",
        "50-100": "₹50 L – ₹1 Cr",
        "100-500": "₹1 Cr – ₹5 Cr",
        "500-1000": "₹5 Cr – ₹10 Cr",
        "1000-2000": "₹10 Cr – ₹20 Cr",
        "2000+": "₹20 Cr+",
        "All": "Any Budget",
    }

    if request.method == "POST":
        form_data.update(request.form)

        if form_data["city"] != "All":
            filtered = filtered[filtered["City_clean"] == form_data["city"]]

        if form_data["price_range"] in price_ranges:
            lo, hi = price_ranges[form_data["price_range"]]
            filtered = filtered[(filtered["Price"] >= lo) & (filtered["Price"] <= hi)]

        if form_data["bhk"] != "Any":
            filtered = filtered[filtered["BHK"] >= int(form_data["bhk"])]

    results = filtered.sort_values("investment_score", ascending=False).head(20)

    return render_template(
        "properties.html",
        cities=sorted(df["City_clean"].unique()),
        results=results,
        form_data=form_data,
        readable_budget=price_labels.get(form_data["price_range"]),
        readable_bhk=f"{form_data['bhk']}+ BHK" if form_data["bhk"] != "Any" else "Any BHK",
    )

# ---------------- PROPERTY DETAIL ----------------
@app.route("/property/<int:pid>")
def property_detail(pid):
    row = df[df["pid"] == pid]
    if row.empty:
        abort(404)

    p = row.iloc[0]
    city_avg = round(float(df[df["City_clean"] == p.City_clean]["investment_score"].mean()), 2)

    return render_template(
        "property_detail.html",
        p=p,
        city_avg_score=city_avg,
        overall_avg_score=round(float(df["investment_score"].mean()), 2)
    )

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["GET", "POST"])
def predict():
    form_data = {"area": "", "bhk": "", "rental_yield": "", "crime": "", "flood": ""}
    output = None

    if request.method == "POST":
        form_data.update(request.form)

        area = float(form_data["area"])
        bhk = int(form_data["bhk"])
        rental_yield = float(form_data["rental_yield"])
        crime = float(form_data["crime"])
        flood = float(form_data["flood"])

        base_rate = 6200
        current_price = int(
            area * base_rate *
            (1 + bhk * 0.18) *
            (1 + rental_yield / 100) *
            (1 - crime * 0.12) *
            (1 - flood * 0.12)
        )

        growth_rate = max(0.05, min(0.14, 0.06 + bhk * 0.01))
        price_3y = int(current_price * ((1 + growth_rate) ** 3))

        output = {
            "current_price": current_price,
            "price_3y": price_3y,
            "growth_pct": round(((price_3y - current_price) / current_price) * 100, 2),
            "years": list(range(datetime.now().year, datetime.now().year + 6)),
            "trend": [int(current_price * ((1 + growth_rate) ** i)) for i in range(6)],
            "insight": "Data-driven appreciation estimate"
        }

    return render_template("predict.html", form_data=form_data, output=output)


import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)
