import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import numpy as np
import av
from io import BytesIO
from PIL import Image

st.title("Visualizador de Filtros em Imagens e Webcam")

# Seleção de múltiplos filtros
filtros_selecionados = st.multiselect(
    "Escolha os filtros para aplicar (na ordem):",
    ["grayscale", "invert", "blur", "sharpen", "canny"],
    format_func=lambda x: {
        "grayscale": "Cinza",
        "invert": "Inverter",
        "blur": "Desfoque",
        "sharpen": "Nitidez",
        "canny": "Borda"
    }[x]
)

# Função para aplicar os filtros selecionados
def aplicar_filtros(img, filtros):
    for filtro in filtros:
        if filtro == "blur":
            img = cv2.GaussianBlur(img, (21, 21), 0)
        elif filtro == "canny":
            img = cv2.Canny(img, 100, 200)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif filtro == "grayscale":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif filtro == "invert":
            img = cv2.bitwise_not(img)
        elif filtro == "sharpen":
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            img = cv2.filter2D(img, -1, kernel)
    return img

# Escolha entre webcam e imagem
modo = st.radio("Escolha o modo de entrada:", ("Webcam", "Upload de Imagem"))

# Modo Webcam
if modo == "Webcam":
    def video_frame_callback(frame):
        img = frame.to_ndarray(format="bgr24")
        img = aplicar_filtros(img, filtros_selecionados)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

    webrtc_streamer(
        key="webcam",
        video_frame_callback=video_frame_callback,
        sendback_audio=False
    )

# Modo Imagem
else:
    uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        img_filtrada = aplicar_filtros(img.copy(), filtros_selecionados)

        # Mostrar imagens lado a lado
        st.image(
            [cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
             cv2.cvtColor(img_filtrada, cv2.COLOR_BGR2RGB)],
            caption=["Original", "Filtrada"],
            width=300
        )

        # Salvar como imagem PNG e oferecer download
        img_pil = Image.fromarray(cv2.cvtColor(img_filtrada, cv2.COLOR_BGR2RGB))
        buffer = BytesIO()
        img_pil.save(buffer, format="PNG")
        buffer.seek(0)

        st.download_button(
            label="Baixar imagem filtrada",
            data=buffer,
            file_name="imagem_filtrada.png",
            mime="image/png"
        )
