# Methodology

## Source-derived research design

The research report describes:
- Scientometric indicators: journal publications, research projects initiated, and academic supervisions.
- Knowledge-area stratification: the eight major CAPES areas.
- Data sources and identifiers: Lattes, OpenAlex, the research group's scientometrics database, journal ISSN identifiers, and researcher Lattes IDs.
- Forecasting model: recurrent neural network with LSTM units.
- Comparative trend model: polynomial nonlinear regression.

## Additional evaluation protocol

For a new reproducible benchmark:
1. Sort each series chronologically.
2. Reserve a final contiguous test period.
3. Fit preprocessing transformations on training data only.
4. Tune hyperparameters using training/validation data only.
5. Generate forecasts for the untouched test horizon.
6. Compare each model with a naïve baseline.
7. Calculate the metrics in `src/scientometric_forecasting/metrics.py`.
8. Preserve predictions, configuration, logs, and software versions.

Do not report a metric unless it was computed from saved observed/predicted pairs. For count data, retain the original scale when reporting MAE and RMSE.
