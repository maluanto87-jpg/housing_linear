"""
app.py — Housing Price Predictor (Streamlit)

Trains a Polynomial Regression model at startup directly from
housing.csv (matches housing_Linear.ipynb), avoiding any
scikit-learn pickle version-mismatch issues on deployment.

Run locally:
    streamlit run app.py

Deploy:
    Push app.py, housing.csv, and requirements.txt to a GitHub repo,
    then deploy on https://share.streamlit.io (Streamlit Community Cloud).
"""

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------------------------------------------------------------
# Page config
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Housing Price Predictor",
    page_icon="🏠",
    layout="centered",
)

FEATURE_ORDER = ["housing_median_age", "total_rooms", "population", "households", "median_income"]
TARGET = "median_house_value"
DEGREE = 3  # matches the final model trained in the source notebook

# ---------------------------------------------------------------
# Train model (cached so it only runs once per app session)
# ---------------------------------------------------------------
@st.cache_resource(show_spinner="Training model...")
def train_model():
    df = pd.read_csv("housing.csv")
    df = df.dropna(subset=FEATURE_ORDER + [TARGET])

    X = df[FEATURE_ORDER]
    y = df[TARGET]

    # Held-out split, purely to report honest performance metrics in the app
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    poly_eval = PolynomialFeatures(degree=DEGREE)
    X_train_poly = poly_eval.fit_transform(X_train)
    X_test_poly = poly_eval.transform(X_test)
    eval_model = LinearRegression()
    eval_model.fit(X_train_poly, y_train)
    y_pred = eval_model.predict(X_test_poly)
    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "MSE": mean_squared_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "R2": r2_score(y_test, y_pred),
    }

    # Final production model: trained on the FULL dataset (matches the notebook's
    # final pickled model, used for the actual predictions below)
    poly = PolynomialFeatures(degree=DEGREE)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)

    return model, poly, metrics

model, poly, metrics = train_model()

# ---------------------------------------------------------------
# Header
# ---------------------------------------------------------------
st.title("🏠 Housing Price Predictor")
st.write(
    "Predicts median house value from housing/population statistics, "
    "using a degree-3 polynomial regression model trained on the "
    "California housing dataset."
)

with st.expander("Model performance (on held-out test data)"):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("MAE", f"{metrics['MAE']:,.0f}")
    c2.metric("RMSE", f"{metrics['RMSE']:,.0f}")
    c3.metric("MSE", f"{metrics['MSE']:,.0f}")
    c4.metric("R² Score", f"{metrics['R2']:.3f}")

st.divider()

# ---------------------------------------------------------------
# Input form
# ---------------------------------------------------------------
st.subheader("Enter District Details")

col1, col2 = st.columns(2)

with col1:
    housing_median_age = st.number_input("Housing Median Age", min_value=0, max_value=100, value=21, step=1)
    total_rooms = st.number_input("Total Rooms", min_value=0, value=7099, step=1)
    population = st.number_input("Population", min_value=0, value=2401, step=1)

with col2:
    households = st.number_input("Households", min_value=0, value=1138, step=1)
    median_income = st.number_input(
        "Median Income (in tens of thousands $)", min_value=0.0, value=8.3014, step=0.01
    )

st.divider()

# ---------------------------------------------------------------
# Predict
# ---------------------------------------------------------------
if st.button("🔍 Predict Price", use_container_width=True, type="primary"):
    input_data = pd.DataFrame([[
        housing_median_age, total_rooms, population, households, median_income,
    ]], columns=FEATURE_ORDER)

    input_poly = poly.transform(input_data)
    prediction = model.predict(input_poly)[0]

    st.subheader("Result")
    st.success(f"### Predicted Median House Value: ${prediction:,.2f}")

    with st.expander("See input summary"):
        st.dataframe(input_data)

st.divider()
st.caption("Model: Polynomial Regression (degree 3) | Dataset: California Housing Dataset")
