import streamlit as st
import pandas as pd
import altair as alt

# Configuración de la página
st.set_page_config(page_title="Crecimiento Económico en México", layout="wide")

# Estilos
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📊 Análisis del Crecimiento Económico en México </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #7D3C98;'>Created by Jesus Siqueiros</h4>", unsafe_allow_html=True)
st.markdown("---")

# Cargar datos
df = pd.read_csv("data/merged_activities.csv").astype({"Primaria": "float",
                                                       "Secundaria": "float",
                                                       "Terciaria": "float"})

# 📌 **1️⃣ Cargar y explorar datos**
st.subheader("📂 Datos Iniciales")
st.write("El siguiente código muestra cómo se cargaron los datos:")

st.code("""
import pandas as pd
# Cargar datos
data = pd.read_csv('data/merged_activities.csv')
# Mostrar las primeras filas
data.head(5)
""", language='python')

st.table(df.head(5))  # Muestra los datos en un formato interactivo

st.markdown("---")

# 📌 **2️⃣ Análisis de Actividad Primaria**
st.subheader("🌾 Desempeño por Estado en Actividades Primarias")
st.write("Las actividades primarias incluyen la agricultura, pesca y ganadería. A continuación, se muestran los estados con mayor participación en esta actividad:")

# Ordenar por actividad primaria
df_sorted = df[["Estado", "Primaria"]].sort_values("Primaria", ascending=False).head(5)

st.code("""
# Ordenar por actividad primaria y mostrar el top 5
data[["Estado","Primaria"]].sort_values("Primaria", ascending=False).head(5)
""", language='python')

st.table(df_sorted)  # Mostrar tabla ordenada

# 📊 **Gráfica de Barras**
st.markdown("### 📈 Comparación Visual de Actividad Primaria por Estado")

# Ordenar correctamente para Altair
df_sorted_chart = df.sort_values("Primaria", ascending=True)

# Crear gráfico de barras
bar_chart = alt.Chart(df_sorted_chart).mark_bar(color="#2E86C1").encode(
    x=alt.X("Estado", sort=df_sorted_chart["Estado"].tolist(), title="Estado"),
    y=alt.Y("Primaria", title="Nivel de Actividad Primaria"),
    tooltip=["Estado", "Primaria"]
).properties(
    width=700,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

st.code("""
# Crear gráfico de barras en Altair
bar_chart = alt.Chart(df_sorted_chart).mark_bar(color="#2E86C1").encode(
    x=alt.X("Estado", sort=df_sorted_chart["Estado"].tolist(), title="Estado"),
    y=alt.Y("Primaria", title="Nivel de Actividad Primaria"),
    tooltip=["Estado", "Primaria"]
).properties(
    width=700,
    height=400
)
""", language='python')

st.markdown("---")

st.subheader("🪚 Desempeño por Estado en Actividades Secundaria")
st.write("Las actividades secundarias son aquellas que transforman la materia prima en productos. A continuación, se muestran los estados con mayor participación en este sector:")

# Ordenar por actividad primaria
df_sorted = df[["Estado", "Secundaria"]].sort_values("Secundaria", ascending=False).head(5)

st.code("""
# Ordenar por actividad primaria y mostrar el top 5
data[["Estado","Secundaria"]].sort_values("Primaria", ascending=False).head(5)
""", language='python')

st.table(df_sorted)  # Mostrar tabla ordenada

# 📊 **Gráfica de Barras**
st.markdown("### 📈 Comparación Visual de Actividad Secundaria por Estado")

# Ordenar correctamente para Altair
df_sorted_chart = df.sort_values("Secundaria", ascending=True)

# Crear gráfico de barras
bar_chart = alt.Chart(df_sorted_chart).mark_bar(color="#2E86C1").encode(
    x=alt.X("Estado", sort=df_sorted_chart["Estado"].tolist(), title="Estado"),
    y=alt.Y("Secundaria", title="Nivel de Actividad Secundaria"),
    tooltip=["Estado", "Secundaria"]
).properties(
    width=700,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

st.code("""
# Crear gráfico de barras en Altair
bar_chart = alt.Chart(df_sorted_chart).mark_bar(color="#2E86C1").encode(
    x=alt.X("Estado", sort=df_sorted_chart["Estado"].tolist(), title="Estado"),
    y=alt.Y("Secundaria", title="Nivel de Actividad Secundaria"),
    tooltip=["Estado", "Secundaria"]
).properties(
    width=700,
    height=400
)
""", language='python')

st.markdown("---")

st.subheader("💻 Desempeño por Estado en Actividades Terciarias")
st.write("Las actividades terciaras son todas aquellas donde se da el comercio y la prestacion de servicios tangibles e intangibles. A continuación, se muestran los estados con mayor participación en este sector:")

# Ordenar por actividad primaria
df_sorted = df[["Estado", "Terciaria"]].sort_values("Terciaria", ascending=False).head(5)

st.code("""
# Ordenar por actividad terciaria y mostrar el top 5
data[["Estado","Terciaria"]].sort_values("Terciaria", ascending=False).head(5)
""", language='python')

st.table(df_sorted)  # Mostrar tabla ordenada

# 📊 **Gráfica de Barras**
st.markdown("### 📈 Comparación Visual de Actividad Terciaria por Estado")

# Ordenar correctamente para Altair
df_sorted_chart = df.sort_values("Terciaria", ascending=True)

# Crear gráfico de barras
bar_chart = alt.Chart(df_sorted_chart).mark_bar(color="#2E86C1").encode(
    x=alt.X("Estado", sort=df_sorted_chart["Estado"].tolist(), title="Estado"),
    y=alt.Y("Terciaria", title="Nivel de Actividad Terciaria"),
    tooltip=["Estado", "Terciaria"]
).properties(
    width=700,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

st.code("""
# Crear gráfico de barras en Altair
bar_chart = alt.Chart(df_sorted_chart).mark_bar(color="#2E86C1").encode(
    x=alt.X("Estado", sort=df_sorted_chart["Estado"].tolist(), title="Estado"),
    y=alt.Y("Terciaria", title="Nivel de Actividad Terciaria"),
    tooltip=["Estado", "Terciaria"]
).properties(
    width=700,
    height=400
)
""", language='python')

st.markdown("---")

