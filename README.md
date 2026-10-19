# Salary Intelligence Platform 📊

## Project Overview
The Salary Intelligence Platform is a data analytics project designed to analyze employee salary data, identify salary trends, compare department-wise and city-wise salaries, and generate useful business insights.

The project uses Python, Pandas, SQL, and machine learning to clean employee data, calculate key performance indicators (KPIs), and estimate salaries.

## Objectives
- Analyze employee salary distribution.
- Compare average salaries across departments.
- Identify city-wise salary trends.
- Clean and preprocess employee datasets.
- Calculate important salary-related KPIs.
- Build a machine learning model for salary prediction.
- Generate actionable insights from employee data.

## Technologies Used
- **Python** – Data processing and analysis
- **Pandas** – Data cleaning and manipulation
- **SQL** – Data querying and analysis
- **Machine Learning (Scikit-learn)** – Salary prediction
- **CSV and JSON** – Data storage and KPI/insight outputs
- **Git and GitHub** – Version control and project hosting

## Project Features
- Employee dataset generation
- Data cleaning and preprocessing
- Salary KPI computation
- Department-wise salary analysis
- City-wise salary analysis
- Salary prediction model
- Automated insight generation
- Data pipeline execution

## Project Structure
```text
salary-intelligence-platform/
├── README.md
├── app.py
├── main.py
├── clean.py
├── compute_kpis.py
├── generate_dataset.py
├── insights.py
├── run_pipeline.py
├── train_model.py
├── scheduler.py
├── employees.csv
├── cleaned_employees.csv
├── kpis.json
├── insights.json
└── salary_model.pkl
```

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/sahnisingh335-star/salary-intelligence-platform.git
cd salary-intelligence-platform
```

### 2. Install Dependencies
```bash
pip install pandas numpy scikit-learn streamlit
```

### 3. Run the Data Pipeline
```bash
python run_pipeline.py
```

### 4. Launch the Application
```bash
streamlit run app.py
```

*Note: Install any additional dependencies required by your Python files. The commands above assume that `app.py` is a Streamlit application and that `run_pipeline.py` runs the complete pipeline.*

## Business Insights
This project helps users understand:
- Average employee salary.
- Salary differences between departments.
- City-wise salary distribution.
- Patterns in employee compensation.
- Potential salary estimates from a trained model.

## Future Improvements
- Add interactive dashboards.
- Integrate a SQL database.
- Improve salary prediction accuracy.
- Add filters for departments, cities, and experience levels.
- Deploy the application online.

## Author
**Sahni Singh**

Aspiring Data Analyst | Python | SQL | Power BI | Excel

## License
This project is intended for learning and portfolio purposes.

