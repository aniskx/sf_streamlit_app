import streamlit 
import pandas

streamlit.title('Main menu')
streamlit.header('Target')
streamlit.text('Distributed computing')
streamlit.text('Data Modeling')
streamlit.text('Cloud tech')

streamlit.header('Platfroms')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
