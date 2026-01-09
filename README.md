
# 🏡 Real Estate Investment Analytics & Scoring System

This project is a **data-driven Real Estate Investment Analytics system** designed to demonstrate a complete **data analytics workflow** — from raw data processing to insight generation and ML-based price prediction.

It focuses on **data cleaning, exploratory data analysis (EDA), feature engineering, and predictive modeling**, with results delivered through a **Flask-based web application** for easy visualization and decision support.

This project is ideal for:

* 📊 Data Analyst / Business Intelligence portfolios
* 📈 Real-world data analytics case studies
* 🤖 ML-assisted analytics projects
* 💼 Interview & hiring assessments

---

## 📄 Business Problem

Real estate investors often face challenges in making **accurate, data-driven investment decisions** due to:

* Fragmented data from multiple sources (pricing, rent, crime, weather, location)
* Inconsistent and noisy datasets
* Difficulty in evaluating **risk vs return** for properties
* Lack of reliable price estimation tools
* Limited insight into location-based investment potential

Without proper analysis, investors may:

* Overpay for properties
* Invest in high-risk areas
* Miss high-yield opportunities
* Make decisions based on intuition rather than data

### 🎯 Project Goal

The goal of this project is to build a **data analytics–driven system** that:

* Cleans and integrates multiple real estate datasets
* Performs exploratory data analysis (EDA) to uncover trends
* Engineers meaningful features for better insights
* Uses machine learning to predict fair property prices
* Visualizes key insights through an interactive web application

This enables investors to make **informed, evidence-based real estate investment decisions**.

---

## 📌 Project Objective

The main objective of this project is to support **data-driven real estate investment decisions** by analyzing:

* Property pricing trends
* Rental yield performance
* Risk indicators (e.g., crime rate, location factors)
* Location-based investment potential
* ML-based price predictions

---

## 🔍 Data Analytics Focus

This project emphasizes **core data analytics skills** used in real-world scenarios.

### 1️⃣ Data Collection

Multiple datasets were collected, including:

* Property price data
* Rental data
* Crime rate data
* Weather and location data

---

### 2️⃣ Data Cleaning & Preparation

Performed using **Python**:

* Handling missing values
* Removing outliers
* Fixing inconsistent formats
* Merging multiple datasets into a master dataset

Notebook used:
`01_Data_Cleaning.ipynb`

---

### 3️⃣ Exploratory Data Analysis (EDA)

Key insights were extracted using:

* Price distribution analysis
* Rental yield trends
* Location-wise comparisons
* Risk factor analysis

Notebook used:
`03_Exploratory_Data_Analysis.ipynb`

---

### 4️⃣ Feature Engineering

Created meaningful features such as:

* Price per square foot
* Rental yield ratios
* Location-based indicators
* Risk-related variables

Notebook used:
`02_Feature_Engineering.ipynb`

---

### 5️⃣ Machine Learning (Regression Model)

A regression model was trained to:

* Predict property prices
* Improve valuation accuracy
* Support investment decisions

Notebooks used:
`04_Model_Training.ipynb`
`05_Final_Validation.ipynb`

Saved model:
`models/real_estate_price_model.pkl`

---

### 6️⃣ Insight Generation

The analysis helps answer questions like:

* Which locations offer better returns?
* How do risk factors affect pricing?
* What price range is fair for a property?
* Which areas are good for long-term investment?

---

## 🌐 Web Application (Insight Delivery Layer)

The Flask web application is used to **present analytics results** in a user-friendly way.

Features include:

* Property search & filtering
* ML-based price prediction
* Interactive charts
* Location-based maps
* Investment comparison views

This ensures **data insights are accessible to non-technical users**.

Main file:
`backend/app.py`

---

## 🛠️ Tools & Technologies Used

* **Python** – Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning** – Scikit-learn (Regression)
* **Flask** – Web application framework
* **HTML/CSS/Bootstrap** – Frontend UI
* **Jupyter Notebook** – EDA & modeling
* **Git & GitHub** – Version control

---

## 📂 Repository Structure

```
real-estate-investment-analytics-python-ml-flask/
│
├── backend/
│   └── app.py
│
├── data/
│   ├── processed/
│   │   └── master_dataset.csv
│   │
│   └── raw/
│       ├── apartment.csv
│       ├── Crime_Rate.csv
│       ├── House_Rent_Dataset.csv
│       ├── Real_Estate_Data.csv
│       └── Weather_Events_India.csv
│
├── frontend/
│   └── templates/
│       ├── index.html
│       ├── Analytics.html
│       ├── map.html
│       ├── predict.html
│       ├── properties.html
│       └── property_detail.html
│
├── images/
│   ├── Home Page.png
│   ├── Analytics Tab.png
│   ├── Map Tab.png
│   ├── Prediction Tab_image1.png
│   └── Search_Properties_Tab_image1.png
│
├── models/
│   └── real_estate_price_model.pkl
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Final_Validation.ipynb
│
├── scripts/
│   ├── 01_data_ingestion.py
│   ├── 02_data_cleaning.py
│   ├── 03_feature_engineering.py
│   ├── 04_eda_summary.py
│   ├── 05_model_training.py
│   ├── 06_model_evaluation.py
│   ├── 07_export_artifacts.py
│   └── config.py
│
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SurajLashkare/real-estate-investment-analytics-python-ml-flask.git
cd real-estate-investment-analytics-python-ml-flask
```

### 2️⃣ Run the Flask App

```bash
python backend/app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📊 Key Business Questions Answered

* Which locations offer the highest rental yield?
* How do property prices vary by region?
* What risk factors impact investment returns?
* Can ML predict fair property prices?
* Which areas show strong investment potential?

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>  

**Suraj Lashkare**
Aspiring Data Analyst
🔗 [LinkedIn](https://www.linkedin.com/in/suraj-lashkare-2605a52aa/)


