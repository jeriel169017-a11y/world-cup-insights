# ⚽ World Cup Insights

Sistema para el análisis histórico de los partidos de la Copa Mundial de la FIFA utilizando **Python**, **Programación Orientada a Objetos (POO)**, **Pandas**, **Matplotlib** y **Streamlit**.

---

# 📌 Descripción

El proyecto descarga automáticamente el histórico de partidos de la Copa Mundial de la FIFA, realiza un análisis exploratorio de datos (EDA), genera estadísticas descriptivas, crea visualizaciones y presenta la información mediante un dashboard interactivo desarrollado con Streamlit.

---

# 🚀 Tecnologías utilizadas

- Python 3
- Pandas
- Matplotlib
- Streamlit
- Git
- GitHub
- Jupyter Notebook

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

# 📊 Funcionalidades

- Descarga automática del conjunto de datos.
- Filtrado exclusivo de partidos de la Copa Mundial.
- Estadísticas generales.
- Análisis exploratorio de datos (EDA).
- Limpieza y procesamiento de datos.
- Exportación de datos procesados.
- Visualización mediante gráficos.
- Dashboard interactivo con Streamlit.

---

# ▶️ Ejecución

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar el proyecto

```bash
python main.py
```

## Ejecutar el Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📒 Notebooks

El proyecto incluye dos notebooks:

- **01_EDA.ipynb**: análisis exploratorio de datos.
- **02_Visualizacion.ipynb**: generación de gráficos.

---

# 👤 Autor

**Jeriel Fonseca**

---

# 📄 Licencia

Proyecto desarrollado con fines académicos.