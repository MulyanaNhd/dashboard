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

    total_kasus = df['Total Cases'].max()
    st.metric(label = "Total Kasus Covid-19 di Indonesia", value=f"{total_kasus:,}")
    
    #Menampilkan hanya kolom lokasi dari kolom kasus baru hingga total sembuh
    df_selected = df.loc[:, 'Location':'Total Recovered']
    st.dataframe(df_selected.head(10))
    
    st.dataframe(df.head(10)) 
    
    #menampilkan statistik deskriptif dataset
    st.subheader("📈 Statistik Deskriptif Dataset")
    st.write(df.describe())