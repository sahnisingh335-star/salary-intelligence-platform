import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# load cleaned data
df = pd.read_csv(
    "data/cleaned/cleaned_employees.csv"
)

# features
X = df[
    [
        "experience_years",
        "performance_rating",
        "department",
        "tenure_years"
    ]
]

# target
y = df["salary"]

# preprocessing
preprocessor = ColumnTransformer(
    [
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            ["department"]
        )
    ],
    remainder="passthrough"
)

# model pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor())
])

# train model
model.fit(X, y)

# save model
joblib.dump(
    model,
    "models/salary_model.pkl"
)

print("Model trained successfully")