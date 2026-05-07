import streamlit as st
import pandas as pd
import plotly.express as px

# Fungsi untuk memuat data
def load_data():
    df = pd.read_csv("covid_19_indonesia_time_series_all.csv")
    # Menghilangkan baris agregat 'Indonesia' agar tidak double saat menghitung total provinsi
    df = df[df["Location"] != "Indonesia"]
    return df

def filter_data(df, year=None, locations=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    if locations:
        df = df[df['Location'].isin(locations)]
    return df

def select_year():
    return st.sidebar.selectbox("Pilih Tahun 🗓️", 
    options=[None, 2020, 2021, 2022],
    format_func=lambda x: "Semua Tahun" if x is None else str(x))

def select_location(df):
    locations = sorted(df['Location'].unique())
    return st.sidebar.multiselect(
        "Pilih Provinsi 📍",
        options=locations,
        default=locations 
    )

# Menggunakan logika .last() agar total kasus akurat (kumulatif)
def total_kasus(df):
    if df.empty: return 0
    return df.sort_values('Date').groupby('Location').last()['Total Cases'].sum()

def total_deaths(df):
    if df.empty: return 0
    return df.sort_values('Date').groupby('Location').last()['Total Deaths'].sum()

def total_recovery(df):
    if df.empty: return 0
    return df.sort_values('Date').groupby('Location').last()['Total Recovered'].sum()

def kolom(df):
    kasus = total_kasus(df)
    kematian = total_deaths(df)
    sembuh = total_recovery(df)

    col1, col2, col3 = st.columns(3)
    # Menggunakan border=True sesuai style Anda
    col1.metric(label="📈 Total Kasus", value=f"{kasus:,}", border=True)
    col2.metric(label="☠️ Total Kematian", value=f"{kematian:,}", border=True)
    col3.metric(label="🛡️ Total Sembuh", value=f"{sembuh:,}", border=True)

def show_data(df):
    st.subheader("Data Covid-19 di Indonesia 🔴⚪")
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    st.dataframe(df[selected_columns].head(10))
    
    st.subheader("📈 Statistik Deskriptif Dataset")
    st.write(df.describe())

def pie_chart(df):
    total_mati = total_deaths(df)
    total_sembuh = total_recovery(df)

    data = {
        'Status': ['Mati', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }

    fig = px.pie(
        data, 
        names='Status', 
        values='Jumlah', 
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=['#4682B4', '#8B0000'] # Tetap pakai warna pilihan Anda
    )
    st.plotly_chart(fig, use_container_width=True)

def bar_chart_kematian(df):
    if df.empty: return
    df_last = df.sort_values('Date').groupby('Location', as_index=False).last()
    top5 = df_last.nlargest(5, 'Total Deaths')

    fig = px.bar(
        top5, x='Location', y='Total Deaths', color='Total Deaths',
        color_continuous_scale='Reds',
        title='🔝 5 Provinsi dengan Kematian Tertinggi'
    )
    st.plotly_chart(fig, use_container_width=True)

def bar_chart_sembuh(df):
    if df.empty: return
    df_last = df.sort_values('Date').groupby('Location', as_index=False).last()
    top5 = df_last.nlargest(5, 'Total Recovered')

    fig = px.bar(
        top5, x='Location', y='Total Recovered', color='Total Recovered',
        color_continuous_scale='Greens',
        title='🔝 5 Provinsi dengan Kesembuhan Tertinggi'
    )
    st.plotly_chart(fig, use_container_width=True)

def map_chart(df, year=None):
    if df.empty:
        st.info("⚠️ Tidak ada data koordinat untuk ditampilkan.")
        return

    # Agregasi data untuk peta
    df_map = df.groupby(['Location', 'Latitude', 'Longitude'], as_index=False)['New Cases'].sum()
    df_map = df_map.dropna(subset=['Latitude', 'Longitude'])

    fig = px.scatter_mapbox(
        df_map, lat="Latitude", lon="Longitude", size="New Cases",
        color="New Cases", hover_name="Location", zoom=3,
        center={"lat": -2.5, "lon": 118},
        size_max=20, opacity=0.7, color_continuous_scale="OrRd",
        title=f"Sebaran Kasus Baru ({year if year else 'Semua Tahun'})"
    )
    fig.update_layout(mapbox_style="carto-positron", height=500)
    st.plotly_chart(fig, use_container_width=True)