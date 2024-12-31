import streamlit as st
import numpy as np
import string
import pickle

model = pickle.load(open('diamond_model.pk1', 'rb'))

def main():
  st.title("Diamond Price Estimator")
  st.caption("_By :blue[Ananya Salian]_")
  with st.expander(label="Introduction"):
    st.write("Intro!!!")


  carat = st.slider("Carat size: ", 0.2, 5.0)
  cut = st.selectbox( "Quality of cut: ", ("Ideal", "Premium", "Very Good", "Good", "Fair"))
  color = st.select_slider("Diamond colour: ", options=['D', 'E', 'F', 'G', 'H', 'I', 'J'])
  clarity = st.select_slider("Clarity: ", options=['SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
  depth = st.slider("total Depth Percentage _(percentage)_: ", 43, 79)
  xval = st.slider("Length _(mm)_: ", 0, 10.74)
  yval = st.slider("Width _(mm)_: ", 0, 58.9)
  zval = st.slider("Depth _(mm)_: ", 43, 31.8)
  table = st.slider("Width of top of diamond, relative to widest point _(mm)_: ", 43, 95)

  inputs = [[carat, cut, color, clarity, depth, xval, yval, zval, table]]

  if st.button("Predict"):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    print(updated_res)
  
  

                         


