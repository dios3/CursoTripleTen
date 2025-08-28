import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos",
                   page_icon="🚗", layout="wide")

# Título de la aplicación
st.title("Análisis de Datos de Vehículos")
st.header("Visualización de datos de anuncios de vehículos")

# Cargar datos


@st.cache_data
def load_data():
    try:
        data = pd.read_csv('vehicles_us.csv')
        return data
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo vehicles_us.csv")
        return None


car_data = load_data()

if car_data is not None:
    st.success("Datos cargados exitosamente!")
    st.write(f"Total de registros: {len(car_data)}")

    # Mostrar preview de datos
    if st.checkbox('Mostrar preview de datos'):
        st.write(car_data.head())

    # Sección de gráficos
    st.header("Visualizaciones")

    col1, col2 = st.columns(2)

    with col1:
        # Botón para histograma
        hist_button = st.button('Mostrar Histograma de Kilometraje')

        if hist_button:
            st.write('### Histograma del kilometraje de los vehículos')
            fig_hist = px.histogram(car_data,
                                    x="odometer",
                                    title="Distribución de Kilometraje",
                                    labels={'odometer': 'Kilometraje'},
                                    color_discrete_sequence=['#FF4B4B'])
            fig_hist.update_layout(bargap=0.1)
            st.plotly_chart(fig_hist, use_container_width=True)

    with col2:
        # Botón para gráfico de dispersión
        scatter_button = st.button(
            'Mostrar Gráfico de Dispersión Precio vs Kilometraje')

        if scatter_button:
            st.write('### Relación entre Precio y Kilometraje')
            fig_scatter = px.scatter(car_data,
                                     x="odometer",
                                     y="price",
                                     title="Precio vs Kilometraje",
                                     labels={'odometer': 'Kilometraje',
                                             'price': 'Precio'},
                                     color_discrete_sequence=['#00CC96'])
            st.plotly_chart(fig_scatter, use_container_width=True)

    # Opción con checkbox (extra)
    st.header("Controles Avanzados")

    build_histogram = st.checkbox('Mostrar histograma de kilometraje')
    build_scatter = st.checkbox(
        'Mostrar gráfico de dispersión precio vs kilometraje')

    if build_histogram:
        st.write('### Histograma del Kilometraje (Checkbox)')
        fig_hist = px.histogram(car_data,
                                x="odometer",
                                title="Distribución de Kilometraje",
                                labels={'odometer': 'Kilometraje'},
                                color_discrete_sequence=["#63FAFA"])
        st.plotly_chart(fig_hist, use_container_width=True)

    if build_scatter:
        st.write('### Precio vs Kilometraje (Checkbox)')
        fig_scatter = px.scatter(car_data,
                                 x="odometer",
                                 y="price",
                                 title="Precio vs Kilometraje",
                                 labels={'odometer': 'Kilometraje',
                                         'price': 'Precio'},
                                 color_discrete_sequence=['#FFA15A'])
        st.plotly_chart(fig_scatter, use_container_width=True)

else:
    st.error("Por favor, asegúrate de que el archivo vehicles_us.csv esté en el directorio del proyecto.")

# Información adicional
st.sidebar.header("Información")
st.sidebar.info("""
Esta aplicación permite visualizar datos de vehículos mediante:
- Histogramas de distribución
- Gráficos de dispersión
- Controles interactivos
""")
