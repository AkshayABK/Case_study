I did Analysis on Insurance Claim : Demographic and Health, I made ETL(Extract, Tranform, Load) process using Cloud Function, Datawarehouse as BigQuery and used Tableau as BI tool.

Here I used three bucket those are : Raw, Cleansed & Curated 
Raw: Here we have to upload the csv file (https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health)
Cleansed: Here data come from raw bucket and get transformed stored in CSV file
Curated: Here data come from cleansed bucket, get transformed and stored in the format of JSON

Here I created three Cloud Function: Raw_to_cleansed, Cleansed_to_curated & curate



