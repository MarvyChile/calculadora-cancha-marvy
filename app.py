
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(layout="wide")

st.sidebar.title("Configuración de la Cancha")

# Inputs de medidas
largo_cancha = st.sidebar.number_input("Largo de la cancha (m)", min_value=10.0, value=120.0)
ancho_cancha = st.sidebar.number_input("Ancho de la cancha (m)", min_value=10.0, value=90.0)
sobre_largo = st.sidebar.number_input("Sobrecancha largo (m)", min_value=0.0, value=2.4)
sobre_ancho = st.sidebar.number_input("Sobrecancha ancho (m)", min_value=0.0, value=4.5)

# Cálculos
largo_total = largo_cancha + 2 * sobre_largo
ancho_total = ancho_cancha + 2 * sobre_ancho

# Visualización
st.subheader("Visualización de la Cancha")

fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, largo_total)
ax.set_ylim(0, ancho_total)

# Dibujar la sobrecancha (área total)
total_rect = patches.Rectangle((0, 0), largo_total, ancho_total, linewidth=2, edgecolor='black', facecolor='#90ee90')
ax.add_patch(total_rect)

# Dibujar el área útil (cancha)
util_rect = patches.Rectangle((sobre_largo, sobre_ancho), largo_cancha, ancho_cancha, 
                               linewidth=2, edgecolor='white', linestyle='--', facecolor='none')
ax.add_patch(util_rect)

# Líneas de cancha básicas
# Línea central
ax.plot([sobre_largo + largo_cancha / 2, sobre_largo + largo_cancha / 2], 
        [sobre_ancho, sobre_ancho + ancho_cancha], color='white', linewidth=2)

# Círculo central
circle = plt.Circle((sobre_largo + largo_cancha / 2, sobre_ancho + ancho_cancha / 2), 9.15, color='white', fill=False, linewidth=2)
ax.add_patch(circle)

# Área de gol (simplificada)
ax.add_patch(patches.Rectangle((sobre_largo, sobre_ancho + (ancho_cancha / 2) - 16.5), 5.5, 33, 
                               linewidth=2, edgecolor='white', facecolor='none'))

# Punto penal
ax.plot(sobre_largo + 11, sobre_ancho + ancho_cancha / 2, 'wo')

# Texto de medidas
ax.text(largo_total / 2, -2, f"Largo útil: {largo_cancha} m", ha='center', fontsize=10, color='white')
ax.text(largo_total / 2, ancho_total + 2, f"LARGO TOTAL: {largo_total} m", ha='center', fontsize=11, weight='bold')
ax.text(-2, ancho_total / 2 + 5, f"Ancho útil: {ancho_cancha} m", va='center', rotation='vertical', fontsize=10, color='white')
ax.text(largo_total + 1, ancho_total / 2 + 5, f"ANCHO TOTAL: {ancho_total} m", va='center', rotation='vertical', fontsize=11, weight='bold')

# Remover ejes
ax.axis('off')
st.pyplot(fig)
