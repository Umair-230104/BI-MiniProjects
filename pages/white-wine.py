import streamlit as st
import pandas as pd 


st.markdown("<h1 style='text-align: center;'>White wine data</h1>", unsafe_allow_html=True)

def data_load():
    white_dataframe = pd.read_excel('Data/winequality-white.xlsx')
white_dataframe = pd.read_excel('Data/winequality-white.xlsx', header=1)
white_dataframe.drop_duplicates(inplace=True)
white_dataframe['wine_type'] = 'white'
st.dataframe(white_dataframe)
