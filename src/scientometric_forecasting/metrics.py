"""Forecast evaluation metrics for numeric time series."""
from __future__ import annotations
import numpy as np

def _arrays(y_true, y_pred):
    y = np.asarray(y_true, dtype=float).reshape(-1)
    p = np.asarray(y_pred, dtype=float).reshape(-1)
    if y.shape != p.shape:
        raise ValueError("y_true and y_pred must have the same shape.")
    if y.size == 0:
        raise ValueError("At least one observation is required.")
    if not (np.isfinite(y).all() and np.isfinite(p).all()):
        raise ValueError("Inputs must contain only finite values.")
    return y, p

def mae(y_true, y_pred):
    y, p = _arrays(y_true, y_pred)
    return float(np.mean(np.abs(y - p)))

def mse(y_true, y_pred):
    y, p = _arrays(y_true, y_pred)
    return float(np.mean((y - p) ** 2))

def rmse(y_true, y_pred):
    return float(np.sqrt(mse(y_true, y_pred)))

def mape(y_true, y_pred):
    y, p = _arrays(y_true, y_pred)
    if np.any(y == 0):
        return float("nan")
    return float(np.mean(np.abs((y - p) / y)) * 100.0)

def smape(y_true, y_pred):
    y, p = _arrays(y_true, y_pred)
    denom = np.abs(y) + np.abs(p)
    terms = np.divide(2.0 * np.abs(y - p), denom,
                      out=np.zeros_like(denom), where=denom != 0)
    return float(np.mean(terms) * 100.0)

def wape(y_true, y_pred):
    y, p = _arrays(y_true, y_pred)
    denom = np.sum(np.abs(y))
    return float("nan") if denom == 0 else float(np.sum(np.abs(y-p)) / denom * 100.0)

def r2(y_true, y_pred):
    y, p = _arrays(y_true, y_pred)
    ss_res = np.sum((y-p)**2)
    ss_tot = np.sum((y-np.mean(y))**2)
    return float("nan") if ss_tot == 0 else float(1.0 - ss_res/ss_tot)

def mase(y_true, y_pred, y_train, seasonality=1):
    y, p = _arrays(y_true, y_pred)
    train = np.asarray(y_train, dtype=float).reshape(-1)
    if seasonality < 1 or len(train) <= seasonality:
        raise ValueError("Training data must be longer than seasonality.")
    scale = np.mean(np.abs(train[seasonality:] - train[:-seasonality]))
    if scale == 0:
        return float("nan")
    return float(np.mean(np.abs(y-p)) / scale)

def calculate_metrics(y_true, y_pred, y_train=None, seasonality=1):
    result = {
        "MAE": mae(y_true, y_pred),
        "MSE": mse(y_true, y_pred),
        "RMSE": rmse(y_true, y_pred),
        "MAPE_percent": mape(y_true, y_pred),
        "sMAPE_percent": smape(y_true, y_pred),
        "WAPE_percent": wape(y_true, y_pred),
        "R2": r2(y_true, y_pred),
    }
    result["MASE"] = (mase(y_true, y_pred, y_train, seasonality)
                      if y_train is not None else float("nan"))
    return result
