import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from src.ingesta.cargador_datos import CargadorDatos
from src.gestor.gestor_partidos import GestorPartidos

# -------------------------------
# Configuración
# -------------------------------
st.set_page_config(
    page_title="World Cup Insights",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ World Cup Insights Dashboard")

st.markdown(
    """
### 📊 Análisis histórico de la Copa Mundial de la FIFA

Este dashboard permite explorar los partidos históricos de la Copa Mundial mediante filtros interactivos y estadísticas descriptivas.
"""
)
st.write("Análisis histórico de la Copa Mundial de la FIFA")

# -------------------------------
# Cargar datos
# -------------------------------
cargador = CargadorDatos()
datos = cargador.descargar_datos()
datos_mundial = cargador.guardar_partidos_mundial(datos)

gestor = GestorPartidos(datos_mundial)
st.sidebar.title("⚙️ Filtros")

anio = st.sidebar.selectbox(
    "Seleccione un Mundial",
    sorted(datos_mundial["date"].str[:4].astype(int).unique())
)
pais = st.sidebar.selectbox(
    "Seleccione el país sede",
    sorted(datos_mundial["country"].unique())
)

# -------------------------------
# Indicadores
# -------------------------------
st.subheader("📊 Estadísticas generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Partidos",
        gestor.total_partidos()
    )

with col2:
    st.metric(
        "Selecciones",
        len(gestor.listar_equipos())
    )

with col3:
    st.metric(
        "Promedio de goles",
        round(gestor.promedio_goles_por_partido(), 2)
    )

# -------------------------------
# Selector de equipos
# -------------------------------
st.divider()

st.subheader("🌎 Consulta por selección")

equipos = sorted(gestor.listar_equipos())

equipo = st.selectbox(
    "Seleccione una selección:",
    equipos
)

partidos = gestor.get_por_equipo(equipo)

partidos = partidos[
    partidos["date"].str.startswith(str(anio))
]

partidos = partidos[
    partidos["country"] == pais
]

st.metric(
    "Partidos jugados",
    len(partidos)
)

st.dataframe(
    partidos[
        [
            "date",
            "home_team",
            "away_team",
            "home_score",
            "away_score"
        ]
    ],
    use_container_width=True
)
st.divider()

st.subheader("🏆 Top 10 selecciones con más victorias")

victorias = gestor.equipo_con_mas_victorias()

import pandas as pd

df_victorias = pd.DataFrame(
    victorias[:10],
    columns=["Selección", "Victorias"]
)

st.dataframe(
    df_victorias,
    use_container_width=True
)
st.bar_chart(
    df_victorias.set_index("Selección")
)