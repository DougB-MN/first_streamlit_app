import streamlit as st
import pandas
import requests as r

st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')

st.text('\N{flexed biceps} Omega 3 and Blueberry Cereal')
st.text('\N{green salad} Kale, Spinach & Rocket Smoothie')
st.text('\N{egg} Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

print (fruits_selected)

#fruits_to_show = my_fruit_list.loc('Avocado')

#st.dataframe(fruits_to_show)
