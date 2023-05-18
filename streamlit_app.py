'''from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
# Eample 2
st.subheader('Range Slider')
value = st.slider('Select a range of values',0.0,100.0,(25.0,75.0))
st.write('Values',value)
# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.line_chart(chart_data)

import streamlit as st

st.header('st.selectbox')
option = st.selectbox(
    'What is your favorite color?',
    ('Blue','Red','Green')
)
st.write('Your favorite color is ',option)

st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green','Yellow','Red','Blue'],
    ['Yellow','Red']
)
st.write('Your selected:',options)

st.header('st.checkbox')
st.write('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('coffee')
cola = st.checkbox('Cola')
if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

# Using st.secrets
import streamlit as st
st.title('st.secrets')
st.write(st.secrets['message']) '''

# Upload file scv lên.
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
