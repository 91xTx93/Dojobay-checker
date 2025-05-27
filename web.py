import streamlit as st
import subprocess
import re

st.title("Dojo Status")
st.write("A web app to check the satus of the dojos listed at [dojobay.pw](https://dojobay.pw).")

# Ejecutar el script allnew.py y mostrar la salida
try:
    result = subprocess.run(
        ["python3", "allnew.py"],
        capture_output=True, text=True, check=True
    )
    # Eliminar códigos de color ANSI
    clean_output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
    st.markdown(f"```text\n{clean_output}\n```", unsafe_allow_html=True)
except subprocess.CalledProcessError as e:
    st.error("Error al ejecutar allnew.py")
    st.code(e.stderr)