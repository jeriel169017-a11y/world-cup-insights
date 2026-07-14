# ⚽ World Cup Insights

Sistema para el análisis histórico de los partidos de la **Copa Mundial de la FIFA**, desarrollado en **Python** utilizando **Programación Orientada a Objetos (POO)**, **Pandas**, **Matplotlib**, **Jupyter Notebook** y **Streamlit**.

El proyecto permite descargar automáticamente el conjunto de datos, realizar un análisis exploratorio (EDA), generar estadísticas descriptivas, visualizar información mediante gráficos y consultar los datos a través de un dashboard interactivo.

---

# 📖 Tabla de contenido

- [Descripción](#-descripción)
- [Objetivos](#-objetivos)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Arquitectura del proyecto](#-arquitectura-del-proyecto)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Funcionalidades](#-funcionalidades)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Dashboard](#-dashboard)
- [Jupyter Notebooks](#-jupyter-notebooks)
- [Resultados obtenidos](#-resultados-obtenidos)
- [Mejoras futuras](#-mejoras-futuras)
- [Autor](#-autor)

---

# 📌 Descripción

World Cup Insights es una aplicación desarrollada para analizar el historial de partidos de la Copa Mundial de la FIFA.

El sistema descarga automáticamente el conjunto de datos desde GitHub, filtra únicamente los partidos del Mundial y permite realizar consultas, generar estadísticas, visualizar información y explorar los datos mediante un dashboard interactivo desarrollado con Streamlit.

Este proyecto integra conceptos de:

- Programación Orientada a Objetos
- Manipulación de datos con Pandas
- Análisis Exploratorio de Datos (EDA)
- Visualización de datos
- Desarrollo de dashboards
- Control de versiones con Git y GitHub

---

# 🎯 Objetivos

## Objetivo general

Desarrollar un sistema que permita analizar los partidos históricos de la Copa Mundial de la FIFA utilizando herramientas de análisis de datos en Python.

## Objetivos específicos

- Descargar automáticamente el conjunto de datos.
- Filtrar únicamente los partidos oficiales del Mundial.
- Implementar consultas mediante Programación Orientada a Objetos.
- Realizar un análisis exploratorio de datos (EDA).
- Generar estadísticas descriptivas.
- Visualizar información mediante gráficos.
- Desarrollar un dashboard interactivo con Streamlit.
- Documentar el proyecto utilizando GitHub.

---

# 🛠 Tecnologías utilizadas

- Python 3
- Pandas
- Matplotlib
- Streamlit
- Jupyter Notebook
- Git
- GitHub

---

# 🏗 Arquitectura del proyecto

El proyecto está organizado siguiendo una arquitectura modular basada en clases.

```text
CargadorDatos
        │
        ▼
GestorPartidos
        │
        ▼
ProcesadorEDA
        │
        ▼
Visualizador
        │
        ▼
Dashboard Streamlit
```

Cada clase tiene una responsabilidad específica, facilitando el mantenimiento y la reutilización del código.

---

# 📂 Estructura del proyecto

```text
world_cup_insights/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── partidos-mundial.csv
│   └── processed/
│       └── partidos_procesados.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Visualizacion.ipynb
│
├── src/
│   ├── eda/
│   ├── gestor/
│   ├── helpers/
│   ├── ingesta/
│   └── visualizacion/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📁 Organización del código

| Carpeta | Descripción |
|----------|-------------|
| **dashboard** | Dashboard interactivo desarrollado con Streamlit. |
| **data/raw** | Datos originales descargados automáticamente. |
| **data/processed** | Datos procesados generados por el sistema. |
| **notebooks** | Desarrollo del análisis exploratorio y visualizaciones. |
| **src/ingesta** | Descarga y almacenamiento de datos. |
| **src/gestor** | Consultas y operaciones sobre el DataFrame. |
| **src/eda** | Procesamiento y análisis exploratorio de datos. |
| **src/visualizacion** | Generación de gráficos. |
| **src/helpers** | Funciones auxiliares reutilizables. |

---

# 📈 Funcionalidades

El sistema permite:

- ✅ Descargar automáticamente el conjunto de datos.
- ✅ Filtrar únicamente partidos de la Copa Mundial.
- ✅ Consultar estadísticas generales.
- ✅ Obtener el total de partidos.
- ✅ Consultar selecciones participantes.
- ✅ Calcular el promedio de goles por partido.
- ✅ Analizar partidos por selección.
- ✅ Analizar partidos por edición del Mundial.
- ✅ Identificar sedes del torneo.
- ✅ Realizar limpieza de datos.
- ✅ Detectar valores faltantes.
- ✅ Generar estadísticas descriptivas.
- ✅ Crear una columna con el total de goles.
- ✅ Exportar los datos procesados.
- ✅ Visualizar información mediante gráficos.
- ✅ Consultar información desde un dashboard interactivo.

---

# ⚙ Instalación

Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

# ▶ Ejecución

Ejecutar la aplicación principal:

```bash
python main.py
```

Ejecutar el dashboard:

```bash
streamlit run dashboard/app.py
```

---

# 📊 Dashboard

El dashboard desarrollado con Streamlit permite consultar la información de manera interactiva.

Entre sus funcionalidades se encuentran:

- Estadísticas generales.
- Cantidad total de partidos.
- Número de selecciones participantes.
- Promedio de goles.
- Filtro por edición del Mundial.
- Filtro por país sede.
- Filtro por selección.
- Visualización de los partidos correspondientes.

---

# 📒 Jupyter Notebooks

El proyecto incluye dos notebooks para el desarrollo y presentación del análisis.

### 01_EDA.ipynb

Incluye:

- Descarga de datos.
- Exploración del conjunto de datos.
- Estadísticas descriptivas.
- Limpieza de datos.
- Detección de valores faltantes.

### 02_Visualizacion.ipynb

Incluye:

- Generación de gráficos.
- Visualización de estadísticas.
- Representación de resultados.

---

# 📊 Resultados obtenidos

Durante el desarrollo del proyecto fue posible:

- Descargar automáticamente el conjunto de datos.
- Procesar la información del Mundial.
- Generar estadísticas descriptivas.
- Visualizar el rendimiento histórico de las selecciones.
- Crear un dashboard interactivo.
- Exportar los datos procesados para futuros análisis.

---

# 🚀 Mejoras futuras

Como trabajo futuro podrían incorporarse nuevas funcionalidades, por ejemplo:

- Comparación entre dos selecciones.
- Estadísticas por jugador.
- Más gráficos interactivos.
- Exportación de reportes en PDF.
- Despliegue del dashboard en Streamlit Cloud.
- Incorporación de filtros avanzados.

---

# 👤 Autor

**Jeriel Fonseca**

Proyecto desarrollado con fines académicos como parte del curso de análisis de datos utilizando Python.

---

# 📄 Licencia

Este proyecto fue desarrollado con fines educativos.

El conjunto de datos utilizado corresponde al historial de resultados internacionales de fútbol publicado por la comunidad de GitHub.