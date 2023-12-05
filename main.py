import pandas as pd
import streamlit as st

from joblib import load

lrm = load("trained_model.h5")
scaler = load("scaler.h5")

st.header("Linkedin User Prediction System")



income_dict  ={
"Less than $10,000":1 ,
"10 to under $20,000":2,
"20 to under $30,000":3,
"30 to under $40,000":4,
"40 to under $50,000":5,
"50 to under $75,000":6,
"75 to under $100,000":7,
"100 to under $150,000":8,
"$150,000 or more?":9,
"Don't know":98,
"Refused":99
}
income   = income_dict[st.selectbox(" What is your income level ?", tuple(income_dict.keys()))]
print("Income code selected :", income)


# educ2 (highest level of school/degree completed):
# 1 Less than high school (Grades 1-8 or no formal schooling)
# 2 High school incomplete (Grades 9-11 or Grade 12 with NO
# diploma)
# 3 High school graduate (Grade 12 with diploma or GED
# certificate)
# 4 Some college, no degree (includes some community college)
# 5 Two-year associate degree from a college or university
# 6 Four-year college or university degree/Bachelorâs degree
# (e.g., BS, BA, AB)
# 7 Some postgraduate or professional schooling, no postgraduate
# degree (e.g. some graduate school)
# 8 Postgraduate or professional degree, including masterâs,
# doctorate, medical or law degree (e.g., MA, MS, PhD, MD, JD)





# educ2      0
# par        0
# marital    0
# gender     0
# age        0