# Task 6 – Data Science Business Insights Dashboard

## 1. Project Overview

This project is an end-to-end Data Science project based on the Netflix titles dataset.

The main objective of this task was to analyze Netflix's content catalog, identify useful business insights, study content trends, evaluate predictive approaches, and present the findings through an interactive Streamlit dashboard.

The project combines data analysis, visualization, predictive analytics, and business-oriented recommendations in a single workflow.

---

## 2. Objectives

The main objectives of this project were:

* Perform data analysis on the Netflix dataset.
* Understand the distribution of Movies and TV Shows.
* Analyze genres, countries, ratings, and content trends.
* Study Netflix content growth over time.
* Develop predictive models for content-growth analysis.
* Build an interactive business intelligence dashboard.
* Generate meaningful business insights and recommendations.
* Present the complete analysis in a professional format.

---

## 3. Dataset

The project uses a cleaned Netflix titles dataset.

The dataset contains information related to Netflix movies and TV shows, including:

* Title
* Content Type
* Country
* Release Year
* Rating
* Genre
* Duration
* Date Added
* Other derived fields used for analysis

The cleaned dataset is stored in:

```text
Task_6_Business_Insights/data/cleaned_dataset.csv
```

The dataset was prepared before being used in the dashboard so that the analysis could be performed on structured and consistent data.

---

## 4. Data Preparation

The cleaned dataset was used as the primary input for the Task 6 analysis.

Additional fields were used to support the dashboard and trend analysis, including:

* Added Year
* Added Month
* Added Day
* Duration Value
* Duration Type
* Primary Genre

These fields make it easier to perform time-based analysis and categorize Netflix content.

---

## 5. Exploratory Data Analysis

The analysis focused on several important areas of the Netflix catalog.

### Content Type

The dataset was analyzed to compare Movies and TV Shows.

The dashboard displays:

* Total number of titles
* Number of Movies
* Number of TV Shows
* Percentage distribution of both content types

This provides a quick overview of the overall content mix.

### Genre Analysis

The most represented primary genres were identified using frequency analysis.

The dashboard displays the top genres and their number of titles, helping understand which types of content appear most frequently in the dataset.

### Country Analysis

The dataset was also analyzed based on country representation.

The dashboard displays the most frequently represented countries and their associated number of titles.

### Rating Analysis

Content ratings were analyzed to identify the most common rating categories.

This provides an overview of the type of audience classification most frequently represented in the dataset.

### Content Growth

Year-wise content analysis was performed to understand how the number of titles changed over time.

A time-series visualization was created to show the number of titles added across different years.

### Movies vs TV Shows Trend

The project also compares Movies and TV Shows over time.

This makes it possible to observe how the content mix changed across different periods.

---

## 6. Business Insights

The analysis produced several useful observations from the dataset.

### Content Mix

Movies represent a larger portion of the Netflix catalog than TV Shows in the analyzed dataset.

This indicates that the catalog has historically contained a significant amount of movie content.

### Genre Distribution

The dashboard identifies the most represented primary genre based on the available records.

This helps understand the major content categories present in the dataset.

### Geographic Distribution

The country analysis shows which countries have the highest representation in the dataset.

This provides a basic view of the geographic distribution of Netflix content.

### Rating Distribution

The rating analysis identifies the most frequently occurring content ratings.

This can help understand the audience classifications represented in the catalog.

### Content Growth

The year-wise analysis shows changes in the number of titles added over time.

The trend visualization makes it easier to identify periods of higher or lower content additions.

---

## 7. Predictive Analytics

Predictive analytics was included as part of the Task 6 workflow to analyze historical content-growth patterns.

The project evaluated multiple approaches:

### Linear Regression

Linear Regression was used as a baseline trend model.

It provides a simple way to understand the relationship between time and the number of titles added.

### Random Forest

Random Forest regression was considered to capture non-linear relationships in the historical data.

It provides an alternative approach to the simple linear baseline.

### Holt and Polynomial Approaches

Additional trend-based approaches were explored for forecasting and understanding historical content-growth behavior.

These models were used to compare different ways of representing the underlying trend.

The predictive section is included in the dashboard to present the machine learning component of the project alongside the descriptive analytics.

---

## 8. Interactive Dashboard

A Streamlit dashboard was developed to present the analysis in an interactive format.

The dashboard provides:

* Netflix catalog overview
* KPI cards
* Content type analysis
* Genre analysis
* Country analysis
* Rating distribution
* Content growth trends
* Movies vs TV Shows trend
* Business insights
* Predictive analytics section
* Dataset explorer
* Interactive filters

Users can filter the dashboard using:

* Content Type
* Primary Genre
* Rating

The dashboard automatically updates the displayed dataset view based on the selected filters.

---

## 9. Dashboard Technologies

The dashboard was developed using:

* Python
* Pandas
* Streamlit
* Plotly
* Plotly Express
* Scikit-learn based predictive approaches
* HTML/CSS styling inside Streamlit

Plotly was used for interactive charts and Streamlit was used to create the dashboard interface.

---

## 10. Business Recommendations

Based on the analysis, the following business-oriented recommendations can be considered:

1. **Monitor content mix**

   Netflix content can be continuously monitored by type to understand the balance between Movies and TV Shows.

2. **Track genre demand**

   Genre-level analysis can be used to identify heavily represented categories and compare them with future content acquisition or production plans.

3. **Analyze geographic opportunities**

   Country-level content data can help identify regions with strong content representation and areas where additional localized content could be explored.

4. **Use rating trends for audience analysis**

   Rating distributions can be monitored to understand the type of audience categories represented in the catalog.

5. **Monitor content growth**

   Year-wise content trends can be tracked regularly to identify changes in the pace of catalog expansion.

6. **Combine analytics with forecasting**

   Historical trends and predictive models can be used together to support future content planning and capacity decisions.

---

## 11. Project Structure

```text
Task_6_Business_Insights/
│
├── Task_6_Business_Insights.ipynb
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── cleaned_dataset.csv
│
├── report/
│   └── Task_6_Report.md
│
└── screenshots/
```

---

## 12. Key Skills Demonstrated

This project demonstrates the following Data Science skills:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Data Visualization
* Time-Series Trend Analysis
* Predictive Analytics
* Machine Learning
* Interactive Dashboard Development
* Business Insight Generation
* Data Storytelling

---

## 13. Conclusion

This Task 6 project combines the complete Data Science workflow into one practical business-oriented application.

The Netflix dataset was analyzed from multiple perspectives including content type, genre, country, ratings, and time-based trends. Predictive approaches were also explored to extend the analysis beyond descriptive statistics.

The final Streamlit dashboard brings these findings together in an interactive format, allowing users to explore the dataset through filters, charts, KPIs, business insights, and predictive analytics.

Overall, the project demonstrates how raw data can be transformed into visual insights and business-focused information through a complete Data Science workflow.
