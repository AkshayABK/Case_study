create or replace table q-gcp-buc1-fsi-training-23-03.Akshay.BMI as
(select PatientID, 
case 
when bmi<=18.5 then 'Underweight' 
when bmi between 18.5 and 24.9 then 'Normal' 
when bmi between 25 and 29.9 then 'Overweight' 
when bmi between 30 and 39.9 then 'Obese' 
when bmi>=40 then 'Morbidly obese' 
END as BMI_status, 
case 
when bmi between 18.5 and 24.9 and diabetic ='No'and bloodpressure<120 and smoker='No' then 'Healthy' 
when diabetic='Yes' or smoker='Yes' or bloodpressure>130 or bmi>=25 then 'Un_healthy' 
when bmi<18.5 then 'Un_healthy' 
end as Healthy_status  
from `q-gcp-buc1-fsi-training-23-03.Akshay.Curated_Cleansed_insurance_data`);

----View 01----
create or replace materialized view `q-gcp-buc1-fsi-training-23-03.Akshay.View_01` as select a.age_category, b.BMI_status, count(a.patientID) as Number_of_ppl, sum(claim) as Total_claim from`q-gcp-buc1-fsi-training-23-03.Akshay.Curated_Cleansed_insurance_data` as a inner join `q-gcp-buc1-fsi-training-23-03.Akshay.BMI` as b on a.patientID = b.patientID where bmi_status in('Normal','Overweight','Obese','Morbidly obese') group by a.age_category,b.BMI_status;

select * from `q-gcp-buc1-fsi-training-23-03.Akshay.View_01` order by Total_claim desc;

----View 02----
create or replace materialized view `q-gcp-buc1-fsi-training-23-03.Akshay.View_02` as select region,count(case when Healthy_status='Healthy' then 1 end) as Healthy_ppl, COUNT (case when Healthy_status='Un_healthy' then 1 end) as Unhealthy_ppl from `q-gcp-buc1-fsi-training-23-03.Akshay.Curated_Cleansed_insurance_data` a inner join `q-gcp-buc1-fsi-training-23-03.Akshay.BMI` b on a.PatientID = b.PatientID group by region;

select * from `q-gcp-buc1-fsi-training-23-03.Akshay.View_02` order by Unhealthy_ppl desc;


