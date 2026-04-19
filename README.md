# Poll Results Visualizer 📊

An industry-grade, end-to-end Data Science project designed to analyze, process, and visualize survey/poll data. This project transforms raw feedback into actionable business insights through a modular Python pipeline and an interactive Streamlit dashboard.

---

## 🌟 Overview

Survey data is often messy and unstructured. This project provides a robust solution for businesses and researchers to:
1. **Ingest** raw poll results (CSV/Synthetic).
2. **Clean** and preprocess data automatically.
3. **Analyze** demographics and sentiment.
4. **Visualize** trends using static and interactive dashboards.

### 🏢 Real-World Applications
- **Elections**: Analyzing voter sentiment across regions and age groups.
- **Business**: Measuring Product Satisfaction (CSAT) and Brand Loyalty (NPS).
- **HR**: Monitoring employee engagement and workplace sentiment.
- **Education**: Gathering and analyzing student feedback on courses.

---

## 🛠️ Tech Stack

| Level | Tools & Technologies |
| :--- | :--- |
| **Beginner** | Python, Excel (CSV), Matplotlib |
| **Intermediate** | **Pandas, Seaborn, Streamlit, Plotly (Selected)** |
| **Advanced** | PySpark, SQL, Tableau API, AWS S3 |

---

## 📂 Project Structure

```text
Poll Results Visualizer/
├── data/                   # Raw and cleaned survey datasets
├── scripts/                # Modular Python scripts
│   ├── data_generator.py   # Synthetic data engine
│   ├── data_processor.py   # Cleaning & feature engineering
│   └── visualizer.py       # Static chart generation engine
├── outputs/                # Analysis outputs
│   ├── charts/             # Saved PNG visualizations
│   └── reports/            # Data summary text reports
├── app.py                  # Streamlit Interactive Dashboard
├── requirements.txt        # Project dependencies
├── interview_prep.md       # 20+ Q&A for placements
└── README.md               # Project documentation
```

---

## 🚀 How to Run

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
```bash
# Clone the repository (if applicable)
# git clone "https://github.com/vtr054/Poll-Results-Visualizer.git"
# cd "Poll Results Visualizer"

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Execution Pipeline
Run the scripts in the following order:

```bash
# Step 1: Generate Synthetic Data
python scripts/data_generator.py

# Step 2: Clean and Process Data
python scripts/data_processor.py

# Step 3: Generate Static Visualizations
python scripts/visualizer.py

# Step 4: Launch Interactive Dashboard
streamlit run app.py
```

---

## 📊 Features & Key Insights

- **Automated Cleaning**: Handles missing values and outliers.
- **NPS Analysis**: Automatically classifies Promoters, Passives, and Detractors.
- **Sentiment Engine**: Extracts emotional tone from open-ended feedback.
- **Demographic Filtering**: Slicing data by Age, Gender, and Region.
- **Interactive Visuals**: Box plots for device satisfaction and Word Clouds for feedback.

---

## 🖼️ Screenshot Guide

For your GitHub repo, keep the following screenshots ready:
1. **Raw Data**: `data/raw_survey_data.csv` opened in Excel.
2. **Cleaned Data**: `data/cleaned_survey_data.csv` showing the new `Age_Group` and `Sentiment` columns.
3. **Charts**: Include `outputs/charts/nps_by_region.png` or `satisfaction_distribution.png`.
4. **Dashboard**: The Streamlit interface with active filters.

---

## 🔮 Future Improvements

- **NLP Integration**: Use HuggingFace Transformers for deep sentiment and thematic analysis.
- **Real-time Data**: Connect to Google Forms API or SurveyMonkey Webhooks.
- **Predictive Analytics**: Predict NPS based on demographic features.
- **Multi-tenant Support**: Allow users to upload their own CSV files directly via the dashboard.

---
