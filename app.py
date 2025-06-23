
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Parámetros
largo_util = 120
ancho_util = 90
sobre_largo = 2.4
sobre_ancho = 4.5
largo_total = largo_util + sobre_largo * 2
ancho_total = ancho_util + sobre_ancho * 2

st.set_page_config(page_title="Plano Cancha Fútbol 11", layout="wide")
st.title("📐 Plano Cancha Fútbol 11 – Medidas y Sobrecancha")

# Crear imagen
fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(-10, largo_total + 10)
ax.set_ylim(-10, ancho_total + 10)

# Área total
ax.add_patch(patches.Rectangle((0, 0), largo_total, ancho_total, linewidth=2, edgecolor='black', facecolor='lightgreen'))

# Área útil
ax.add_patch(patches.Rectangle((sobre_largo, sobre_ancho), largo_util, ancho_util, linewidth=2, edgecolor='white', facecolor='none', linestyle='--'))

# Línea media y círculo
ax.plot([sobre_largo + largo_util / 2]*2, [sobre_ancho, sobre_ancho + ancho_util], color='white', linewidth=2)
circle = plt.Circle((sobre_largo + largo_util / 2, sobre_ancho + ancho_util / 2), 9.15, color='white', fill=False, linewidth=2)
ax.add_patch(circle)
ax.plot(sobre_largo + largo_util / 2, sobre_ancho + ancho_util / 2, 'wo', markersize=4)

# Áreas
for x in [sobre_largo, sobre_largo + largo_util - 16.5]:
    ax.add_patch(patches.Rectangle((x, sobre_ancho + (ancho_util - 40.3)/2), 16.5, 40.3, linewidth=2, edgecolor='white', facecolor='none'))
for x in [sobre_largo, sobre_largo + largo_util - 5.5]:
    ax.add_patch(patches.Rectangle((x, sobre_ancho + (ancho_util - 18.32)/2), 5.5, 18.32, linewidth=2, edgecolor='white', facecolor='none'))

# Puntos penales
ax.plot(sobre_largo + 11, sobre_ancho + ancho_util / 2, 'wo', markersize=3)
ax.plot(sobre_largo + largo_util - 11, sobre_ancho + ancho_util / 2, 'wo', markersize=3)

# Texto superior
ax.text(largo_total / 2, ancho_total + 5, f"LARGO CON SOBRECANCHA: {largo_total} m", ha='center', fontsize=11, weight='bold')
ax.text(largo_total / 2, -7, f"LARGO CANCHA: {largo_util} m", ha='center', fontsize=10)

# Texto lateral
ax.text(largo_total + 6, ancho_total / 2, f"ANCHO CON SOBRECANCHA: {ancho_total} m", va='center', rotation=270, fontsize=11, weight='bold')
ax.text(-8, ancho_total / 2, f"ANCHO CANCHA: {ancho_util} m", va='center', rotation=90, fontsize=10)

# Sobrecancha medida extra
ax.text(largo_total / 2, ancho_total + 9, f"SOBRECANCHA LARGO: {sobre_largo * 2} m", ha='center', fontsize=10, style='italic')
ax.text(largo_total + 10, ancho_total / 2, f"SOBRECANCHA ANCHO: {sobre_ancho * 2} m", va='center', rotation=270, fontsize=10, style='italic')

ax.set_title("Vista Reglamentaria de la Cancha con Medidas", fontsize=14, weight='bold')
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)
