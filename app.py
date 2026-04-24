import streamlit as st
from data import *

def judul():
    #judul dashboard
    st.title("📊 Dashboard Covid-19")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data Covid-19 di Indonesia")

st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

if menu == "Home":
    judul()
    kolom()
elif menu == "Halaman Data":
    judul()
    show_data()

st.markdown("---")
st.markdown("© 2026 Mulyana Nurhamida/184240027. All rights reserved.")
