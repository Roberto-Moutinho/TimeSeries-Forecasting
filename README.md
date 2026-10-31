# Scientometric Time-Series Forecasting

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Research](https://img.shields.io/badge/Research-Scientometrics-6f42c1)]()

**Time-series modeling and forecasting of Brazilian scientific production using recurrent neural networks and nonlinear regression.**

This repository accompanies the undergraduate research project *Análise Cientométrica baseada em Séries Temporais: Modelagem e Previsões com Redes Neurais e Regressões Não Lineares a partir de Dados Acadêmicos Brasileiros*, developed by **Roberto Dalcin Moutinho** under the supervision of **Prof. Dr. Jesús P. Mena-Chalco**, at the Federal University of ABC (UFABC), Brazil.

> The repository separates results documented in the final research report from additional evaluation procedures proposed to make future computational experiments more reproducible. Metrics listed as recommended below must not be interpreted as results already obtained in the report.

## Overview

The project investigates the temporal evolution of Brazilian scientific production through three scientometric indicators:

- **Journal publications**;
- **Research projects initiated**;
- **Academic supervisions**.

The indicators are analyzed across the eight major CAPES knowledge areas:

1. Agricultural Sciences
2. Biological Sciences
3. Engineering
4. Exact and Earth Sciences
5. Linguistics, Literature and Arts
6. Health Sciences
7. Humanities
8. Applied Social Sciences

The research combines historical time-series analysis, Long Short-Term Memory (LSTM) recurrent neural networks, and polynomial nonlinear regression. The objective is to characterize historical patterns and produce forecasts that may support the discussion of scientific-development trends in Brazil.

## Research questions

1. How have publications, research projects, and academic supervisions evolved across knowledge areas?
2. Which areas exhibit sustained growth, stabilization, or decline?
3. How do LSTM forecasts compare visually and quantitatively with polynomial regression?
4. What are the limitations of extrapolating historical scientometric trends?

## Methodological scope

The final report describes the following workflow:

1. Data collection and preprocessing using academic information associated with the Lattes Platform and OpenAlex, together with the scientometrics research group's database.
2. Construction of annual time series for the three indicators.
3. LSTM-based time-series forecasting.
4. Polynomial nonlinear regression for comparison.
5. Interpretation of trends across the eight knowledge areas.

For journal publications, ISSN identifiers are used to associate journals with knowledge areas. For research projects and academic supervisions, researcher Lattes identifiers are used in the extraction procedure.

## Data and time coverage

The report discusses historical series beginning in 1990 and extending through the available historical observations. The report's broader project description refers to historical data through 2024 and forecast scenarios extending to 2035. The exact usable interval can differ by indicator and knowledge area and must be read from the actual source files.

**Important:** The underlying Lattes/OpenAlex-derived datasets are not included in this repository by default. Do not commit restricted, personal, confidential, or redistributed data without confirming the applicable terms and permissions. Provide your own data files in the documented format.

## Models

### LSTM

The report uses a recurrent neural network with Long Short-Term Memory units to model sequential dependencies and forecast future observations.

### Polynomial nonlinear regression

Polynomial regression curves are fitted to the historical observations and used as a complementary trend model. The report includes equations for the three indicators in its appendices.

The polynomial degree, fitting interval, and extrapolation behavior should be explicitly recorded in the experiment configuration. High-degree polynomial extrapolation can be unstable outside the observed interval.

## Evaluation metrics

The final report presents plots, forecast trajectories, polynomial equations, and qualitative interpretations. It does **not** provide a complete, consistently tabulated set of out-of-sample forecast-error metrics for every indicator and knowledge area. Therefore, this repository includes an evaluation module for additional analyses; its outputs must be generated from actual observed and predicted values.

Recommended metrics:

| Metric | Interpretation | Notes |
|---|---|---|
| MAE | Mean Absolute Error | Error in the original target units |
| MSE | Mean Squared Error | Penalizes large errors more strongly |
| RMSE | Root Mean Squared Error | Same unit as the target |
| MAPE | Mean Absolute Percentage Error | Undefined/unstable when actual values are zero or near zero |
| sMAPE | Symmetric MAPE | Percentage-style measure; still requires care near zero |
| WAPE | Weighted Absolute Percentage Error | Aggregate absolute error relative to total observed magnitude |
| R² | Coefficient of determination | Can be negative on out-of-sample data |
| MASE | Mean Absolute Scaled Error | Requires a valid in-sample naïve scale |

For count-valued scientometric series, **MAE, RMSE, WAPE and MASE** are useful primary measures. Report MAPE only when its denominator is appropriate. Always compare against at least a naïve baseline (for example, last-observation-carried-forward) before claiming predictive skill.

### Evaluation protocol to adopt for new experiments

- Preserve chronological order; never randomly shuffle time-series observations.
- Define the training, validation, and test periods before model fitting.
- Fit scalers and transformations on training data only.
- Use rolling-origin evaluation or expanding-window evaluation when sufficient observations exist.
- Report each metric per series and an explicitly defined aggregate; do not average incompatible scales without justification.
- Record forecast horizon, data interval, random seed, software versions, and model hyperparameters.
- Include prediction plots and residual diagnostics.

These are **recommended reproducibility practices**, not claims that the original report used this exact protocol.

## Repository structure

```text
TimeSeries-Research/
├── README.md
├── LICENSE
├── CITATION.cff
├── .gitignore
├── requirements.txt
├── configs/
│   └── evaluation.example.json
├── data/
│   ├── raw/
│   │   └── README.md
│   ├── processed/
│   │   └── README.md
│   └── sample/
│       └── annual_series_example.csv
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   └── REPRODUCIBILITY.md
├── notebooks/
│   └── README.md
├── results/
│   ├── figures/
│   │   └── .gitkeep
│   └── tables/
│       └── .gitkeep
├── src/
│   └── scientometric_forecasting/
│       ├── __init__.py
│       ├── metrics.py
│       ├── baselines.py
│       └── evaluate.py
└── tests/
    └── test_metrics.py
```

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/TimeSeries-Research.git
cd TimeSeries-Research
```

### 2. Create an environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Prepare a dataset

Use the schema described in `docs/DATA_DICTIONARY.md`. A small synthetic example is provided in `data/sample/annual_series_example.csv`; it is only a demonstration and is not research data.

### 5. Evaluate predictions

```bash
python -m scientometric_forecasting.evaluate \
  --input data/sample/annual_series_example.csv \
  --output results/tables/example_metrics.csv
```

The evaluator expects columns `year`, `actual`, and `prediction`. Replace the synthetic example with genuine held-out predictions before interpreting the metrics.

## Main findings documented in the report

The report analyzes the three indicators across all eight knowledge areas and describes declines or changes in trajectories in several areas. It highlights the importance of interpreting these patterns in the context of broader structural, institutional, and funding conditions. The report specifically calls attention to the situation of Health Sciences.

The report also identifies limitations of LSTM models, including sensitivity to hyperparameter choices and challenges in capturing long-term and seasonal patterns. It suggests N-HiTS and N-BEATS as promising directions for future work, alongside multivariate analysis.

**No causal conclusion should be drawn from a univariate trend or forecast alone.** Forecasts are conditional projections based on historical patterns, not evidence that a particular policy or event caused the observed trajectory.

## Limitations

- Historical database coverage, classification rules, and metadata quality may affect counts.
- Journal classification based on ISSN and researcher identification based on Lattes IDs depend on the completeness and consistency of those identifiers.
- LSTM forecasts can be sensitive to architecture, hyperparameters, scaling, and the available history.
- Polynomial extrapolation may diverge rapidly outside the observed time interval.
- Forecast uncertainty and structural breaks should be considered when interpreting long-range projections.
- The report does not provide a complete benchmark table of standard forecast-error metrics for every series.

## Responsible use

Scientometric indicators are imperfect proxies for research activity and quality. Publication counts, project counts, and supervision counts should not be interpreted as direct measures of scientific merit. Comparisons across areas must account for differences in publication cultures, field size, database coverage, and time-to-publication.

## Citation

If this repository or its research description is useful, cite the underlying undergraduate research report. See `CITATION.cff` for a starting citation record. Update the repository URL and release metadata after publication.

## Author

**Roberto Dalcin Moutinho**  
Federal University of ABC (UFABC), Brazil  
Research area: Computer Science / Scientometrics / Time-Series Forecasting

## Acknowledgements

Research supervision: **Prof. Dr. Jesús P. Mena-Chalco**.

## License

The source code is distributed under the MIT License. This license does not grant rights to third-party datasets, Lattes records, OpenAlex-derived datasets, institutional databases, or report materials. Check their respective terms before redistribution.
