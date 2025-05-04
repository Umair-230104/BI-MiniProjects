import streamlit as st
import pandas as pd 

st.markdown("<h1 style='text-align: center;'>Overall wine data</h1>", unsafe_allow_html=True)


def data_load():
    red_dataset = pd.read_excel('Data/winequality-red.xlsx')
red_dataframe = pd.read_excel('Data/winequality-red.xlsx', header=1)
red_dataframe.drop_duplicates(inplace=True)
red_dataframe["wine_type"] = "red"

white_dataframe = pd.read_excel('Data/winequality-white.xlsx')
white_dataframe = pd.read_excel('Data/winequality-white.xlsx', header=1)
white_dataframe.drop_duplicates(inplace=True)
white_dataframe['wine_type'] = 'white'

all_wine = pd.concat([white_dataframe, red_dataframe], ignore_index=True)
st.dataframe(all_wine)
