import streamlit as st
from data import *

def judul():
    #judul dashboard
    st.title("📊 Dashboard Covid-19")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data Covid-19 di Indonesia")

st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

#HALMAN HOME
if menu == "Home":
    judul()
    #pilih tahun
    year = select_year()

    #Load & filter data
    df = load_data()
    df_filtered = filter_data(df, year)
    kolom(df_filtered)
    pie_chart(df_filtered)

elif menu == "Halaman Data":
    judul()
    year = select_year()
    #Load & filter data
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)

st.markdown("---")
st.markdown("© 2026 Mulyana Nurhamida/184240027. All rights reserved.")
