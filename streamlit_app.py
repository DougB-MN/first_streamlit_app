import streamlit as st
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')

st.text('\N{flexed biceps} Omega 3 and Blueberry Cereal')
st.text('\N{green salad} Kale, Spinach & Rocket Smoothie')
st.text('\N{egg} Hard-Boiled Free-Range Egg')

streamlit.dataframe(my_fruit_list)
