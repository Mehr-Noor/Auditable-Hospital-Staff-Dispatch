import joblib
import pandas as pd
from src.features import build_features

logreg = joblib.load("models/logreg.pkl")
xgb_model = joblib.load("models/xgb.pkl")

def score(input_data: dict) -> float:
    df = pd.DataFrame([input_data])
    X = build_features(df)

    p1 = logreg.predict_proba(X)[:, 1][0]
    p2 = xgb_model.predict_proba(X)[:, 1][0]

    return 0.5 * p1 + 0.5 * p2

def risk_bucket(score: float) -> str:
    if score < 0.3:
        return "LOW"
    elif score < 0.6:
        return "MEDIUM"
    return "HIGH"
