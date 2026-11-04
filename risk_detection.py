import pandas as pd

data = {
    "soil_moisture": [15, 45, 20, 60, 10],
    "temperature": [38, 25, 35, 22, 40],
    "rainfall_mm": [0, 12, 2, 20, 0]
}

df = pd.DataFrame(data)

def detect_risk(row):
    if row["soil_moisture"] < 20 and row["temperature"]R > 30:
        return "High Risk"
    elif row["soil_moisture"] < 25:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Risk"] = df.apply(detect_risk, axis=1)

print(df)
