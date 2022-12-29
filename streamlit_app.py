import streamlit
import pandas
streamlit.title('Breakfast Menu')
streamlit.header('My breakkie')
streamlit.text('🐔 Scrambled eggs')
streamlit.text('🥑 Avocado & Cheese')
streamlit.text('🥣 Porridge')
streamlit.title('My Parents New Healthy Diner')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
