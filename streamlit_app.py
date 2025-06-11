import streamlit as st
import requests
from datetime import datetime

st.title("📡 Conexión Streamlit → Make con Webhook")

Agendador, Presentador = st.tabs(["Agendador", "Presentaciones"])

with Agendador:
    with st.form("my_form"):
        st.subheader("Agendar Cita.")

        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo Electrónico")
        motivo = st.text_area("Motivo")
        fecha = st.date_input("Día")
        hora = st.time_input("Hora")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not all([nombre, correo, motivo]):
                st.warning("⚠️ Todos los campos son obligatorios.")
            else:
                # Combinar fecha y hora como string (opcional si quieres enviar juntos)
                fecha_str = fecha.strftime("%Y-%m-%d")
                hora_str = hora.strftime("%H:%M")

                data = {
                "nombre": nombre,
                "correo": correo,
                "motivo": motivo,
                "fecha": fecha_str,
                "hora": hora_str
                }

                url = "https://hook.eu2.make.com/s5klmux6w3w21ewees4d9nxio81lt644"  # Reemplaza con tu URL real
                try:
                    response = requests.post(url, json=data)

                    if response.status_code == 200:
                        st.success("✅ Mensaje enviado a Make.")
                        st.subheader("📩 Cita agendada. Revisa tu correo de confirmación.")
                    else:
                        st.error(f"❌ Error al enviar los datos. Código: {response.status_code}")
                except Exception as e:
                    st.error(f"❌ Error de conexión: {e}")
with Presentador:
    st.subheader("Generar Presentacion")
