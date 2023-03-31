I did Analysis on Insurance Claim : Demographic and Health, ETL(Extract, Tranform, Load) process using Cloud Function, Datawarehouse as BigQuery and Tableau as BI tool.

Created three bucket those are : Raw, Cleansed & Curated 
Raw: have to upload the csv file (https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health)
Cleansed: data come from raw bucket and get transformed stored in CSV file
Curated: data come from cleansed bucket, get transformed and stored in the format of JSON

Created three Cloud Function: Raw_to_cleansed, Cleansed_to_curated & Curated_to_BigQuery
These function get trigger on finalizing/creating file, langauge Python

BigQuery - DW
Created some materialized view

Tableau - BI tool




