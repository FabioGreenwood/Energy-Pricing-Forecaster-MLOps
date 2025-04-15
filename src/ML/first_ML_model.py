"""
===============================================================================
 File Name   : first_ML_model.py
 Description : For creating a sample simple pickled ML model for deploying an initial docker
 Author      : Fabio Greenwood
 Date Created: 2025-04-15
 Last Edited : YYYY-MM-DD
===============================================================================
"""

import os
import pickle
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# === Load data ===
data = pd.read_csv("data/sample_data.csv", parse_dates=['date'], index_col='date')

# === Optional: ensure it's sorted ===
data = data.sort_index()

# === Train a simple ARIMA model ===
model = ARIMA(data['value'], order=(1, 1, 1))  # ARIMA(p,d,q)
model_fit = model.fit()

# === Save the model ===
os.makedirs("models", exist_ok=True)
with open("models/forecast_model.pkl", "wb") as f:
    pickle.dump(model_fit, f)

print("Forecasting model trained and saved to models/forecast_model.pkl")
