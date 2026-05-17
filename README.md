# Salary Intelligence Platform

## Features

- Data pipeline
- Data cleaning
- KPI engine
- Salary prediction model
- FastAPI backend
- Streamlit dashboard
- Insights engine
- Automation scheduler

## Setup

pip install -r requirements.txt

## Generate Dataset

python scripts/generate_dataset.py

## Run Pipeline

python pipeline/run_pipeline.py

## Generate KPIs

python pipeline/compute_kpis.py

## Train Model

python models/train_model.py

## Run API

uvicorn api.main:app --reload

## Run Dashboard

streamlit run dashboard/app.py

## Run Insights

python pipeline/insights.py

## Run Scheduler

python scripts/scheduler.py