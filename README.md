# Data Analysis Assessment
## Overview
This project presents an **Exploratory Data Analysis (EDA)** of a sales dataset to evaluate performance, identify trends, and assess the relationship between priority levels and sales value. The analysis was conducted using Python with a focus on data preprocessing, visualisation, and basic statistical insights.

---

## Objectives
* Analyse **sales performance by salesperson**
* Examine **sales trends over time**
* Investigate the relationship between **priority levels and sales value**
* Apply **data preprocessing techniques** to improve data quality

---

## Tools & Technologies
* Python
* pandas
* matplotlib
* seaborn

---

## Dataset
The dataset contains transactional sales data including:
* Salesperson
* Sales value
* Priority level
* Date

> Note: The dataset file is not included in this repository.

---

## Methodology
### 1. Data Understanding
* Loaded dataset using pandas
* Inspected structure, columns, and data types
* Generated summary statistics

### 2. Data Preprocessing
* Handled missing values (removed incomplete rows)
* Converted date column to datetime format
* Standardised categorical values
* Removed inconsistent entries
* Encoded priority levels numerically
* Detected and removed outliers using the IQR method

### 3. Exploratory Data Analysis (EDA)
* **Bar Chart:** Sales per salesperson
* **Line Plot:** Total sales over time
* **Scatter Plot:** Priority vs sales value

### 4. Correlation Analysis
* Calculated Pearson correlation between priority and sales value

---

## Key Findings
* Sales performance is **unevenly distributed** among salespeople
* Sales show **fluctuations over time**, indicating variability
* **Weak correlation** between priority and sales value

---

## Visualisations
The project includes:
* Sales distribution by salesperson
* Sales trends over time
* Relationship between priority and sales

---

## How to Run the Code

1. Install required libraries:
```bash
pip install pandas matplotlib seaborn openpyxl
```

2. Place the dataset file:
```
Sales Data PDA 4052.xlsx
```

3. Run the script:
```bash
python main.py
```

---

## Code Repository (for Report)

The full implementation is available at:
👉 [https://github.com/axitpatel1310/Data-Analysis-Assessment](https://github.com/axitpatel1310/Data-Analysis-Assessment)

---

## Academic Context
This project was completed as part of a **Data Analytics / Data Science assessment**, focusing on applying EDA techniques to real-world business data.

---

## Limitations
* Small dataset size may limit generalisation
* Correlation does not imply causation
* Priority encoding assumes linear relationship

---

## Future Improvements
* Apply predictive modelling
* Use larger datasets
* Perform advanced statistical analysis
* Improve visualisation depth

**Author**
Axit Patel


Just say: *“upgrade README to pro level”* 🚀
