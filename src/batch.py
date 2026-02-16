import pandas as pd
from src.scoring import score, risk_bucket
from src.decision import dispatch_decision

df = pd.read_csv("data/hospital_staffing.csv")

results = []

for _, row in df.iterrows():
    s = score(row.to_dict())
    risk = risk_bucket(s)
    decision = dispatch_decision(risk)

    results.append({
        "risk_score": s,
        "risk_level": risk,
        **decision
    })

pd.DataFrame(results).to_csv("data/batch_results.csv", index=False)
print("Batch inference completed.")
