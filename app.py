import pandas as pd
import plotly.express as px
import streamlit as st

# encabezado
st.header('Análisis de vehículos en USA')

# leer datos
df = pd.read_csv('vehicles_us.csv')

# checkbox histograma
build_hist = st.checkbox('Mostrar histograma')

if build_hist:
    st.write('Histograma del kilometraje')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, key='histograma')  

# checkbox dispersión
build_scatter = st.checkbox('Mostrar dispersión')

if build_scatter:
    st.write('Relación precio vs kilometraje')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, key='dispersion')  
    