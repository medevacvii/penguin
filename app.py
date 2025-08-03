import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguin Species Prediction ML app")
st.info("This is an end-to-end Machine Learning app")

with st.expander("Data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df
  
  st.write("Input variables")
  X_raw = df.drop('species', axis = 1)
  X_raw
  
  st.write("Target variable")
  y_raw = df.species
  y_raw

  st.write("Descriptive Statistics")
  des = df.describe()
  des

  st.write("Mor information about Data")
  info = df.info()
  st.text(info)
  
with st.expander("Data Visualization"):
  st.scatter_chart(data = df, x = 'bill_length_mm', y = 'body_mass_g', color = 'species')

with st.expander("Input data"):
  pass

with st.expander("Data Preparation"):
  pass

with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male','female'))
  data = {
    'island':island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'gender': gender
  }

  input_df = pd.DataFrame(data, index[0])
  input_penguins = pd.concat([input_df, X_raw], axis = 0])
