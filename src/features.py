import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["staff_gap"] = df["required_staff"] - df["available_staff"]
    df["load_per_staff"] = df["avg_patient_load"] / (df["available_staff"] + 1)

    return df[
        [
            "required_staff",
            "available_staff",
            "avg_patient_load",
            "historical_shortage_rate",
            "region_staff_pool",
            "staff_gap",
            "load_per_staff",
        ]
    ]
