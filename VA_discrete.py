import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import streamlit as st
import seaborn as sns
sns.set(style="darkgrid")

def pmf_binomial(k, n, p):
    return binom.pmf(k, n, p)

def plot_pmf(n, p):
    x = np.arange(0, n+1)
    y = pmf_binomial(x, n, p)

    plot=sns.barplot(x=x, y=y,color='#87CEEB', alpha=0.8)
    plt.title('Función de Masa de Probabilidad (Distribución Binomial)')
    plt.xlabel('Número de Caras')
    plt.ylabel('Probabilidad')
    st.pyplot(plot.get_figure())

# Función de probabilidad acumulada binomial
def cdf_binomial(x, n, p):
    cdf = [binom.cdf(i, n, p) for i in range(x + 1)]
    return cdf

# Función para trazar la función de probabilidad acumulada
def plot_cdf(n, p):
    x_max = n  # Valor máximo para el deslizador
    x_values = np.arange(0, x_max + 1)
    y_values = cdf_binomial(x_max, n, p)
     # Crear una figura de Matplotlib
    fig, ax = plt.subplots()

    # Personalización del gráfico de línea con Matplotlib
    ax.step(x_values, y_values, marker='o', where='post', linestyle='-')
    ax.set_title('Función de Probabilidad Acumulada (Distribución Binomial)')
    ax.set_xlabel('Número de caras')
    ax.set_ylabel('Probabilidad Acumulada')
    ax.grid(True)
   
   

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)