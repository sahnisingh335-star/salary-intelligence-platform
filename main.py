import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv(
    "data/cleaned/cleaned_employees.csv"
)

st.title("Salary Intelligence Dashboard")

# show dataset
st.subheader("Employee Dataset")
st.write(df.head())

# average salary
avg_salary = df["salary"].mean()

st.metric(
    "Average Salary",
    f"₹ {avg_salary:,.0f}"
)

# department salary
st.subheader("Department Wise Salary")

dept_salary = (
    df.groupby("department")["salary"]
    .mean()
)

st.bar_chart(dept_salary)

# salary distribution
st.subheader("Salary Distribution")

fig, ax = plt.subplots()

ax.hist(df["salary"], bins=20)

st.pyplot(fig)

# filters
st.subheader("Filter By Department")

department = st.selectbox(
    "Select Department",
    df["department"].unique()
)

filtered_df = df[
    df["department"] == department
]

st.write(filtered_df)