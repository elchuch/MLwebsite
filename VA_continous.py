import numpy as np
import  seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import norm
def histogram():
    estaturas= np.random.normal(loc=165, scale=10, size=1000000)

# Configuración de estilo de seaborn
    sns.set(style="darkgrid")

# Graficar histograma de frecuencia con seaborn
    plt.figure(figsize=(8, 6))
    #s=sns.kdeplot(estaturas,color='skyblue')
     #Crear histograma de densidad de frecuencia
    s=sns.histplot(estaturas, bins='auto', stat='density', color='skyblue', edgecolor='black',kde=True)
    # Configurar el color del KDE
    s.get_lines()[0].set_color('red') 
    plt.title('Estaturas de comunidad Poblana')
    plt.xlabel('Estatura (cm)')
    plt.ylabel(' Densidad de frecuencia')
    plt.grid(axis='y')
    st.pyplot(s.get_figure())
