# Reproducibility checklist

- [ ] Record the exact data source and extraction date.
- [ ] Record data coverage and missing-year handling.
- [ ] Record indicator and knowledge-area definitions.
- [ ] Record train/validation/test boundaries.
- [ ] Prevent temporal leakage in preprocessing and tuning.
- [ ] Record model architecture and every hyperparameter.
- [ ] Record random seeds and software versions.
- [ ] Save predictions paired with actual test observations.
- [ ] Evaluate against a naïve baseline.
- [ ] Report MAE, RMSE, WAPE and MASE where defined; include complementary metrics with caveats.
- [ ] Save residual and forecast plots.
- [ ] Distinguish historical observations from forecasts in every figure.
- [ ] Do not interpret forecasts as causal explanations.
