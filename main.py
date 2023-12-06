import pandas as pd
import streamlit as st

from joblib import load

lrm = load("trained_model.h5")

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
st.write("Income code selected :", income)

education_dict = {
    "Postgraduate or professional degree, including masterâs,doctorate, medical or law degree (e.g., MA, MS, PhD, MD, JD)":8,
    "Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school)":7,
    "Four-year college or university degree/Bachelorâs degree (e.g., BS, BA, AB)":6,
    "Two-year associate degree from a college or university": 5,
    "Some college, no degree (includes some community college)": 4,
    "High school graduate (Grade 12 with diploma or GED certificate)":3,
    "High school incomplete (Grades 9-11 or Grade 12 with NO diploma)":2,
    "Less than high school (Grades 1-8 or no formal schooling)":1
}

education   = education_dict[st.selectbox("What is your highest education level ?", tuple(education_dict.keys()))]
st.write("Education code selected :", education)

par_dict = {

"Yes":1,
"No":2,
"Don't know":8,
"Refused":9
}

par   = par_dict[st.selectbox("are you a parent of a child under 18 living in your home?", tuple(par_dict.keys()))]
st.write("par code selected :", par)

marital_dict = {
"Married":1,
"Living with a partner":2, 
"Divorced":3,
"Separated":4,
"Widowed":5, 
"Never been married":6,
"Don't know":8,
"Refused":9  
}
marital = marital_dict[st.selectbox("current marital status", tuple(marital_dict.keys()))]

gender_dict = {
    "male":1,
    "female":2,
    "other":3,
    "Don't know":98,
    "Refused": 99
}
gender = gender_dict[st.selectbox("Gender", tuple(gender_dict.keys()))]
st.write("Gender code selected :", gender)


age = st.number_input("Enter Age : ")
st.write("Age entered:", age)

test_df = pd.DataFrame({"income":[income],"educ2":[education],"par":[par],"marital":[marital],"gender":[gender], "age":[age]})


prediction = lrm.predict(test_df)

st.write("Prediction :", "Yes, a linkedin User" if prediction[0] == 1 else "Not a linkedin User")