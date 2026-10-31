"""Evaluate saved observed/forecast pairs from a CSV file."""
import argparse
from pathlib import Path
import pandas as pd
from .metrics import calculate_metrics

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--actual-column", default="actual")
    parser.add_argument("--prediction-column", default="prediction")
    parser.add_argument("--year-column", default="year")
    args = parser.parse_args()

    frame = pd.read_csv(args.input)
    required = [args.actual_column, args.prediction_column]
    missing = [c for c in required if c not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    frame = frame.dropna(subset=required)
    train = None
    if "train_actual" in frame.columns:
        train = frame["train_actual"].dropna().to_numpy()
    metrics = calculate_metrics(
        frame[args.actual_column].to_numpy(),
        frame[args.prediction_column].to_numpy(),
        y_train=train
    )
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([metrics]).to_csv(output, index=False)
    print(pd.Series(metrics).to_string())
    print(f"\nSaved: {output}")

if __name__ == "__main__":
    main()
