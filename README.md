Netflix Movies and TV Shows Data Cleaning & Preprocessing

This project involves cleaning and preprocessing the Netflix Titles dataset available on Kaggle. The main goal is to prepare the raw data for further analysis and machine learning tasks by handling missing values, fixing inconsistencies, and transforming key features.

Dataset Source : https://www.kaggle.com/datasets/shivamb/netflix-shows?select=netflix_titles.csv

Steps Performed:

1. Data Cleaning
   
-->Removed duplicate entries

-->Handled missing values in director, cast, country, rating, duration, and date_added

-->Corrected misclassified values (e.g., duration values in the rating column)

-->Stripped extra whitespace from textual columns

2.Data Transformation

-->Converted date_added to proper datetime format

-->Extracted year, month, and month_name from the date_added

-->Split duration into duration_num and duration_unit

3. Data Filtering
   
-->Removed entries with invalid or zero duration

-->Estimated total duration in minutes

-->Removed outliers using the Interquartile Range (IQR) method

4.Final Checks

-->Verified distributions of type, rating, and country

-->Ensured consistent duration_unit formats

-->Confirmed date formatting and data integrity

5. Data Export
   
-->Saved the cleaned dataset as cleaned_netflix_data.csv

Output:

Cleaned data file: cleaned_netflix_data.csv

Final shape: (rows, columns)

Null values: 0

Duplicates: 0

Usage

You can use the cleaned dataset for:

1.Exploratory Data Analysis (EDA)

2.Dashboard creation

3.Machine learning model building

4.Recommendation systems
