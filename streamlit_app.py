import streamlit as st
import requests

# URL del Webhook de Make.com
WEBHOOK_URL = "https://hook.us1.make.com/tu-webhook-url-aqui"

st.title("🎯 Generador de Presentaciones")

st.write("Completa el siguiente formulario para generar automáticamente una presentación profesional en formato PDF.")

st.info("📄 La presentación generada tendrá **7 diapositivas** y se entregará en **formato PDF**.")

with st.form("presentation_form"):
    titulo = st.text_input("Título de la presentación")
    tipo = st.selectbox("Tipo de presentación", ["Propuesta", "Informe", "Pitch", "Otro"])
    objetivo = st.text_area("Objetivo del contenido", help="Describe brevemente qué deseas comunicar o lograr con la presentación.")
    audiencia = st.selectbox("Audiencia objetivo", ["Cliente", "Inversores", "Gerencia", "Equipo interno", "Otro"])
    estilo = st.selectbox("Estilo deseado", ["Formal", "Creativo", "Corporativo", "Minimalista", "Otro"])
    idioma = st.selectbox("Idioma", ["Español", "Inglés", "Otro"])
    ideas = st.text_area("Puntos clave o ideas principales", help="Enumera o describe los temas que debe incluir la presentación.")

    submit = st.form_submit_button("Generar y descargar PDF")

    if submit:
        payload = {
            "titulo": titulo,
            "tipo": tipo,
            "objetivo": objetivo,
            "audiencia": audiencia,
            "estilo": estilo,
            "idioma": idioma,
            "ideas": ideas,
            "formato": "PDF",  # fijo
        }

        try:
            with st.spinner("🛠️ Generando presentación..."):
                response = requests.post(WEBHOOK_URL, json=payload)

            if response.status_code == 200:
                st.success("✅ Tu presentación fue generada correctamente.")
                st.download_button(
                    label="📥 Descargar presentación (PDF)",
                    data=response.content,
                    file_name="presentacion_generada.pdf",
                    mime="application/pdf"
                )
            else:
                st.error(f"❌ Error al generar la presentación. Código: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Ocurrió un error al conectar con el servidor: {e}")
