
import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Parámetros iniciales
st.set_page_config(page_title="Calculadora Cancha Fútbol 11", layout="wide")
st.title("⚽ Calculadora de Materiales – Cancha Fútbol 11")

# Entradas del usuario
st.sidebar.header("📏 Medidas de la Cancha")
largo_util = st.sidebar.number_input("Largo útil (m)", min_value=1.0, value=120.0)
ancho_util = st.sidebar.number_input("Ancho útil (m)", min_value=1.0, value=90.0)
sobre_largo = st.sidebar.number_input("Sobrecancha (largo) por lado (m)", min_value=0.0, value=2.4)
sobre_ancho = st.sidebar.number_input("Sobrecancha (ancho) por lado (m)", min_value=0.0, value=4.5)

# Cálculos generales
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

# Cinta Mayland y Pegamento
uniones_largo = math.floor(ancho_total / 4) - 1
uniones_ancho = math.floor(largo_total / 42) - 1
cinta_largo = uniones_largo * largo_total
cinta_ancho = uniones_ancho * ancho_total
cinta_total = cinta_largo + cinta_ancho
baldes_mapei = math.ceil(cinta_total / 20)

# Rellenos
arena_std = round(area_total * 32, 1)
caucho_std = round(area_total * 7, 1)
arena_fifa = round(area_total * 12, 1)
caucho_fifa = round(area_total * 14, 1)

# Resultados
st.header("🧾 Detalle de Cálculo por Ítem")
st.markdown(f"**Área útil:** {area_util:.1f} m²")
st.markdown(f"**Área total:** {area_total:.1f} m²")
st.markdown(f"**Pasto blanco requerido:** {pasto_blanco:.1f} m² – Rollos: {rollos_blanco} – Corte adicional: {corte_blanco}")
st.markdown(f"**Pasto verde requerido:** {pasto_verde:.1f} m² – Rollos: {rollos_verde} – Corte adicional: {corte_verde}")
st.markdown(f"**Cinta Mayland:** {cinta_total:.1f} m – **Baldes Mapei (10 kg):** {baldes_mapei}")
st.markdown(f"**Relleno Estándar:** Arena Sílice {arena_std} kg, Caucho {caucho_std} kg")
st.markdown(f"**Relleno FIFA:** Arena Sílice {arena_fifa} kg, Caucho {caucho_fifa} kg")
st.markdown("**Arcos:** 2 unidades reglamentarias")

# Visualización final con medidas, sin título
# Visualización de la Cancha con Medidas
st.header("📐 Visualización de la Cancha con Medidas")

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(-10, largo_total + 10)
ax.set_ylim(-10, ancho_total + 10)

# Área total y útil
ax.add_patch(patches.Rectangle((0, 0), largo_total, ancho_total, linewidth=2, edgecolor='black', facecolor='lightgreen'))
ax.add_patch(patches.Rectangle((sobre_largo, sobre_ancho), largo_util, ancho_util, linewidth=2, edgecolor='white', facecolor='none', linestyle='--'))

# Línea media, círculo, áreas y puntos penales
ax.plot([sobre_largo + largo_util / 2]*2, [sobre_ancho, sobre_ancho + ancho_util], color='white', linewidth=2)
circle = plt.Circle((sobre_largo + largo_util / 2, sobre_ancho + ancho_util / 2), 9.15, color='white', fill=False, linewidth=2)
ax.add_patch(circle)
ax.plot(sobre_largo + largo_util / 2, sobre_ancho + ancho_util / 2, 'wo', markersize=4)

for x in [sobre_largo, sobre_largo + largo_util - 16.5]:
    ax.add_patch(patches.Rectangle((x, sobre_ancho + (ancho_util - 40.3)/2), 16.5, 40.3, linewidth=2, edgecolor='white', facecolor='none'))
for x in [sobre_largo, sobre_largo + largo_util - 5.5]:
    ax.add_patch(patches.Rectangle((x, sobre_ancho + (ancho_util - 18.32)/2), 5.5, 18.32, linewidth=2, edgecolor='white', facecolor='none'))

ax.plot(sobre_largo + 11, sobre_ancho + ancho_util / 2, 'wo', markersize=3)
ax.plot(sobre_largo + largo_util - 11, sobre_ancho + ancho_util / 2, 'wo', markersize=3)

# Etiquetas fuera del campo
ax.text(largo_total / 2, ancho_total + 5, f"LARGO CON SOBRECANCHA: {largo_total} m", ha='center', fontsize=11, weight='bold')
ax.text(largo_total / 2, -7, f"LARGO CANCHA: {largo_util} m", ha='center', fontsize=10)
ax.text(largo_total + 6, ancho_total / 2, f"ANCHO CON SOBRECANCHA: {ancho_total} m", va='center', rotation=270, fontsize=11, weight='bold')
ax.text(-8, ancho_total / 2, f"ANCHO CANCHA: {ancho_util} m", va='center', rotation=90, fontsize=10)
ax.text(largo_total / 2, ancho_total + 9, f"SOBRECANCHA LARGO: {sobre_largo * 2} m", ha='center', fontsize=10, style='italic')
ax.text(largo_total + 10, ancho_total / 2, f"SOBRECANCHA ANCHO: {sobre_ancho * 2} m", va='center', rotation=270, fontsize=10, style='italic')

ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)
