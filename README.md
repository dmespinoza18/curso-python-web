# Curso Interactivo de Python (Web App)

Esta es una aplicación web interactiva creada con **Streamlit**, que enseña Python de forma visual y accesible.

Cada capítulo incluye:
- 📖 Texto narrado automáticamente
- 💻 Ejemplo de código Python
- 🖼️ Imagen visual generada automáticamente
- 🔊 Reproductor de audio (voz natural con gTTS)

---

## 🚀 ¿Cómo usar?

### 1. Clona el repositorio o descarga los archivos

```bash
git clone https://github.com/tuusuario/curso-python-web.git
cd curso-python-web
```

### 2. Instala dependencias

```bash
pip install streamlit gTTS pillow
```

### 3. Ejecuta localmente

```bash
streamlit run app_web_autogen.py
```

---

## 📁 Estructura esperada

```
curso-python-web/
├── app_web_autogen.py
├── README.md
└── chapters/
    ├── capitulo_1/
    │   └── texto.txt
    ├── capitulo_2/
    │   └── texto.txt
    └── ...
```

> Solo necesitas `texto.txt`, lo demás se genera automáticamente (`codigo.py`, `imagen.png`, `audio.mp3`).

---

## ☁️ Publicar en Streamlit Cloud

1. Crea una cuenta en [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Sube este repositorio a GitHub (público o privado con acceso)
3. En Streamlit Cloud, haz clic en “New app” y selecciona:
   - Repositorio: `tuusuario/curso-python-web`
   - Branch: `main`
   - File: `app_web_autogen.py`
4. Haz clic en **Deploy**

¡Tu curso Python estará disponible en línea!

---

## ✨ Autor

Creado por [Tu Nombre o Usuario] — proyecto educativo para enseñar Python paso a paso.
