import pandas as pd
import json

df = pd.read_csv(
    "data/cleaned/cleaned_employees.csv"
)

insights = []

# highest salary department
highest_dept = (
    df.groupby("department")["salary"]
    .mean()
    .idxmax()
)

insights.append(
    f"{highest_dept} department has highest average salary"
)

# gender pay gap
male_avg = (
    df[df["gender"] == "Male"]["salary"]
    .mean()
)

female_avg = (
    df[df["gender"] == "Female"]["salary"]
    .mean()
)

if male_avg > female_avg:
    insights.append(
        "Male employees earn more on average"
    )
else:
    insights.append(
        "Female employees earn more on average"
    )

# high-risk employees
high_risk = df[
    (df["performance_rating"] <= 2) &
    (df["tenure_years"] > 5)
]

insights.append(
    f"{len(high_risk)} employees are high attrition risk"
)

# performance mismatch
mismatch = df[
    (df["performance_rating"] >= 4) &
    (df["salary"] < df["salary"].mean())
]

insights.append(
    f"{len(mismatch)} high performers are underpaid"
)

# highest paid city
highest_city = (
    df.groupby("city")["salary"]
    .mean()
    .idxmax()
)

insights.append(
    f"{highest_city} has highest average salary"
)

with open(
    "output/insights.json",
    "w"
) as f:

    json.dump(
        insights,
        f,
        indent=4
    )

print("Insights generated successfully")
