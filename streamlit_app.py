import streamlit as st
import requests

st.title("📡 Conexión Streamlit → Make con Webhook")

with st.form("my_form"):
    st.write("Agendar Cita.")
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo Electronico")
    motivo = st.text_area("Motivo")
    fecha = st.date_input("Dia")
    hora = st.time_input("Hora")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        data = { "Nombre": nombre,
                "Correo": correo,
                "Motivo": motivo,
                "Fecha": fecha,
                "Hora": hora }
        url = "https://hook.eu2.make.com/s5klmux6w3w21ewees4d9nxio81lt644"  # ← reemplaza con tu URL real
        response = requests.post(url, json=data)

        if response.status_code == 200:
            st.success("✅ Mensaje enviado a Make.")
            st.subheader("Agendado. Revise su correo de confirmacion.")
        else:
            st.error("❌ Error al enviar los datos.")
    else:
        st.warning("⚠️ Escribe un mensaje antes de enviarlo.")
