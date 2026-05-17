import pandas as pd

def clean_data():

    df = pd.read_csv(
        "data/raw/employees.csv"
    )

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # handle missing values
    df.fillna({
        "department": "Unknown",
        "city": "Unknown"
    }, inplace=True)

    # standardize text
    df["department"] = (
        df["department"]
        .str.title()
        .str.strip()
    )

    df["city"] = (
        df["city"]
        .str.title()
        .str.strip()
    )

    # salary outlier removal
    Q1 = df["salary"].quantile(0.25)
    Q3 = df["salary"].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[
        (df["salary"] >= lower) &
        (df["salary"] <= upper)
    ]

    # save cleaned data
    df.to_csv(
        "data/cleaned/cleaned_employees.csv",
        index=False
    )

    print("Data cleaned successfully")