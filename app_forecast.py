import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests
from datetime import datetime,timedelta

st.title('Forecasting System')

# matrix = pickle.load(open("books.pk1","rb"))
model = pickle.load(open(r"C:\Users\kittu\model_forecast.pk1","rb"))
# result = pickle.load(open("result.pk1","rb")
# number = st.number_input('Insert a number')
# st.write('The current number is ', number)
# # def forecast(num):
#     pred=model.forecast(num, alpha=0.05)
#     return pred
d=st.date_input("select the date")
    # "select the date",

st.write('Your selected date is:', d)

number = int(st.number_input('number of days '))
st.write(' number of days selected', number)
if st.button('FORECAST'):

    a=[]

    startdate = d
    for day in range(1,number):
        x=(startdate + timedelta(days=day))
        a.append(x)


    pred = model.forecast(30)

    pred=pred.tolist()
    df = pd.DataFrame({
        'date':a,
        'second column': pred
    })

    df = df.rename(columns={'date': 'index'}).set_index('index')



    st.line_chart(df,height=1000)
    st.table(df)






     # col1=st.columns(1)
    # with col1:
    # st.table(forecast(number))




