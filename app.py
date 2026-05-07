import streamlit as st
from data import *

def judul():
    # Judul dashboard tetap dengan style Anda
    st.title("📊 Dashboard Covid-19 Indonesia")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data Covid-19 di Indonesia 🇮🇩")

# Sidebar navigasi
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# Load data awal untuk mengambil daftar lokasi
df_raw = load_data()

# Sidebar Filters (Tersedia untuk semua halaman)
year = select_year()
locations = select_location(df_raw)

# Filter data berdasarkan input sidebar
df_filtered = filter_data(df_raw, year, locations)

# HALAMAN HOME
if menu == "Home":
    judul()
    # Menampilkan metrik, pie chart, bar charts, dan peta
    kolom(df_filtered)
    pie_chart(df_filtered)
    bar_chart_kematian(df_filtered)
    bar_chart_sembuh(df_filtered)
    map_chart(df_filtered, year)

# HALAMAN DATA
elif menu == "Halaman Data":
    judul()
    show_data(df_filtered)

st.markdown("---")
st.markdown("© 2026 Mulyana Nurhamida/184240027. All rights reserved.")