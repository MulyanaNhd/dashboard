import streamlit as st
import pandas as pd

#fungsi untuk memuat data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def total_kasus():
    df = load_data()
    total_kasus = df['New Cases'].sum()
    st.metric(label = "Total Kasus Covid-19 di Indonesia", value=f"{total_kasus:,}")
    return total_kasus

def total_deaths():
    df = load_data()
    total_kematian = df['New Deaths'].sum()
    st.metric(label = "Total Kematian Kematian Keseluruhan", value=f"{total_kematian:,}") 
    return total_kematian

def total_recovery():
    df = load_data()
    total_sembuh = df['New Recovered'].sum()
    st.metric(label = "Total Sembuh Keseluruhan", value=f"{total_sembuh:,}")
    return total_sembuh

def kolom():
    kasus = total_kasus()
    kematian = total_deaths()
    sembuh = total_recovery()

    col1, col2, col3 = st.columns(3)
    col1.metric(label = "📈 Total Kasus ", value = kasus, border = True)
    col2.metric(label = "☠️ Total Kematian ", value = kematian, border = True)
    col3.metric(label = "🛡️ Total Sembuh ", value = sembuh, border = True)

#fungsi untuk menampilkan data dalam bentuk tabel
def show_data():
    df = load_data()
    st.subheader("📌 Data Covid-19 di Indonesia")
 
    #Menampilkan hanya kolom lokasi dari kolom kasus baru hingga total sembuh
    df_selected = df.loc[:, 'Location':'Total Recovered']
    st.dataframe(df_selected.head(10))
    
    st.dataframe(df.head(10)) 
    
    #menampilkan statistik deskriptif dataset
    st.subheader("📈 Statistik Deskriptif Dataset")
    st.write(df.describe())
