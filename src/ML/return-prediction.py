"""
===============================================================================
 File Name   : first_ML_model.py
 Description : For creating a sample simple pickled ML model for deploying an initial docker
 Author      : Fabio Greenwood
 Date Created: 2025-04-15
 Last Edited : YYYY-MM-DD
===============================================================================
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def first_docker_main(import_path="data/time_series.csv", output_path="data/output.csv"):

    print("start")
    # === Load data ===
    df = pd.read_csv(import_path, parse_dates=["date"], index_col="date")
    series = df["value"].values

    # === Convert to supervised format using sliding window ===
    def create_features(series, window_size=5):
        X, y = [], []
        for i in range(len(series) - window_size):
            X.append(series[i:i + window_size])
            y.append(series[i + window_size])
        return np.array(X), np.array(y)

    window_size = 5
    X, y = create_features(series, window_size)

    # === Train/test split ===
    split_train_val = int(len(X) * 0.75)
    split_val_test_neg = -int(len(X) * 0.15)

    X_train, X_val, X_test = X[:split_train_val], X[split_train_val:split_val_test_neg], X[split_val_test_neg:]
    y_train, y_val, y_test = y[:split_train_val], y[split_train_val:split_val_test_neg], y[split_val_test_neg:]

    # === Train model ===
    model = LinearRegression()
    model.fit(X_train, y_train)

    # === Validation ===
    y_pred = model.predict(X_val)
    print("Test MSE:", mean_squared_error(y_val, y_pred))


    # === Testing ===
    print("===========================")
    print("this is feed into the predict statement")
    print(X_test.reshape(1, -1))
    next_value = model.predict(X_test.reshape(1, -1))

    output = pd.DataFrame(next_value)

    output.to_csv(output_path)

    print(f"Predicted next value: {next_value}")


if __name__ == "__main__":

    first_docker_main()
