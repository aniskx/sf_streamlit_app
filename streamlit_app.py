import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Main menu')
streamlit.header('Dinner')
streamlit.text('Art1')
streamlit.text('Art2')
streamlit.text('Art3')

streamlit.header('Platfroms')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)




streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
