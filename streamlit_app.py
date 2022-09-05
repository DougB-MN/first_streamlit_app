import streamlit as st
import pandas as pd
import requests as r
import snowflake.connector as sfc

my_cnx = sfc.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select current_user(), current_account(),current_region()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')

st.text('\N{flexed biceps} Omega 3 and Blueberry Cereal')
st.text('\N{green salad} Kale, Spinach & Rocket Smoothie')
st.text('\N{egg} Hard-Boiled Free-Range Egg')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

df = pd.DataFrame (fruits_selected, columns = ['Fruit'])

st.dataframe(df)

fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered ', fruit_choice)

fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

st.dataframe(fruityvice_normalized)
