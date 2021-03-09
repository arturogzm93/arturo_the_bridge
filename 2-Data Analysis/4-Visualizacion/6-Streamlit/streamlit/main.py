import streamlit as st
import functions as ft

csv_path = 'red_recarga_acceso_publico_2021.csv'

ft.config_page()
st.title('CARGATRON')

uploader_csv = st.sidebar.file_uploader('Introducir CSV', type = ['csv'])
st.write(uploader_csv)

df = ft.cargar_datos(csv_path, uploader_csv)

menu = st.sidebar.selectbox('Seleccionar menu:', ('home', 'datos', 'filtros'))

if menu == 'home':

    ft.home(df)

elif menu == 'datos':

    ft.datos(df)

elif menu == 'filtros':

    ft.filtros(df)
