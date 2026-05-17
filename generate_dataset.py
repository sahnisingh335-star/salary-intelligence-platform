from faker import Faker
import pandas as pd
import random

fake = Faker()

departments = [
    "Engineering",
    "HR",
    "Finance",
    "Sales",
    "Marketing"
]

cities = [
    "Mumbai",
    "Delhi",
    "Bhopal",
    "Pune",
    "Bangalore"
]

data = []

for i in range(600):

    row = {
        "employee_id": f"EMP{i+1}",
        "name": fake.name(),
        "age": random.randint(21, 50),
        "gender": random.choice(["Male", "Female"]),
        "department": random.choice(departments),
        "city": random.choice(cities),
        "experience_years": random.randint(1, 15),
        "tenure_years": random.randint(1, 10),
        "salary": random.randint(300000, 1500000),
        "performance_rating": random.randint(1, 5)
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_csv(
    "data/raw/employees.csv",
    index=False
)

print("Dataset generated successfully")