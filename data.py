import streamlit as st
import pandas as pd
import plotly.express as px


#fungsi untuk memuat data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def filter_data(df, year = None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

def select_year():
    return st.sidebar.selectbox("Pilih Tahun 🗓️", 
    options=[None, 2020, 2021, 2022],
    format_func=lambda x: "Semua Tahun" if x is None else str(x))

def total_kasus(df):
    return df['New Cases'].sum()

def total_deaths(df):
    return df['New Deaths'].sum()

def total_recovery(df):
    return df['New Recovered'].sum()

def kolom(df):
    kasus = total_kasus(df)
    kematian = total_deaths(df)
    sembuh = total_recovery(df)

    col1, col2, col3 = st.columns(3)
    col1.metric(label = "📈 Total Kasus ", value = kasus, border = True)
    col2.metric(label = "☠️ Total Kematian ", value = kematian, border = True)
    col3.metric(label = "🛡️ Total Sembuh ", value = sembuh, border = True)

#fungsi untuk menampilkan data dalam bentuk tabel
def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    df_selected = df[selected_columns]
    
    st.subheader("Data Covid-19 di Indonesia 🔴⚪")
    st.dataframe(df_selected.head(10))
 
    #Menampilkan hanya kolom lokasi dari kolom kasus baru hingga total sembuh
    df_selected = df.loc[:, 'Location':'Total Recovered']
    st.dataframe(df_selected.head(10))
    
    st.dataframe(df.head(10)) 
    
    #menampilkan statistik deskriptif dataset
    st.subheader("📈 Statistik Deskriptif Dataset")
    st.write(df.describe())

def pie_chart(df):
    #pemanggilan data 
    total_mati = total_deaths(df)
    total_sembuh = total_recovery(df)

    #dataframe
    data ={
        'Status': ['Mati', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }

    fig = px.pie(
        data, 
        names='Status', 
        values='Jumlah', 
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole = 0.5,
        color_discrete_sequence=[ '#4682B4', '#8B0000']
    )

    st.plotly_chart(fig, use_container_width=True)
