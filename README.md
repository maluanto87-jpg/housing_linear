# 🏠 Housing Price Predictor

A web app that predicts median house value from district-level housing statistics, using a Polynomial Regression model trained on the California Housing dataset. Built with **Streamlit** and **scikit-learn**.

🔗 **Live demo:** # 🏠 Housing Price Predictor

A web app that predicts median house value from district-level housing statistics, using a Polynomial Regression model trained on the California Housing dataset. Built with **Streamlit** and **scikit-learn**.

🔗 **Live demo:**# 🏠 Housing Price Predictor

A web app that predicts median house value from district-level housing statistics, using a Polynomial Regression model trained on the California Housing dataset. Built with **Streamlit** and **scikit-learn**.

🔗 **Live demo:** https://housinglinear-b3zcwuijmy73fa7tdrpmmo.streamlit.app/

---

## 📋 Overview

This app takes five district-level statistics — **housing median age**, **total rooms**, **population**, **households**, and **median income** — and predicts the **median house value** for that district, using a degree-3 polynomial regression model.

---

## 🗂️ Project Structure

```
housing/
├── app.py              # Streamlit web app (trains model at startup)
├── housing.csv           # Training dataset (California Housing)
├── requirements.txt      # Python dependencies
├── runtime.txt            # Pinned Python version for deployment
└── README.md
```

---

## 🧠 Model

- **Algorithm:** Polynomial Regression (degree 3) — `PolynomialFeatures` + `LinearRegression` (scikit-learn)
- **Dataset:** California Housing dataset
- **Features used:** `housing_median_age`, `total_rooms`, `population`, `households`, `median_income`
- **Target:** `median_house_value`

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| R² Score | Proportion of variance explained |

> The app trains **two** versions of the model at startup: one on an 80/20 train/test split purely to compute honest performance metrics (shown in the app's expandable panel), and a second one trained on the **full dataset** which is what's actually used to generate predictions — matching the final model saved in the original notebook. There's no pickled model file, so there's no risk of scikit-learn version mismatches between your machine and the deployment environment.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
> On Windows, if `pip` isn't recognized, use `py -m pip install -r requirements.txt` instead.

### 3. Run the app locally
```bash
streamlit run app.py
```
> On Windows: `py -m streamlit run app.py`

The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Push this repo to GitHub, with `app.py`, `housing.csv`, `requirements.txt`, and `runtime.txt` all in the **root** folder (exact filenames — no spaces, no "(1)" suffixes; these are the most common causes of a broken deploy).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"**, select this repo and branch, and set the main file to `app.py`.
4. Click **Deploy** — Streamlit Cloud installs everything from `requirements.txt` automatically, using the Python version pinned in `runtime.txt`.
5. Copy the generated URL and share it, or add it to the top of this README.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [scikit-learn](https://scikit-learn.org/) — model training (Polynomial Regression)
- [pandas](https://pandas.pydata.org/) / [numpy](https://numpy.org/) — data handling

---

## 📌 Notes

- The **production model** used for predictions is trained on the full dataset with no held-out test set (matching the original notebook), so treat the displayed MAE/RMSE/R² metrics — computed from a separate train/test split — as an estimate of generalization performance, not an exact measure of the deployed model's accuracy.
- Rows with missing values in the required feature or target columns are dropped before training.
- Column names must exactly match `housing_median_age`, `total_rooms`, `population`, `households`, `median_income`, and `median_house_value`. If your CSV uses different names, update `FEATURE_ORDER` and `TARGET` in `app.py`.

---


---

## 📋 Overview

This app takes five district-level statistics — **housing median age**, **total rooms**, **population**, **households**, and **median income** — and predicts the **median house value** for that district, using a degree-3 polynomial regression model.

---

## 🗂️ Project Structure

```
housing/
├── app.py              # Streamlit web app (trains model at startup)
├── housing.csv           # Training dataset (California Housing)
├── requirements.txt      # Python dependencies
├── runtime.txt            # Pinned Python version for deployment
└── README.md
```

---

## 🧠 Model

- **Algorithm:** Polynomial Regression (degree 3) — `PolynomialFeatures` + `LinearRegression` (scikit-learn)
- **Dataset:** California Housing dataset
- **Features used:** `housing_median_age`, `total_rooms`, `population`, `households`, `median_income`
- **Target:** `median_house_value`

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| R² Score | Proportion of variance explained |

> The app trains **two** versions of the model at startup: one on an 80/20 train/test split purely to compute honest performance metrics (shown in the app's expandable panel), and a second one trained on the **full dataset** which is what's actually used to generate predictions — matching the final model saved in the original notebook. There's no pickled model file, so there's no risk of scikit-learn version mismatches between your machine and the deployment environment.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
> On Windows, if `pip` isn't recognized, use `py -m pip install -r requirements.txt` instead.

### 3. Run the app locally
```bash
streamlit run app.py
```
> On Windows: `py -m streamlit run app.py`

The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Push this repo to GitHub, with `app.py`, `housing.csv`, `requirements.txt`, and `runtime.txt` all in the **root** folder (exact filenames — no spaces, no "(1)" suffixes; these are the most common causes of a broken deploy).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"**, select this repo and branch, and set the main file to `app.py`.
4. Click **Deploy** — Streamlit Cloud installs everything from `requirements.txt` automatically, using the Python version pinned in `runtime.txt`.
5. Copy the generated URL and share it, or add it to the top of this README.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [scikit-learn](https://scikit-learn.org/) — model training (Polynomial Regression)
- [pandas](https://pandas.pydata.org/) / [numpy](https://numpy.org/) — data handling

---

## 📌 Notes

- The **production model** used for predictions is trained on the full dataset with no held-out test set (matching the original notebook), so treat the displayed MAE/RMSE/R² metrics — computed from a separate train/test split — as an estimate of generalization performance, not an exact measure of the deployed model's accuracy.
- Rows with missing values in the required feature or target columns are dropped before training.
- Column names must exactly match `housing_median_age`, `total_rooms`, `population`, `households`, `median_income`, and `median_house_value`. If your CSV uses different names, update `FEATURE_ORDER` and `TARGET` in `app.py`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📋 Overview

This app takes five district-level statistics — **housing median age**, **total rooms**, **population**, **households**, and **median income** — and predicts the **median house value** for that district, using a degree-3 polynomial regression model.

---

## 🗂️ Project Structure

```
housing/
├── app.py              # Streamlit web app (trains model at startup)
├── housing.csv           # Training dataset (California Housing)
├── requirements.txt      # Python dependencies
├── runtime.txt            # Pinned Python version for deployment
└── README.md
```

---

## 🧠 Model

- **Algorithm:** Polynomial Regression (degree 3) — `PolynomialFeatures` + `LinearRegression` (scikit-learn)
- **Dataset:** California Housing dataset
- **Features used:** `housing_median_age`, `total_rooms`, `population`, `households`, `median_income`
- **Target:** `median_house_value`

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| R² Score | Proportion of variance explained |

> The app trains **two** versions of the model at startup: one on an 80/20 train/test split purely to compute honest performance metrics (shown in the app's expandable panel), and a second one trained on the **full dataset** which is what's actually used to generate predictions — matching the final model saved in the original notebook. There's no pickled model file, so there's no risk of scikit-learn version mismatches between your machine and the deployment environment.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
> On Windows, if `pip` isn't recognized, use `py -m pip install -r requirements.txt` instead.

### 3. Run the app locally
```bash
streamlit run app.py
```
> On Windows: `py -m streamlit run app.py`

The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

1. Push this repo to GitHub, with `app.py`, `housing.csv`, `requirements.txt`, and `runtime.txt` all in the **root** folder (exact filenames — no spaces, no "(1)" suffixes; these are the most common causes of a broken deploy).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"**, select this repo and branch, and set the main file to `app.py`.
4. Click **Deploy** — Streamlit Cloud installs everything from `requirements.txt` automatically, using the Python version pinned in `runtime.txt`.
5. Copy the generated URL and share it, or add it to the top of this README.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [scikit-learn](https://scikit-learn.org/) — model training (Polynomial Regression)
- [pandas](https://pandas.pydata.org/) / [numpy](https://numpy.org/) — data handling

---

## 📌 Notes

- The **production model** used for predictions is trained on the full dataset with no held-out test set (matching the original notebook), so treat the displayed MAE/RMSE/R² metrics — computed from a separate train/test split — as an estimate of generalization performance, not an exact measure of the deployed model's accuracy.
- Rows with missing values in the required feature or target columns are dropped before training.
- Column names must exactly match `housing_median_age`, `total_rooms`, `population`, `households`, `median_income`, and `median_house_value`. If your CSV uses different names, update `FEATURE_ORDER` and `TARGET` in `app.py`.

---

