import streamlit as st
import joblib
import numpy as np
model=joblib.load('rf_classifier.pkl')
def predict(input_data):
    predictions=model.predict(input_data)
    return predictions

st.title("Life Expectancy Deployment:")
liex=st.number_input("Enter Life expectancy:")
Am=st.number_input("Enter Adult Mortality:")
ind=st.number_input("Enter infant deaths:")
alc=st.number_input("Enter ratio of Alcohol consumption")
pe=st.number_input("Enter percentage expenditure:")
h=st.number_input("Enter Hepatitis B:")
ml=st.number_input("enter measles")
bmi=st.number_input("enter BMI ratio")
death=st.number_input("Enter under-five deaths :")
po=st.number_input("Enter number of Polio cases:")
Totex=st.number_input("enter Total expenditure")
Dip=st.number_input("enter Diphtheria")
hiv=st.number_input("Enter HIV/AIDS:")
gdp=st.number_input("Enter GDP:")
pop=st.number_input("Enter Population:")
thy=st.number_input("Enter thinness  1-19 years:")
th=st.number_input("Enter thinness 5-9 years:")
Icor=st.number_input("Enter Income composition of resources:")
sch=st.number_input("Enter Schooling:")
arr=np.array([[liex,Am,ind,alc,pe,h,ml,bmi,death,po,Totex,Dip,hiv,gdp,pop,thy,th,Icor,sch]])

if st.button("predict"):
    result = predict(arr)
    st.success(f"prediction:{result}")