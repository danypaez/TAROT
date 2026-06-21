import streamlit as st
from philosopher_ai import responder
from gtts import gTTS
import uuid
import os

# -------------------
# Configuración
# -------------------

st.set_page_config(
    page_title="Tarot Terapéutico",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Tarot Terapéutico y Espiritualidad Universal")

st.write(
    "Un espacio de reflexión, autoconocimiento y conexión con la energía creadora."
)

# -------------------
# Datos del usuario
# -------------------

nombre = st.text_input("Tu nombre")

mensaje = st.text_area(
    "¿Qué deseas compartir hoy?"
)

# -------------------
# Botón de consulta
# -------------------

if st.button("Consultar"):

    if not mensaje:

        st.warning(
            "Compartime aquello que sentís en este momento."
        )

    else:

        try:

            respuesta = responder(
                nombre,
                mensaje
            )

            st.markdown("### Reflexión")

            st.write(respuesta)

            # Generar audio

            os.makedirs("temp", exist_ok=True)

            archivo = f"temp/voz_{uuid.uuid4().hex}.mp3"

            tts = gTTS(
                text=respuesta,
                lang="es"
            )

            tts.save(archivo)

            with open(archivo, "rb") as audio:

                st.audio(
                    audio.read(),
                    format="audio/mp3"
                )

        except Exception as e:

            st.error(
                "En este momento no logro conectar con la reflexión universal."
            )

            st.write(e)
