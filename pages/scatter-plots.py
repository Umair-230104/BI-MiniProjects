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

def load_scatter_plots():
    # Scatter plot: Alcohol vs. Quality
    fig1 = plt.figure(figsize=(10, 5))  # store figure object
    plt.scatter(red_dataframe['alcohol'], red_dataframe['quality'], color='red', label='Rødvin', alpha=0.5)
    plt.scatter(white_dataframe['alcohol'], white_dataframe['quality'], color='gold', label='Hvidvin', alpha=0.5)
    plt.xlabel('Alkohol (%)')
    plt.ylabel('Kvalitet')
    plt.title('Alkoholindhold vs. Kvalitet')
    plt.legend()
    plt.grid(True)
    st.pyplot(fig1)  # ✅ pass the figure, not plt

    # Scatter plot: Residual sugar vs. Quality
    fig2 = plt.figure(figsize=(10, 5))
    plt.scatter(red_dataframe['residual sugar'], red_dataframe['quality'], color='pink', label='Rødvin', alpha=0.5)
    plt.scatter(white_dataframe['residual sugar'], white_dataframe['quality'], color='orange', label='Hvidvin', alpha=0.5)
    plt.xlabel('Restsukker (g/dm³)')
    plt.ylabel('Kvalitet')
    plt.title('Restsukker vs. Kvalitet')
    plt.legend()
    plt.grid(True)
    st.pyplot(fig2)

load_scatter_plots()






    