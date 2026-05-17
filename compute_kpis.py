import pandas as pd
import json

df = pd.read_csv(
    "data/cleaned/cleaned_employees.csv"
)

kpis = {

    "average_salary":
        float(df["salary"].mean()),

    "high_performers":
        int(
            len(
                df[df["performance_rating"] >= 4]
            )
        ),

    "department_salary":
        df.groupby("department")["salary"]
        .mean()
        .to_dict()
}

with open(
    "output/kpis.json",
    "w"
) as f:

    json.dump(
        kpis,
        f,
        indent=4
    )

print("KPIs generated successfully")