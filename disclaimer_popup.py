import streamlit as st

# Función para mostrar el mensaje de advertencia
def show_disclaimer_popup():
    with st.popover("Open popover"):
        st.markdown("Hello World 👋")