import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import joblib

from src.features import build_features

df = pd.read_csv("data/hospital_staffing.csv")

X = build_features(df)
y = df["shortage_risk"]

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

xgb_model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    eval_metric="logloss",
)
xgb_model.fit(X_train, y_train)

logreg_auc = roc_auc_score(y_val, logreg.predict_proba(X_val)[:, 1])
xgb_auc = roc_auc_score(y_val, xgb_model.predict_proba(X_val)[:, 1])

print("LogReg AUC:", logreg_auc)
print("XGBoost AUC:", xgb_auc)

joblib.dump(logreg, "models/logreg.pkl")
joblib.dump(xgb_model, "models/xgb.pkl")
