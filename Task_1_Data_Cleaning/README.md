# Task 1 - Data Cleaning and Preprocessing

## About the Project

In this task, I worked on a dataset containing information about Netflix movies and TV shows.

The main goal was to understand the dataset, check for data quality issues, and prepare the data for further analysis.

## Dataset

The original dataset contains:

* 8,790 rows
* 10 columns

Some of the columns include:

* show_id
* type
* title
* director
* country
* date_added
* release_year
* rating
* duration
* listed_in

## What I Did

### 1. Checked the Dataset

I first checked the shape, column names, data types, and basic information about the dataset.

### 2. Checked Missing Values

I checked all columns for missing values.

There were no missing values in the dataset, so no missing-value filling was required.

### 3. Checked Duplicate Rows

I checked the dataset for duplicate records.

There were no duplicate rows.

### 4. Cleaned Text Data

I removed unnecessary spaces from the text columns to keep the values consistent.

### 5. Worked on Date Column

The `date_added` column was initially stored as text, so I converted it into datetime format.

I also created three new columns:

* `added_year`
* `added_month`
* `added_day`

### 6. Cleaned Duration

The `duration` column had values like:

* `90 min`
* `1 Season`
* `2 Seasons`

I separated these into two columns:

* `duration_value`
* `duration_type`

I also converted `Season` and `Seasons` into one consistent category.

### 7. Worked on Genres

The `listed_in` column contains one or more genres for each title.

I created a new `primary_genre` column by taking the first genre from the list.

I kept the original `listed_in` column as well.

## Final Result

After preprocessing, the dataset contains:

* 8,790 rows
* 16 columns
* 0 missing values
* 0 duplicate rows

The cleaned dataset is saved as:

`cleaned_dataset.csv`

## Files in This Project

* `Dataset.csv` - Original dataset
* `cleaned_dataset.csv` - Cleaned dataset
* `Task_1_Data_Cleaning.ipynb` - Jupyter Notebook containing the complete work
* `README.md` - Project information
