# Data dictionary

## Input format for evaluation

| Column | Type | Meaning |
|---|---|---|
| `year` | integer | Annual observation year |
| `actual` | numeric | Observed value in the test period |
| `prediction` | numeric | Forecast generated without using the test target |

One file should represent one indicator/knowledge-area/model/horizon combination, or include explicit identifier columns and group before evaluation.

## Suggested metadata

- `indicator`: publications, research_projects, or academic_supervisions
- `knowledge_area`: one of the eight areas listed in the README
- `model`: LSTM, polynomial_regression, or baseline name
- `forecast_origin`: final year available at prediction time
- `horizon`: number of steps ahead
- `seed`: random seed, when applicable
- `split`: train/validation/test designation

Do not mix multiple series in a single metric calculation unless the aggregation method is explicitly defined.
