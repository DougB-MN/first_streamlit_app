import streamlit as st
import pandas as pd
import requests as r
import snowflake.connector as sfc
from urllib.error import URLError

my_cnx = sfc.connect(**st.secrets["snowflake"])

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
  
st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')

st.text('\N{flexed biceps} Omega 3 and Blueberry Cereal')
st.text('\N{green salad} Kale, Spinach & Rocket Smoothie')
st.text('\N{egg} Hard-Boiled Free-Range Egg')

st.header('\N{banana} Build your own fruit smoothie \N{grapes}')
          
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

df = pd.DataFrame (fruits_selected, columns = ['Fruit'])

st.dataframe(data=fruits_selected)

st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

if st.button('Get Fruit Load List'):
    st.header("The fruit_load_list contains:")
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)

try:
    add_my_fruit = st.text_input('What fruit would you like to add?')
    if not add_my_fruit:
        st.error("Please add a fruit to the list.")
    else:
        st.write('Thanks for adding ', add_my_fruit)
        my_cur = my_cnx.cursor()
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('" + add_my_fruit +"')")
except URLError as e:
        st.error()


