# 🎬 Netflix Intelligence – Business Insights Dashboard

An end-to-end Data Science project created as part of the **Auspify Technologies Data Science Internship – Task 6**.

This project analyzes the Netflix titles dataset and combines **data analysis, interactive visualization, predictive analytics, and business insights** into a single Streamlit dashboard.

---

## 📌 Project Overview

The project focuses on understanding Netflix's content catalog and identifying useful patterns related to:

* Movies and TV Shows
* Genres
* Ratings
* Countries
* Content growth
* Historical trends
* Predictive content-growth analysis

The final output is an interactive dashboard called **Netflix Intelligence**.

---

## 🎯 Objectives

The main objectives of this project are:

* Perform complete data analysis on the Netflix dataset
* Explore important content patterns
* Analyze genres, countries, ratings, and content types
* Study content growth over time
* Develop predictive models for content-growth analysis
* Create interactive visualizations
* Generate business insights and recommendations
* Present the findings through a professional dashboard and report

---

## 📊 Dataset

The project uses a cleaned Netflix titles dataset.

The final cleaned dataset contains **8,790 records**.

| Metric             |     Value |
| ------------------ | --------: |
| Total Titles       |     8,790 |
| Movies             |     6,126 |
| TV Shows           |     2,664 |
| Release Year Range | 1925–2021 |

### Important Columns

The dataset contains fields such as:

* `title`
* `type`
* `director`
* `cast`
* `country`
* `date_added`
* `release_year`
* `rating`
* `duration`
* `listed_in`
* `description`

Additional features used for analysis include:

* `added_year`
* `added_month`
* `added_day`
* `duration_value`
* `duration_type`
* `primary_genre`

---

## 🔍 Data Analysis

The project performs analysis across multiple dimensions.

### Content Type

Movies and TV Shows are compared to understand the overall content mix.

### Genre Analysis

The most frequently represented primary genres are identified and visualized.

### Country Analysis

Country-level analysis is used to understand the geographic distribution of content.

### Rating Analysis

Content ratings are analyzed to understand the distribution of audience categories.

### Content Growth

Year-wise analysis is used to study changes in the Netflix catalog over time.

### Movies vs TV Shows Trend

The project compares the historical addition of Movies and TV Shows across different years.

---

## 📈 Dashboard Features

The Streamlit dashboard contains the following sections:

### Executive Overview

Displays key metrics including:

* Total Titles
* Movies
* TV Shows
* Top Genre
* Top Country
* Common Rating
* Release Range
* Filtered Records

### Content Mix

Interactive visualizations showing the distribution of Movies and TV Shows.

### Content Landscape

Displays the most represented:

* Genres
* Countries

### Rating Distribution

Shows the distribution of Netflix content ratings.

### Content Growth

Displays year-wise content addition trends.

### Movies vs TV Shows Over Time

Compares the historical content mix by year.

### Business Insights

Highlights observations derived from the dataset.

### Predictive Analytics

Presents the predictive approaches used for content-growth analysis.

### Dataset Explorer

Allows users to browse filtered Netflix records directly from the dashboard.

---

## 🤖 Predictive Analytics

Predictive analytics was included to extend the project beyond descriptive analysis.

The project explores different approaches for analyzing historical Netflix content growth, including:

### Linear Regression

Used as a baseline model for understanding the relationship between time and content additions.

### Random Forest

Used to explore non-linear patterns in historical content-growth data.

### Holt + Polynomial Approaches

Additional trend-based approaches were explored to analyze historical growth patterns.

The predictive analysis is presented as part of the overall business analytics workflow.

---

## 💡 Business Insights

The analysis provides several observations from the available Netflix dataset:

* Movies represent a larger portion of the catalog than TV Shows.
* Some genres have considerably more titles than others.
* Content representation varies across countries.
* Rating categories have different levels of representation.
* The number of content additions changes across different years.
* The historical trend can be used to study Netflix catalog growth.

These findings are presented interactively through the dashboard.

---

## 💼 Business Recommendations

Based on the analysis, the following areas can be considered for further business analysis:

1. Monitor the balance between Movies and TV Shows.
2. Track genre-level content distribution over time.
3. Study regional content representation to identify potential opportunities.
4. Monitor rating distribution for audience-focused analysis.
5. Use historical content-growth trends for planning and forecasting.
6. Combine catalog data with additional business metrics such as viewing hours, engagement, subscriptions, and revenue for deeper analysis.

These recommendations are analytical observations based on the available dataset and are not official Netflix business decisions.

---

## 🛠️ Tech Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Statsmodels

### Visualization

* Plotly
* Matplotlib

### Dashboard

* Streamlit

### Development

* Jupyter Notebook
* VS Code

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
Auspify_Data_Science_Internship/
│
├── Task_6_Business_Insights/
│   │
│   ├── Task_6_Business_Insights.ipynb
│   │
│   ├── dashboard/
│   │   └── app.py
│   │
│   ├── data/
│   │   └── cleaned_dataset.csv
│   │
│   ├── report/
│   │   └── Task_6_Report.md
│   │
│   └── screenshots/
│       ├── 01_dashboard_overview.png
│       ├── 02_content_mix.png
│       ├── 03_content_landscape.png
│       ├── 04_content_trends.png
│       ├── 05_business_insights.png
│       └── 06_dataset_explorer.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/MandeepChauhan9756/auspify-data-science-internship.git
```

### 2. Move into the project directory

```bash
cd Auspify_Data_Science_Internship
```

### 3. Create and activate the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Task 6 dashboard

```bash
streamlit run Task_6_Business_Insights/dashboard/app.py
```

The dashboard will open in the browser.

---

## 📸 Dashboard Screenshots

Screenshots of the completed dashboard are available in:

```text
Task_6_Business_Insights/screenshots/
```

They cover:

* Dashboard overview
* Content mix
* Content landscape
* Content trends
* Business insights
* Dataset explorer

---

## 📄 Project Report

The detailed Task 6 report is available at:

```text
Task_6_Business_Insights/report/Task_6_Report.md
```

The report covers:

* Project overview
* Objectives
* Dataset
* Data preparation
* Exploratory analysis
* Predictive analytics
* Dashboard
* Business insights
* Business recommendations
* Conclusion

---

## 🎓 Internship

**Auspify Technologies**
**Data Science Internship**
**Task 6 – Data Science Business Insights Dashboard**

### Project Title

**Netflix Intelligence – Business Insights Dashboard**

---

## 👤 Author

**Mandeep Chauhan**

Data Science & Python Backend Developer

---

## 📌 Note

This project was created for learning and internship purposes using the Netflix titles dataset.

The dashboard findings, predictive analysis, forecasts, and business recommendations are based on the available dataset and should be considered analytical observations rather than official Netflix business decisions.
