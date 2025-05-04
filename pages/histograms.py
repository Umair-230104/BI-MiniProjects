import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

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

def load_histograms(df):
    numeric_columns = df.select_dtypes(include='number').columns
    for column in numeric_columns:
        fig, ax = plt.subplots()
        df[column].hist(bins=30, ax=ax)
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)  # Display the plot in Streamlit

load_histograms(all_wine)