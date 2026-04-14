import pandas as pd
import plotly.express as px
import streamlit as st

# encabezado
st.header('Análisis de vehículos en USA')

# leer datos
df = pd.read_csv('vehicles_us.csv')

# botón para histograma
hist_button = st.button('Mostrar histograma')

if hist_button:
    st.write('Histograma del kilometraje de vehículos')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# botón para scatter
scatter_button = st.button('Mostrar gráfico de dispersión')

if scatter_button:
    st.write('Relación entre precio y kilometraje')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

# botón para checkbox
build_hist = st.checkbox('Mostrar histograma')

if build_hist:
    st.write('Histograma del kilometraje')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig)

build_scatter = st.checkbox('Mostrar dispersión')

if build_scatter:
    st.write('Relación precio vs kilometraje')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig)