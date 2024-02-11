import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
import plotly.express as px
import streamlit as st
def plot_missing_values(df):
    missing = (df.isnull().mean() * 100).round(2)
    fig = px.bar(missing, x=missing.index, y=missing.values,
                 labels={'x': 'Variable', 'y': 'Porcentaje de valores nulos'},
                 title="% de valores nulos ",
                 range_y=[0, 100],
                 template='plotly_dark') 
    fig.update_layout(
        template='plotly_dark',  # Puedes cambiar esto a otro tema predefinido
        paper_bgcolor="#FDFEFE ",# Establecer el fondo del papel a transparente
        plot_bgcolor='#82E0AA ',
        font=dict(
            family='Arial',  # Puedes cambiar la fuente según tus preferencias
            size=14,  # Tamaño del texto
            color='red'  # Color del texto
        ),
        title_text='% de valores nulos',  # Cambiar el texto del título
        title_font=dict(
            size=24,  # Tamaño del título
            color='black'  # Color del título
        )
    )
     # Cambiar al tema oscuro)  # Ajustar el rango del eje y # Cambiar al tema oscuro
    st.plotly_chart(fig)