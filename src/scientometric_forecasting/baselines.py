"""Simple forecasting baselines."""
import numpy as np

def naive_last_value(train, horizon):
    train = np.asarray(train, dtype=float).reshape(-1)
    if train.size == 0 or horizon < 1:
        raise ValueError("Non-empty training data and positive horizon required.")
    return np.repeat(train[-1], horizon)
