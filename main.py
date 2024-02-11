import streamlit as st
from  VA_discrete import plot_pmf
from VA_discrete import plot_cdf
from VA_continous import histogram
import pandas as pd
from eda import plot_missing_values

# Obtener el conjunto de datos desde la fuente original
# Obtener el conjunto de datos desde la fuente original
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# Procesar el conjunto de datos correctamente
data = raw_df.values  # Utilizamos todos los datos
target = data[:, -1]  # La última columna es la variable objetivo
data = data[:, :-1]  # Excluimos la última columna, que es la variable objetivo

# Convertir a DataFrame para mayor comodidad (opcional)
column_names = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
]

# Asegurar que los datos y los nombres de las columnas coincidan
df = pd.DataFrame(data, columns=column_names[:data.shape[1]])
df["MEDV"] = target  # Añadir la variable objetivo al DataFrame

def main():
    st.title("Página Principal")

    # Botón para ir a la segunda página
    if st.button("Ir a la otra página"):
        # Establecer el valor de la variable de sesión para indicar la navegación a la otra página
        st.session_state.page = "second"
        # Recargar la aplicación para mostrar la segunda página
        st.experimental_rerun()

def second():
    st.title("Probability distributions")
    va = r"""
    $$\textbf{¿Que es una variable aleatoria?}$$
    
Una variable aleatoria es una función $$f : \Omega \rightarrow \mathbb{R}$$ que asigna un valor numérico a cada resultado posible de un experimento aleatorio. 
En otras palabras, es una variable cuyo valor depende del resultado de un evento aleatorio. 
La función de masa de probabilidad (PMF) o la función de densidad de probabilidad (PDF) describen la probabilidad asociada con 
cada posible valor que la variable aleatoria puede tomar.

Una variable aleatoria puede ser clasificada como discreta o continua. Una variable aleatoria discreta toma valores distintos y 
aislados, mientras que una variable aleatoria continua puede tomar cualquier valor dentro de un intervalo.

$$\textbf{Variable aleatoria discreta}$$

Ejemplo 1

Considera el lanzamiento de de una monera 3 veces.El espacio muestral del experimento es:

 $S$ = $\{CCC, CCX, CXC, XCC, CXX, XCX, XXC, XXX\}$ entonces nuestra variable aleatoria
 puede ser  $$X:$$numero de caras en en el lanzamiento de 3 monedas

 Entonces, para cada elemento en $$S$$, asignamos el número de caras correspondiente:
 $X(CCC)=3$  $X(CCX)=2$  $X(CXC)=2$  $X(XCC)=2$  $X(CXX)=1$   $X(XCX)=1$  $X(XXC)=1$  $X(XXX)=0$

Por lo tanto, la variable aleatoria  $X$ toma valores en el conjunto $\{0,1,2,3\}$


El grado de incertidumbre  de los valores que toma  uan variable aleatoria no es el mismo,existen
 algunos valores que ocurren con más frecuentemente  que otros.Es por esto que es necesario cuantificar la incertidumbre mediante 
 la $\textbf{función de probabilidad}$


 $\textbf{Soporte de una v.a}$
 

 Formalmente al conjunto de valores  que hacen que la 'densidad'(esto es,la probabilidad)
 de la v.a sea positiva se le denomina SOPORTE.Si la v.a se llama $X$,entonces sus soporte se denota como $S_X$
  

 $\textbf{Función masa de probabilidad (PMF)}$

 La función $f_x : S_x \rightarrow \mathbb{R}$,tal que $f_x(x)= \mathbb{P}(X=x)$,para todo $x \in S_x$,
 se dice   $\textbf{Función masa de probabilidad (PMF)}$ de la variable aleatoria $X$

 Propiedades
 - $f_X(x)\ge0$    $\forall$   $x$   $\in$   $S_x$

 - $\sum_{x} f_X(x)=1$

 Tambien la forma en la que  la probabilidad se distribuye a lo largo de todos los posibles valores del
 $S$ de  la variable aleatoria $X$ sigue un patron.

 Sigamos con el ejemplo 1,donde la v.a es $X$: numer de caras al lanzar 3 monedas.
 Supongamos que  quiero saber saber el numero de caras cuando lanzo $n$ veces una moneda,
 ¿Podria haber un unico modelo para reprsentar todas estas variables aleatorias?
 resulta que si y se llama $distribución $ $binomial$

 

"""

    va_1=""" PMF por sus siglas en ingles es simple,me sirve para asignar probabilidades.
    Pero como  yo calculo probabilidades del tipo '¿cual es la probabilidad de que salgan al menos 2 caras?
    o ¿cual es la probabilidad de que a lo mucho 2 caras?.Bien aqui entra en juego la funcion de distribución acumulada 
    que me cuantifica la incertibre  acumulada hasta un cierto valor del soporte $S_x$

   
   """


# Renderizar en Streamlit
    st.write(va)
    st.title('Visualización de la Función de Masa de Probabilidad')
    st.write('En el siguiente ejemplo tenemos la distribucion binomial,la cual a medida que variamos el numero de ensayos $n$ ,la cuantificación de la incertidumbre para cada valor del soporte $S_x$ cambia') 
    st.write(" Nuestra variable aleatoria discreta sera :$X$=numero de caras al lanzar una moneda $n$ veces") 
    n_lanzamientos = st.slider('Número de lanzamientos de la moneda (N)', 2, 100, 2)
# Probabilidad de obtener cara en un lanzamiento
    probabilidad_cara = st.slider('Probabilidad de obtener cara en un lanzamiento (p)', 0.0, 1.0, 0.5)
    plot_pmf(n_lanzamientos, probabilidad_cara)
    st.write(va_1)
    st.title('Visualización de la Función de Probabilidad Acumulada')
    n_ensayos = st.slider('Número total de ensayos (n)', 1, 100, 10)
    probabilidad_exito = st.slider('Probabilidad de éxito en un ensayo (p)', 0.0, 1.0, 0.5)
    # Visualización de la función de probabilidad acumulada
    plot_cdf(n_ensayos, probabilidad_exito)
    st.title('Distribución normal o  gaussiana')
    st.write("La distribución normal es ampliamente  utilizada para comprender  muchos  fenomenos naturales.Es un grafico  en forma de campana.Es una disposición  simetrica de un conjunto de datos en el que la mayoria de los valores se agrupan en la media y el resto se estrechan simétricamente hacia cualquier extremo")
    st.write("Comprendamos un ejemplo de la vida diaria que pueden seguir la curva normal")
    normal_ex=r"""
    La altura de las personas es un ejemplo  distribución normal.La mayoria de las personas en una población especifica son de
    estatura promedio.El numero de personas mas altas  y más cortas  que la altura promedio es casi igual,en otras
    palabras un numero muy pequeño de personas es muy alta o extremadamente baja.Varios factores genéticos y 
    ambientales influyen en la altura.
    """
    html_code = """
<iframe src="https://giphy.com/embed/AKnOEDShoxVICWuvFI" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<p><a href="https://giphy.com/gifs/elhormiguero-antena-3-el-hormiguero-atresmedia-AKnOEDShoxVICWuvFI"></a></p>
"""

# Renderizar HTML en Streamlit
    st.markdown(html_code, unsafe_allow_html=True)
    desc_p="""
    Entendamos mejor esto de la distribución normal con un ejempo:
    - Se llevó a cabo una exhaustiva encuesta en el estado de Puebla, México, donde se entrevistaron a mil personas de diversos municipios con el objetivo de obtener información precisa sobre sus estaturas. Este estudio proporcionará valiosos datos que nos permitirán comprender mejor la distribución de alturas en la población de la región y contribuirá a análisis más detallados sobre la salud y el bienestar de la comunidad
    """
    st.write(normal_ex)
    st.write(desc_p)
    histogram()
    st.write("Como podemos ver la distribución de los datos tiene forma de campana")
  
    st.write("Así que decides encuestar a 1000000 personas al azar (es decir escoges una muestra aleatoria) y miras el histograma de densidad de frecuencia. (Recuerda que el de densidad  de frecuencia significa que la suma de las áreas del histograma suma 1),no confundir con el grafico de densidad de probabilidad, ya que matematicamente  hablando no es lo mismo,estás obteniendo una representación visual suavizada de la distribución de tus datos, pero no estás calculando la verdadera densidad de probabilidad matemática")
    st.write("La pregunta aqui es ¿Hay alguna curva que se ajuste a mis datos?")
    st.write("Claro y es la la 'función de densidad', que  es precisamente ese contorno o linea continua que sea ajusta a mis datos ")
    st.write("¿Y para que sirve la  función de densidad?")
    f_density="""
    - Tener una teoría de la distribución de una variable numérica en una población
    - Calcular la probabilidad de ocurrencia entre 2 valores  $a$ y $b$ . El área debajo de la curva,que es la intregral de la PDF
    """
    st.write(f_density)
    st.write("Ademas cuando nos dicen que una variable aleatoria $X$ sigue una distribución normal es decir $X \sim \mathcal{N}(\mu, \sigma^2)$")
    st.write("Donde $\mu$ y $\sigma$ son los parametros  de la función de densidad estimados,podemos trazar la curva teorica(PDF).Algunas pruebas que se usan para saber si una variable aleatoria sigue una distrubución normal son :")
    pruebas_p="""
    - Prueba de Shapiro-Wilk
    - Prueba de Kolmogorov-Smirnov
    - Prueba de Lilliefors 
     entre otras 
    """
    st.write(pruebas_p)
    st.title('Descripción de distribuciones de probabilidad')
    desc_pro="""
    Valor esperado o esperanza matematica de una variable aleatoria discreta es la suma del producto de la probabilidad de cada suceso por el valor de dicho suceso.
    Los nombre de esperanza matemática y valor esperado tienen su origen en los juegos de azar y hacen referencia a la ganancia promedio esperada por un jugador cuando hace un gran número de apuestas.
    
    
    Ejemplo:
    Un jugador lanza dos monedas. Gana 1 ó 2 \$ si aparecen una o dos caras. Por otra parte pierde 5 \$ si no aparece cara. Determinar la esperanza matemática del juego y si éste es favorable.
    donde los resultados del experimento son $S$=$\{(c,c);(c,x);(x,c);(x,x)\}$.
    
    
    En este caso, la esperanza matemática $\mathbb{E}[X]$ epresenta el valor esperado que el jugador ganaría o perdería en promedio por cada juego. Si el valor es positivo, el juego sería favorable para el jugador; si es negativo, sería desfavorable.


    La fórmula para calcular la esperanza matemática(caso discreto) es $\mathbb{E}[X] = \sum_{i} x_i \cdot P(X = x_i)$
    donde $x_i$ son los posibles valores de la variable aleatoria  $X$ (en este caso, las ganancias o pérdidas)
    y $P(X=x_i)$ son las probabilidades asociadas a esos valores.


    En  este caso, los posibles valores de $X$ \: \{1,2,-5} con las siguientes probabilidades\:

    - $P(X=1)= 2/4$
    - $P(X=2)= 1/4$
    - $P(X=-5)= 1/4$


    $$E(X)$$ = $$(1)(2/4)$$ + $$(2)(1/4)$$ + $$(-5)(1/4)$$ = $$-1/4$$

    La interpretación es que, en promedio, el jugador perdería 0.25 por cada juego. Dado que la esperanza matemática es negativa, podemos decir que el juego es desfavorable para el jugador en el largo plazo. En otras palabras, en promedio, el jugador puede esperar perder dinero por cada juego repetido

 

    """
    st.write(desc_pro)
    st.title("Describiendo los datos")
    st.write("Usaremos un conjunto de datos de sklearn,en el cual tengo multiples variables")
    st.write(df.head())
    plot_missing_values(df)
    

    # Botón para volver a la primera página
    if st.button("main page return"):
        # Establecer el valor de la variable de sesión para indicar la vuelta a la primera página
        st.session_state.page = "main"
        # Recargar la aplicación para mostrar la primera página
        st.experimental_rerun()

# Inicializar la variable de sesión en la primera ejecución
if 'page' not in st.session_state:
    st.session_state.page = "main"

# Lógica para cambiar entre páginas
if st.session_state.page == "main":
    main()
elif st.session_state.page == "second":
    second()
