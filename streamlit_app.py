import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My parents new healthy diner")

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacodo toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruits_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list=my_fruits_list.set_index('Fruit')

#let's put a pick list here
fruits_selected=streamlit.multiselect('pick some fruits:', list(my_fruits_list.index),['Avocado','Strawberries'])
filtered_fruits=my_fruits_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(filtered_fruits)

def fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_normalized=fruityvice_data(fruit_choice)
    streamlit.dataframe(fruityvice_normalized)
except:
  streamlit.error()


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
# add button to load the fruit
if streamlit.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_row)


streamlit.stop()
add_my_fruit=streamlit.text_input('what fruit you would like to add?')
my_cur.execute("Insert into pc_rivery_db.public.fruit_load_list values ('"+add_my_fruit+"')")
streamlit.write("Thanks for adding", add_my_fruit)
my_cur.execute("Insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")



