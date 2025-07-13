import os
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS

# Configurar paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

st.set_page_config(page_title="Curso Interactivo de Python", layout="centered")
st.title("📘 Curso Interactivo de Python")

# Cargar capítulos disponibles
def obtener_capitulos():
    if not os.path.exists(CHAPTERS_DIR):
        return []
    return sorted([d for d in os.listdir(CHAPTERS_DIR) if os.path.isdir(os.path.join(CHAPTERS_DIR, d))])

# Generar código si falta
def generar_codigo(path):
    ejemplo = '# Ejemplo básico en Python\nprint("Hola, mundo!")\n'
    with open(path, "w", encoding="utf-8") as f:
        f.write(ejemplo)

# Generar imagen si falta
def generar_imagen(path, titulo="Python Visual"):
    img = Image.new("RGB", (600, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()
    draw.text((40, 120), titulo, fill=(0, 0, 0), font=font)
    img.save(path)

# Cargar contenido del capítulo
def cargar_contenido(capitulo):
    ruta = os.path.join(CHAPTERS_DIR, capitulo)
    texto_path = os.path.join(ruta, "texto.txt")
    codigo_path = os.path.join(ruta, "codigo.py")
    imagen_path = os.path.join(ruta, "imagen.png")
    audio_path = os.path.join(ruta, "audio.mp3")

    contenido = {"texto": "", "codigo": "", "imagen": None, "audio": None}

    if os.path.exists(texto_path):
        with open(texto_path, "r", encoding="utf-8") as f:
            contenido["texto"] = f.read()

    if contenido["texto"]:
        if not os.path.exists(codigo_path):
            generar_codigo(codigo_path)
        if not os.path.exists(imagen_path):
            generar_imagen(imagen_path, capitulo.replace("_", " ").title())
        if not os.path.exists(audio_path):
            tts = gTTS(contenido["texto"], lang="es")
            tts.save(audio_path)

    if os.path.exists(codigo_path):
        with open(codigo_path, "r", encoding="utf-8") as f:
            contenido["codigo"] = f.read()

    if os.path.exists(imagen_path):
        contenido["imagen"] = imagen_path

    if os.path.exists(audio_path):
        contenido["audio"] = audio_path

    return contenido

# Interfaz
capitulos = obtener_capitulos()
if not capitulos:
    st.warning("No se encontraron capítulos. Crea la carpeta /chapters/capitulo_1/ con texto.txt.")
else:
    seleccionado = st.selectbox("Selecciona un capítulo:", capitulos)
    contenido = cargar_contenido(seleccionado)

    st.subheader("📖 Texto del capítulo")
    st.write(contenido["texto"])

    if contenido["codigo"]:
        st.subheader("💻 Código de ejemplo")
        st.code(contenido["codigo"], language="python")

    if contenido["imagen"]:
        st.subheader("🖼️ Imagen visual")
        st.image(Image.open(contenido["imagen"]), use_column_width=True)

    if contenido["audio"]:
        st.subheader("🔊 Narración automática")
        with open(contenido["audio"], "rb") as f:
            st.audio(f.read(), format="audio/mp3")
