import streamlit as st
import requests

st.title("🎯 Generador de Presentaciones")
st.write("Completa el siguiente formulario para generar automáticamente una presentación profesional en formato PDF.")
st.info("📄 La presentación generada tendrá **7 diapositivas** y se entregará en **formato PDF**.")

# Inicia una clave en session_state para guardar el PDF
if "pdf_data" not in st.session_state:
    st.session_state["pdf_data"] = None

with st.form("presentation_form"):
    titulo = st.text_input("Título de la presentación")
    autor = st.text_input("Autor de la Presentacion") # Añadir Autor
    tipo = st.selectbox("Tipo de presentación", ["Pitch", "Propuesta", "Investigativo"])
    objetivo = st.text_area("Objetivo del contenido", help="Describe brevemente qué deseas comunicar o lograr con la presentación.")
    audiencia = st.selectbox("Audiencia objetivo", ["Cliente", "Inversores", "Estudiantes", "Viewers"])
    estilo = st.selectbox("Estilo deseado", ["Formal", "Creativo", "Corporativo", "Minimalista"])
    idioma = st.selectbox("Idioma", ["Español", "Inglés"])
    ideas = st.text_area("Puntos clave o ideas principales", help="Enumera o describe los temas que debe incluir la presentación.")

    submit = st.form_submit_button("Generar y descargar PDF")

    if submit:
        payload = {
            "titulo": titulo,
            "Autor": autor,
            "tipo": tipo,
            "objetivo": objetivo,
            "audiencia": audiencia,
            "estilo": estilo,
            "idioma": idioma,
            "ideas": ideas,
        }

        try:
            with st.spinner("🛠️ Generando presentación..."):
                # URL del Webhook de Make.com
                response = requests.post("https://hook.eu2.make.com/ffs14tm3lqou5owigyec97iomsvqmc9u", json=payload)
                st.session_state["pdf_data"] = response.content
                
            if response.status_code == 200:
                st.success("✅ Tu presentación fue generada correctamente.")
            else:
                st.error(f"❌ Error al generar la presentación. Código: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Ocurrió un error al conectar con el servidor: {e}")
            
# Mostrar el botón de descarga si ya se recibió el PDF
if st.session_state["pdf_data"]:
    st.download_button(
        label="📥 Descargar presentación (PDF)",
        data=st.session_state["pdf_data"],
        file_name="presentacion_generada.pdf",
        mime="application/pdf"
    )
