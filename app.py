
import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="Calculadora Cancha Fútbol 11", layout="wide")

st.title("Calculadora de Materiales – Cancha Fútbol 11")

# Entradas del usuario
st.sidebar.header("Medidas de la Cancha")
largo_util = st.sidebar.number_input("Largo útil (m)", min_value=1.0, value=120.0)
ancho_util = st.sidebar.number_input("Ancho útil (m)", min_value=1.0, value=90.0)
sobre_largo = st.sidebar.number_input("Sobrecancha (largo) por lado (m)", min_value=0.0, value=2.4)
sobre_ancho = st.sidebar.number_input("Sobrecancha (ancho) por lado (m)", min_value=0.0, value=4.5)

# Cálculo de área
largo_total = largo_util + sobre_largo * 2
ancho_total = ancho_util + sobre_ancho * 2
area_total = largo_total * ancho_total
area_util = largo_util * ancho_util

# Pasto blanco (1,4% del área útil)
pasto_blanco = round(area_util * 0.014, 1)

# Rollos blanco (2x42 = 84 m²)
rollos_blanco = math.floor(pasto_blanco / 84)
resto_blanco = pasto_blanco - (rollos_blanco * 84)
corte_blanco = f"{resto_blanco:.1f} m²" if resto_blanco > 0 else "No requiere"

# Pasto verde
pasto_verde = area_total - pasto_blanco
rollos_verde = math.floor(pasto_verde / 168)
resto_verde = pasto_verde - (rollos_verde * 168)
corte_verde = f"{resto_verde:.1f} m²" if resto_verde > 0 else "No requiere"

# Cinta Mayland
uniones_largo = math.floor(ancho_total / 4) - 1
uniones_ancho = math.floor(largo_total / 42) - 1
cinta_largo = uniones_largo * largo_total
cinta_ancho = uniones_ancho * ancho_total
cinta_total = cinta_largo + cinta_ancho

# Pegamento
baldes_mapei = math.ceil(cinta_total / 20)

# Rellenos
arena_std = round(area_total * 32, 1)
caucho_std = round(area_total * 7, 1)
arena_fifa = round(area_total * 12, 1)
caucho_fifa = round(area_total * 14, 1)

# Visualización del campo
def dibujar_cancha(largo, ancho, sobre_l, sobre_a):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, largo)
    ax.set_ylim(0, ancho)

    cancha_total = patches.Rectangle((0, 0), largo, ancho, linewidth=1.5, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(cancha_total)

    cancha_util = patches.Rectangle((sobre_l, sobre_a), largo - 2 * sobre_l, ancho - 2 * sobre_a, linewidth=2, edgecolor='white', facecolor='none', linestyle='--')
    ax.add_patch(cancha_util)

    ax.set_title("Visualización de la Cancha")
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)

dibujar_cancha(largo_total, ancho_total, sobre_largo, sobre_ancho)

# Mostrar resultados
st.subheader("Resumen de Cálculo de Materiales")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"**Área útil:** {area_util:.1f} m²")
    st.markdown(f"**Área total:** {area_total:.1f} m²")
    st.markdown(f"**Pasto blanco requerido:** {pasto_blanco:.1f} m²")
    st.markdown(f"**Rollos blancos (2x42):** {rollos_blanco} rollos")
    st.markdown(f"**Corte adicional blanco:** {corte_blanco}")

with col2:
    st.markdown(f"**Pasto verde requerido:** {pasto_verde:.1f} m²")
    st.markdown(f"**Rollos verdes (4x42):** {rollos_verde} rollos")
    st.markdown(f"**Corte adicional verde:** {corte_verde}")
    st.markdown(f"**Cinta Mayland:** {cinta_total:.1f} m")
    st.markdown(f"**Baldes Mapei (10 kg):** {baldes_mapei} baldes")

st.subheader("Relleno Estándar")
st.markdown(f"- Arena Sílice: {arena_std} kg")
st.markdown(f"- Caucho Granulado: {caucho_std} kg")

st.subheader("Relleno FIFA")
st.markdown(f"- Arena Sílice: {arena_fifa} kg")
st.markdown(f"- Caucho Granulado: {caucho_fifa} kg")

st.subheader("Arcos")
st.markdown("2 unidades reglamentarias")
