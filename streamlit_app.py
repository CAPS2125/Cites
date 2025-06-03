import streamlit as st
import requests

st.title("📡 Conexión Streamlit → Make con Webhook")

mensaje = st.text_input("Escribe un mensaje para Make:")

if st.button("Enviar a Make"):
    if mensaje:
        data = {"mensaje": mensaje}
        url = "https://hook.eu2.make.com/s5klmux6w3w21ewees4d9nxio81lt644"  # ← reemplaza con tu URL real
        response = requests.post(url, json=data)

        if response.status_code == 200:
            st.success("✅ Mensaje enviado a Make.")
            st.write(response)
        else:
            st.error("❌ Error al enviar los datos.")
    else:
        st.warning("⚠️ Escribe un mensaje antes de enviarlo.")
