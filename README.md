# Diabetes-Data-Analysis

A data analysis project designed to determine the effect of health problems and attributes of patients on whether or not they have diabetes

## Diabetes Overview

Diabetes is a health condition where blood sugar spikes due to insufficient insulin production (which is needed to allow glucose to enter cells) or the improper response of the body to insulin. Long-term consequences of diabetes include heart attack, stroke, nerve damage, and hearing loss. As these consequences can either be fatal or worsen quality of life, identifying patients at risk is critical for early diagnosis and treatment of these patients. Early treatment, in turn, greatly reduces the chance that diabetes evolves into the afformentioned long-term effects. This analysis project will contribute to early diabetes diagnosis and treatment by investigating the effect of various risk factors on whether or not a patient has diabetes.

## Dataset

- Healthcare Diabetes Dataset by Nandita Pore
    - Used for predicting if a patient is at risk of diabetes based on a list of risk factors
- Key Variables
    - Outcome: the main variable for my analysis, states if diabetes is present (1) or absent (0) in a patient
    - Blood pressure, diastolic (mmHg)
    - BMI (kg/m^2)
    - Age (years)

## Research Questions

1. Is diabetes more likely in older people?
2. Do high blood pressure and high BMI create a higher risk of diabetes?

## Descriptive Stats

### Age

![Age variable descriptive stats](results/age_descriptive.png)

According to these descriptive stats, there are 2768 entries in this dataset. The average age of people listed in this dataset is approximately 33 years old. The range of ages included is 21 to 81 years old. The standard deviation is 11 years, which is large in the context of age, so the data points are spread out, indicating high variability in the age data.

## Visualizations

## Hypothesis Testing

## Insights

## How to Run/See the Analysis Files

### Python

Go to the python directory, choose either desc.py or ttest.py to run, and run this command

```bash
python3 [desc.py or ttest.py]
```

### R

Copy and paste the contents of either desc.r or ttest.r. Visit [Posit Cloud](posit.cloud) and make a new project. Then add a new R file, paste your code, save the file and run it. Be sure to also paste the CSV file into a new text file and save it as a CSV.

### SAS

TBD

### PowerBI Dashboard

Link TBD

## Sources/Tools Used

1. Dataset link: https://www.kaggle.com/datasets/nanditapore/healthcare-diabetes
2. Presentation tool: https://gamma.app/create
3. The Markdown Guide: https://www.markdownguide.org/
4. Diabetes overview: https://my.clevelandclinic.org/health/diseases/7104-diabetes
5. Coding assistant: https://claude.ai
6. pandas: https://pandas.pydata.org/
