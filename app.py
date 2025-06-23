
import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="Calculadora Cancha Fútbol 11", layout="wide")
st.title("⚽ Calculadora de Materiales – Cancha Fútbol V1")

# Entradas
st.sidebar.header("📏 Medidas de la Cancha")
largo_util = st.sidebar.number_input("Largo útil (m)", min_value=1.0, value=120.0)
ancho_util = st.sidebar.number_input("Ancho útil (m)", min_value=1.0, value=90.0)
sobre_largo = st.sidebar.number_input("Sobrecancha (largo) por lado (m)", min_value=0.0, value=2.4)
sobre_ancho = st.sidebar.number_input("Sobrecancha (ancho) por lado (m)", min_value=0.0, value=4.5)

# Cálculos
largo_total = largo_util + sobre_largo * 2
ancho_total = ancho_util + sobre_ancho * 2
area_total = largo_total * ancho_total
area_util = largo_util * ancho_util

# Pasto blanco
pasto_blanco = round(area_util * 0.014, 1)
rollos_blanco = math.floor(pasto_blanco / 84)
resto_blanco = pasto_blanco - (rollos_blanco * 84)
corte_blanco = f"{resto_blanco:.1f} m²" if resto_blanco > 0 else "No requiere"

# Pasto verde
pasto_verde = area_total - pasto_blanco
rollos_verde = math.floor(pasto_verde / 168)
resto_verde = pasto_verde - (rollos_verde * 168)
corte_verde = f"{resto_verde:.1f} m²" if resto_verde > 0 else "No requiere"

# Cinta y Pegamento
uniones_largo = math.floor(ancho_total / 4) - 1
uniones_ancho = math.floor(largo_total / 42) - 1
cinta_largo = uniones_largo * largo_total
cinta_ancho = uniones_ancho * ancho_total
cinta_total = cinta_largo + cinta_ancho
baldes_mapei = math.ceil(cinta_total / 20)

# Relleno
arena_std = round(area_total * 32, 1)
caucho_std = round(area_total * 7, 1)
arena_fifa = round(area_total * 12, 1)
caucho_fifa = round(area_total * 14, 1)

# Presentación visual
with st.container():
    st.header("🧾 Detalle de Cálculo por Ítem")

    with st.expander("📌 Área Total y Útil"):
        st.markdown(f"- Área útil (sin sobrecancha): **{area_util:.1f} m²**")
        st.markdown(f"- Área total (con sobrecancha): **{area_total:.1f} m²**")

    with st.expander("🟦 Pasto Blanco – Líneas de Cancha"):
        st.markdown(f"- Total requerido: **{pasto_blanco:.1f} m²**")
        st.markdown(f"- Rollos de 2x42 m (84 m²): **{rollos_blanco}**")
        st.markdown(f"- Corte adicional: **{corte_blanco}**")

    with st.expander("🟩 Pasto Verde – Área Resto de la Cancha"):
        st.markdown(f"- Total requerido: **{pasto_verde:.1f} m²**")
        st.markdown(f"- Rollos de 4x42 m (168 m²): **{rollos_verde}**")
        st.markdown(f"- Corte adicional: **{corte_verde}**")

    with st.expander("🔗 Cinta Mayland"):
        st.markdown(f"- Total requerido: **{cinta_total:.1f} m**")

    with st.expander("🧪 Pegamento Mapei"):
        st.markdown(f"- Baldes de 10 kg requeridos: **{baldes_mapei} baldes**")

    with st.expander("🌋 Relleno Estándar"):
        st.markdown(f"- Arena Sílice: **{arena_std} kg**")
        st.markdown(f"- Caucho Granulado: **{caucho_std} kg**")

    with st.expander("🌋 Relleno FIFA"):
        st.markdown(f"- Arena Sílice: **{arena_fifa} kg**")
        st.markdown(f"- Caucho Granulado: **{caucho_fifa} kg**")

    with st.expander("🥅 Arcos"):
        st.markdown("- **2 unidades reglamentarias** incluidas por defecto")

# Vista gráfica con etiquetas corregidas
st.header("📐 Vista Esquemática de la Cancha")

def dibujar_cancha_reglamentaria():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, largo_total)
    ax.set_ylim(0, ancho_total)

    ax.add_patch(patches.Rectangle((0, 0), largo_total, ancho_total, linewidth=2, edgecolor='black', facecolor='lightgreen'))
    ax.add_patch(patches.Rectangle((sobre_largo, sobre_ancho), largo_util, ancho_util, linewidth=2.5, edgecolor='white', facecolor='none', linestyle='--'))

    ax.plot([sobre_largo + largo_util / 2, sobre_largo + largo_util / 2], [sobre_ancho, sobre_ancho + ancho_util], color='white', linewidth=2)
    circle = plt.Circle((sobre_largo + largo_util / 2, sobre_ancho + ancho_util / 2), 9.15, color='white', fill=False, linewidth=2)
    ax.add_patch(circle)

    area_largo = 16.5
    area_ancho = 40.3

    ax.add_patch(patches.Rectangle((sobre_largo, sobre_ancho + (ancho_util - area_ancho) / 2), area_largo, area_ancho, linewidth=2, edgecolor='white', facecolor='none'))
    ax.add_patch(patches.Rectangle((sobre_largo + largo_util - area_largo, sobre_ancho + (ancho_util - area_ancho) / 2), area_largo, area_ancho, linewidth=2, edgecolor='white', facecolor='none'))

    ax.plot(sobre_largo + 11, sobre_ancho + ancho_util / 2, 'wo')
    ax.plot(sobre_largo + largo_util - 11, sobre_ancho + ancho_util / 2, 'wo')

    ax.text(largo_total / 2, -3, f"Largo cancha útil: {largo_util} m", ha='center', va='top', fontsize=10)
    ax.text(largo_total / 2, -6, f"Largo con sobrecancha: {largo_total} m", ha='center', va='top', fontsize=10)

    ax.text(-5, ancho_total / 2, f"Ancho cancha útil: {ancho_util} m", ha='left', va='center', fontsize=10, rotation=90)
    ax.text(-9, ancho_total / 2, f"Ancho con sobrecancha: {ancho_total} m", ha='left', va='center', fontsize=10, rotation=90)

    # ax.set_title("Vista esquemática reglamentaria de la cancha", fontsize=14)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.tight_layout()
    st.pyplot(fig)

dibujar_cancha_reglamentaria()
