import streamlit as st
import pandas as pd

#fungsi untuk memuat data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

#fungsi untuk menampilkan data dalam bentuk tabel
def show_data():
    df = load_data()
    st.subheader("📌 Data Covid-19 di Indonesia")
    st.dataframe(df.head(10)) #menampilkan 10 data pertama

#menampilkan statistik deskriptif dari dataset
st.subheader("📈 Statistik Deskriptif Dataset")
df = load_data()
st.write(df.describe())