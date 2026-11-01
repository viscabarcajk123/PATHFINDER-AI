"""Generates the synthetic Pathfinder AI datasets (one CSV per stream: 14 questions -> 10 field scores).
Scores come from a transparent weighted rubric (see streams.py) + small random noise."""
from pathlib import Path
import numpy as np
import pandas as pd
from streams import STREAMS, question_columns, target_columns, primary_question

ROOT = Path(__file__).resolve().parent
N_ROWS = 3000
SEED = 42

def generate(stream, n=N_ROWS, seed=SEED):
    Q, T = question_columns(stream), target_columns(stream)
    rubric = STREAMS[stream]["rubric"]
    primary = {t: primary_question(stream, t) for t in T}
    rng = np.random.default_rng(seed)
    levels = np.array([1, 2, 3, 4, 5])
    p_normal = np.array([0.24, 0.24, 0.24, 0.16, 0.12])   # general answer pattern
    p_liked = np.array([0.03, 0.07, 0.20, 0.35, 0.35])    # questions a student is "into"
    rows = []
    for _ in range(n):
        if rng.random() < 0.65:   # student with 1-2 genuine interest areas
            k = rng.choice([1, 2], p=[0.6, 0.4])
            liked = {primary[t] for t in rng.choice(T, size=k, replace=False)}
        else:                      # no clear interest
            liked = set()
        rows.append([rng.choice(levels, p=p_liked if q in liked else p_normal) for q in Q])
    df = pd.DataFrame(rows, columns=Q)
    centred = df - 3
    for t, weights in rubric.items():
        score = 60 + sum(w * centred[q] for q, w in weights.items()) + rng.normal(0, 2.5, n)
        df[t] = np.clip(score, 0, 100).round(1)
    df.insert(0, "student_id", np.arange(1, n + 1))
    return df

if __name__ == "__main__":
    (ROOT / "datasets").mkdir(exist_ok=True)
    for stream in STREAMS:
        out = ROOT / "datasets" / f"{STREAMS[stream]['slug']}_data.csv"
        data = generate(stream)
        data.to_csv(out, index=False)
        print(f"{stream}: saved {len(data)} rows x {data.shape[1]} columns to {out}")
