# Netflix Intelligence – Data Science Business Insights Dashboard

## 1. Project Overview

This project was created as part of the Auspify Technologies Data Science Internship – Task 6.

The main goal of this project was to build an end-to-end data science dashboard using the Netflix titles dataset. I worked on the data analysis, visualization, predictive modeling and business insights in one project.

The final result is an interactive Streamlit dashboard called **Netflix Intelligence**.

The dashboard allows users to explore Netflix content by type, genre and rating. It also shows content trends, model performance, future predictions and business recommendations.

---

## 2. Objective

The main objectives of this project were:

* Analyze the Netflix content dataset.
* Understand the distribution of Movies and TV Shows.
* Find the most common genres, ratings and countries.
* Analyze Netflix content growth over time.
* Build predictive models for content growth.
* Compare model performance.
* Create an interactive dashboard.
* Generate useful business insights and recommendations.

---

## 3. Dataset

The project uses the Netflix titles dataset.

The cleaned dataset contains **8,790 titles**.

The dataset includes information such as:

* Title
* Content Type
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Listed Genres
* Description

During the data preparation stage, missing values were handled and additional columns were created to make the analysis easier.

Some of the additional fields used in the project include:

* `added_year`
* `added_month`
* `added_day`
* `duration_value`
* `duration_type`
* `primary_genre`

---

## 4. Data Cleaning and Preparation

Before starting the analysis, I cleaned and prepared the dataset.

The main steps were:

1. Loaded the raw Netflix dataset.
2. Checked the dataset structure and data types.
3. Checked missing values.
4. Removed duplicate records.
5. Processed the `date_added` column.
6. Extracted year, month and day from the date.
7. Processed the duration information.
8. Created a primary genre column.
9. Checked the cleaned dataset again before using it for analysis.

After cleaning, the final dataset contained **8,790 records**.

---

## 5. Exploratory Data Analysis

I used exploratory data analysis to understand the Netflix content library.

The dashboard focuses on the following areas:

### Content Type

The dataset contains both Movies and TV Shows.

There are:

* **6,126 Movies**
* **2,664 TV Shows**

Movies make up the larger part of the dataset.

### Genre Analysis

The dashboard identifies the most frequently appearing primary genres and displays the top genres using interactive charts.

This helps in understanding what type of content is most commonly represented in the dataset.

### Country Analysis

Country information was analyzed to understand the geographical distribution of Netflix content.

The dashboard displays the countries with the highest number of titles.

### Rating Analysis

The rating distribution was also analyzed to understand which audience categories appear most frequently in the dataset.

### Time Analysis

Content trends were analyzed using the year in which titles were added to Netflix.

This makes it possible to see how the Netflix catalog changed over time.

---

## 6. Dashboard

The dashboard was developed using **Streamlit** and **Plotly**.

The dashboard includes interactive filters for:

* Content Type
* Primary Genre
* Rating

After applying filters, the charts and dataset explorer update according to the selected data.

The main dashboard sections are:

* Executive Overview
* Content Mix
* Content Landscape
* Rating Distribution
* Content Growth
* Movies vs TV Shows Trend
* Business Insights
* Predictive Analytics
* Business Recommendations
* Dataset Explorer

---

## 7. Machine Learning

For the predictive part of the project, I worked with yearly Netflix content counts.

The purpose was to understand historical content growth and estimate future content levels.

The models included:

### Linear Regression

Linear Regression was used as a simple baseline model.

It helps understand the overall relationship between time and the number of titles added.

### Random Forest

Random Forest Regression was used to capture more complex and non-linear patterns in the historical data.

The model was compared with the Linear Regression baseline.

---

## 8. Model Performance

The models were evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

The Random Forest model achieved:

* **R² Score: 0.791**
* **MAE: 301.87**
* **RMSE: 377.74**

These metrics are displayed directly in the Predictive Analytics section of the dashboard.

The model comparison helps show how different approaches perform on the same forecasting problem.

---

## 9. Forecasting

The project also includes future content forecasting.

The forecast section uses the historical content trend to estimate future Netflix content levels.

The forecast is presented visually so that the expected trend can be compared with the historical data.

The purpose of this section is not to predict Netflix's actual future catalog exactly, but to demonstrate how historical data can be used for a basic business forecasting workflow.

---

## 10. Business Insights

Some of the main observations from the analysis are:

### Movies have a larger share

Movies represent a much larger portion of the dataset compared with TV Shows.

This shows that the Netflix catalog in this dataset has a strong movie presence.

### Genre concentration

Some genres appear much more frequently than others.

This indicates that the content library is not evenly distributed across all genres.

### Geographic distribution

A relatively small number of countries account for a large share of the available content records.

This shows that content production and availability are concentrated in particular markets.

### Content growth

The yearly analysis shows changes in the number of titles added over time.

This helps identify periods where Netflix's catalog expanded more rapidly.

### Ratings

The rating analysis shows which audience categories are most represented in the dataset.

---

## 11. Business Recommendations

Based on the analysis, the following recommendations can be considered:

### 1. Maintain a balanced content portfolio

Since Movies form a large part of the catalog, Netflix could continue monitoring the balance between Movies and TV Shows to maintain variety.

### 2. Monitor genre trends

Popular genres can be monitored regularly to understand viewer demand and identify areas where additional content may be useful.

### 3. Explore regional opportunities

The country-level analysis can be used to identify markets with lower content representation and evaluate opportunities for regional content.

### 4. Use forecasting for planning

Historical content trends and forecasting models can support high-level planning for future content additions.

### 5. Combine analytics with business data

The current dataset focuses mainly on catalog information. Adding viewing hours, engagement, subscriptions and revenue data in the future would make the business analysis more useful.

---

## 12. Technologies Used

The main technologies used in this project are:

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Plotly
* Matplotlib
* Jupyter Notebook
* Git & GitHub

---

## 13. Project Structure

```text
Auspify_Data_Science_Internship/
│
├── data/
│   ├── raw/
│   └── cleaned_dataset.csv
│
├── dashboard/
│   └── app.py
│
├── notebooks/
│   └── Netflix analysis notebooks
│
├── models/
│   └── model files
│
├── REPORT.md
├── README.md
└── requirements.txt
```

---

## 14. Conclusion

This project helped me put together a complete data science workflow instead of working on only one part of the process.

I started with data cleaning and exploratory analysis, then moved to visualization and predictive modeling. Finally, I combined the results into an interactive Streamlit dashboard with business insights and recommendations.

The project also helped me understand how machine learning results can be presented together with normal business analytics in a way that is easier to understand.

The final **Netflix Intelligence** dashboard provides one place to explore the Netflix catalog, understand content trends and view the predictive analysis results.

---

## 15. Internship Details

**Organization:** Auspify Technologies
**Program:** Data Science Internship
**Task:** Task 6 – Data Science Business Insights Dashboard
**Project:** Netflix Intelligence
