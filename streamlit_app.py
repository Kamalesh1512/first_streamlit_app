import streamlit
import pandas as pd
import requests



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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
