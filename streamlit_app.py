import streamlit as st
import pandas

st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')

st.text('\N{flexed biceps} Omega 3 and Blueberry Cereal')
st.text('\N{green salad} Kale, Spinach & Rocket Smoothie')
st.text('\N{egg} Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_frulit_list = my_fruit_list.set_index('Fruit')

show my_fruit_list.index

st.multiselect("Pick some fruits:", list(my_fruit_list.index))
st.dataframe(my_fruit_list)
