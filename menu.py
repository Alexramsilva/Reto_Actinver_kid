# -*- coding: utf-8 -*-

import streamlit as st

# ==========================================
# CONFIGURACIÓN
# ==========================================

CLAVE_ACCESO = "Reto Actinver"   # <-- Cambia aquí la clave

# --- Personalización de diseño ---
st.markdown("""
<style>
    .stApp {
        background-color: #0B1220;
    }

    .css-1d391kg {
        color: #faf7f8;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# PANTALLA DE ACCESO
# ==========================================
st.markdown(
    '<h1 style="color:#FFFFFF;">🔐 Acceso</h1>',
    unsafe_allow_html=True
)

# st.title("🔐 Acceso")
st.markdown(
    '<h3 style="color:#FFFFFF;">Ingresa la clave de ingreso</h3>',
    unsafe_allow_html=True
)

clave = st.text_input(
    "",
    type="password"
)

if clave == CLAVE_ACCESO:

    st.success("Acceso autorizado")

    # ==========================================
    # MENÚ
    # ==========================================
    st.markdown(
    '<h1 style="color:#FFFFFF;">Menú de enlaces</h1>',
    unsafe_allow_html=True
    )

    # st.title("Menú de enlaces")

    links = {
        "App BMV (comprar o vender)": "https://appbmv-f9igvhnh5sc7wjax66ukjs.streamlit.app/",
        "Análisis Financiero": "https://retoactinver-7ugnxpfgupkdufnskngbvg.streamlit.app/",
        "Simulación Monte Carlo individual" : "https://dr42zwffvmeo7pls3snkuv.streamlit.app/",
        "Portafolio Óptimo" : "https://portafolio-optimo-otqmf2ztv3f99wlwlhjkew.streamlit.app/",
        "Simulación Monte Carlo (en grupo" : "https://simulmc-kq7fbvqbafqnateomyp8qp.streamlit.app/",
        
    }
    st.markdown(
    '<h3 style="color:#FFFFFF;">Selecciona una opción</h3>',
    unsafe_allow_html=True
    )
    opcion = st.selectbox(
        "",
        list(links.keys())
    )

    st.markdown(
        f"[▶️ Ir a: {opcion}]({links[opcion]})",
        unsafe_allow_html=True
    )

elif clave:
    st.error("❌ Clave incorrecta")
