import streamlit 
import pandas

streamlit.title('Main menu')
streamlit.header('Dinner')
streamlit.text('Art1')
streamlit.text('Art2')
streamlit.text('Art3')

streamlit.header('Platfroms')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruits_to_show)

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


