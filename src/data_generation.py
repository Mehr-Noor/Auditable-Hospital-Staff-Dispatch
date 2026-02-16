import pandas as pd
import numpy as np

np.random.seed(42)

N = 1000

data = pd.DataFrame({
    "required_staff": np.random.randint(5, 20, N),
    "available_staff": np.random.randint(3, 18, N),
    "avg_patient_load": np.random.randint(10, 40, N),
    "historical_shortage_rate": np.random.uniform(0, 0.6, N),
    "region_staff_pool": np.random.randint(20, 100, N),
})

data["staff_gap"] = data["required_staff"] - data["available_staff"]
data["shortage_risk"] = (
    (data["staff_gap"] > 2).astype(int)
)

data.to_csv("data/hospital_staffing.csv", index=False)
print("Synthetic dataset generated.")
