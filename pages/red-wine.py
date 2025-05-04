import streamlit as st
import pandas as pd 

st.markdown("<h1 style='text-align: center;'>Red wine data</h1>", unsafe_allow_html=True)


def data_load():
    red_dataset = pd.read_excel('Data/winequality-red.xlsx')
red_dataframe = pd.read_excel('Data/winequality-red.xlsx', header=1)
red_dataframe.drop_duplicates(inplace=True)
red_dataframe["wine_type"] = "red"
st.dataframe(red_dataframe)