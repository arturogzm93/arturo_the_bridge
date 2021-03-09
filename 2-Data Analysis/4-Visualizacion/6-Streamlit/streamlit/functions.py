import streamlit as st
import pandas as pd
from PIL import Image

def config_page():

    st.set_page_config(page_title = 'Cargatron', page_icon = ':electric_plug:', layout ='wide')

@st.cache(suppress_st_warning=True)

def cargar_datos(csv_path, uploader_csv):

    if uploader_csv is None:

        df = pd.read_csv(csv_path, sep = ';')
        df = df.rename(columns={'latidtud':'lat', 'longitud': 'lon'})

    else:

        st.write('No te flipes, que esto no esta preparado para subir tu caca.')
        st.stop()
        uploader_csv.seek(0)
        df = pd.read_csv(uploader_csv, sep=';')

    st.balloons()

    return df

def home(df):

    img = Image.open('puntos-recarga-madrid.jpg')
    st.image(img, use_column_width='auto')

    with st.beta_expander('¿Quieres saber más?'):

        st.write('Ante el problema climático actual se estan conviertiendo en una solución factible')

    with st.echo():

        st.dataframe(df)  # asi o ejecuta y ademas te muestra el nombre del archivo

def datos(df):

    st.write('El mapa: ')
    st.map(df)

    st.write('Cargadores por distrito')
    cargadores_distritos = df.groupby('DISTRITO')['Nº CARGADORES'].sum()
    st.bar_chart(cargadores_distritos)

    st.write('Cargadores por operador')
    cargadores_operador = df.groupby('OPERADOR')['Nº CARGADORES'].sum()
    st.bar_chart(cargadores_operador)

def filtros(df):

    check_distrito = st.sidebar.checkbox('¿Quieres filtrar distritos?')

    distritos = df['DISTRITO'].unique().tolist()
    filtro_distrito = st.sidebar.selectbox('Seleccionar distrito:', distritos)

    check_operador = st.sidebar.checkbox('¿Quieres filtrar operadores?')

    operadores = df['OPERADOR'].unique().tolist()
    filtro_operador = st.sidebar.selectbox('Seleccionar operador:', operadores)

    check_num = st.sidebar.checkbox('¿Quieres filtrar numero de cargadores?')

    min_carg = df['Nº CARGADORES'].min()
    max_carg = df['Nº CARGADORES'].max()
    n_posibles = range(min_carg, max_carg + 1)
    filtro_num_carg = st.sidebar.select_slider('Selecciona el nº de cargadores',
                             n_posibles, value=(min_carg, max_carg))

    if check_distrito:

        df = df[df['DISTRITO'] == filtro_distrito]

    if check_operador:

        df = df[df['OPERADOR'] == filtro_operador]

    if check_num:

        df = df[(df['Nº CARGADORES'] >= filtro_num_carg[0]) & (df['Nº CARGADORES'] <= filtro_num_carg[1])]

    if df.shape[0] == 0:

        st.warning('Ey!!! Te has pasado filtrando, cambia los filtros')
        st.stop()

    if check_distrito:

        zoom = 13

    else:

        zoom = 11

    col1, col2 = st.beta_columns([3, 2])

    with col1:

        st.map(df, zoom)

    with col2:

        if not check_distrito:

            st.write('Cargadores por distrito')
            cargadores_distritos = df.groupby('DISTRITO')['Nº CARGADORES'].sum()
            st.bar_chart(cargadores_distritos)

        if not check_operador:

            st.write('Cargadores por operador')
            cargadores_operador = df.groupby('OPERADOR')['Nº CARGADORES'].sum()
            st.bar_chart(cargadores_operador)