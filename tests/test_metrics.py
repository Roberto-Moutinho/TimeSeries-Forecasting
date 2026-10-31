import numpy as np
from scientometric_forecasting.metrics import mae, mse, rmse, smape, wape, r2, mase

def test_basic_metrics():
    y = [3, -0 if False else 5, 7]
    p = [2, 5, 8]
    assert mae(y, p) == 2/3
    assert np.isclose(mse(y, p), 2/3)
    assert np.isclose(rmse(y, p), np.sqrt(2/3))
    assert np.isfinite(smape(y, p))
    assert np.isfinite(wape(y, p))
    assert np.isfinite(r2(y, p))

def test_mase():
    assert np.isfinite(mase([4, 5], [3, 6], [1, 2, 3, 4]))
