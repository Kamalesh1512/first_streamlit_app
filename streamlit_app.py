import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title("My parents new healthy diner")

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacodo toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruits_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list=my_fruits_list.set_index('Fruit')

fruits_selected=streamlit.multiselect('pick some fruits:', list(my_fruits_list.index),['Avocado','Strawberries'])
filtered_fruits=my_fruits_list.loc[fruits_selected]

streamlit.dataframe(filtered_fruits)



streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# json is normalized. 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# dataframe is created
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

streamlit.header("The fruit load list contains:")
add_my_fruit=streamlit.text_input('what fruit you would like to add?')
my_cur.execute("Insert into pc_rivery_db.public.fruit_load_list values ('"+add_my_fruit+"')")
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)

