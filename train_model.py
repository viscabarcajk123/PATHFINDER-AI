from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score, precision_score, recall_score, f1_score, accuracy_score
from sklearn.model_selection import train_test_split
from streams import STREAMS, question_columns, target_columns, field_names

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

def train_stream(stream):
    slug = STREAMS[stream]["slug"]
    QUESTION_COLUMNS, TARGET_COLUMNS, FIELD_NAMES = question_columns(stream), target_columns(stream), field_names(stream)
    data = pd.read_csv(ROOT / "datasets" / f"{slug}_data.csv")
    X, y = data[QUESTION_COLUMNS], data[TARGET_COLUMNS]
    labels = y.to_numpy().argmax(axis=1)
    X_train, X_test, y_train, y_test, labels_train, labels_test = train_test_split(
        X, y, labels, test_size=0.20, random_state=42, stratify=labels
    )
    # Scores are built from weighted answers, so a linear model learns them best
    reg = Ridge(alpha=1.0)
    reg.fit(X_train, y_train)
    predicted_scores = np.clip(reg.predict(X_test), 0, 100)
    classifier = LogisticRegression(max_iter=3000, class_weight="balanced")
    classifier.fit(X_train, labels_train)
    predicted_labels = classifier.predict(X_test)
    per_field = []
    for i, name in enumerate(FIELD_NAMES):
        per_field.append({
            "field": name,
            "mae": round(float(mean_absolute_error(y_test.iloc[:, i], predicted_scores[:, i])), 3),
            "r2": round(float(r2_score(y_test.iloc[:, i], predicted_scores[:, i])), 3)
        })
    metrics = {
        "stream": stream,
        "dataset_rows": int(len(data)), "train_records": int(len(X_train)), "test_records": int(len(X_test)),
        "regression": {"mae": float(mean_absolute_error(y_test, predicted_scores)),
                       "r2": float(r2_score(y_test, predicted_scores, multioutput="uniform_average"))},
        "classification": {
            "accuracy": float(accuracy_score(labels_test, predicted_labels)),
            "precision_weighted": float(precision_score(labels_test, predicted_labels, average="weighted", zero_division=0)),
            "recall_weighted": float(recall_score(labels_test, predicted_labels, average="weighted", zero_division=0)),
            "f1_weighted": float(f1_score(labels_test, predicted_labels, average="weighted", zero_division=0))
        },
        "per_field": per_field,
        "note": "All targets are synthetic rubric-generated scores; metrics do not validate real-world career outcomes."
    }
    joblib.dump(reg, MODEL_DIR / f"{slug}_model.pkl")
    joblib.dump(classifier, MODEL_DIR / f"{slug}_classifier.pkl")
    (MODEL_DIR / f"{slug}_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(f"\nPATHFINDER AI - {stream.upper()} MODEL EVALUATION")
    print(f"Dataset: {len(data)} records | Train: {len(X_train)} | Test: {len(X_test)}")
    print(f"Regression MAE: {metrics['regression']['mae']:.3f} (lower is better)")
    print(f"Regression R²: {metrics['regression']['r2']:.3f} (closer to 1 is generally better)")
    print(f"Top-field accuracy: {metrics['classification']['accuracy']:.3f}")
    print(f"Weighted precision: {metrics['classification']['precision_weighted']:.3f}")
    print(f"Weighted recall: {metrics['classification']['recall_weighted']:.3f}")
    print(f"Weighted F1: {metrics['classification']['f1_weighted']:.3f}")

def main():
    for stream in STREAMS:
        train_stream(stream)
    print("\nSaved models and metrics for all streams under the models folder.")

if __name__ == "__main__":
    main()
