import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/cleaned/cleaned_employees.csv"
)

st.title("Salary Intelligence Dashboard")

st.subheader("Employee Dataset")
st.write(df.head())

avg_salary = df["salary"].mean()

st.metric(
    "Average Salary",
    f"₹ {avg_salary:,.0f}"
)

st.subheader("Department Wise Salary")

dept_salary = (
    df.groupby("department")["salary"]
    .mean()
)

st.bar_chart(dept_salary)

st.subheader("Salary Distribution")

fig, ax = plt.subplots()

ax.hist(df["salary"], bins=20)

st.pyplot(fig)

st.subheader("Filter By Department")

department = st.selectbox(
    "Select Department",
    df["department"].unique()
)

filtered_df = df[
    df["department"] == department
]

st.write(filtered_df)