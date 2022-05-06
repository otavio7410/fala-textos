import cv2
import numpy as np
import pytesseract
from gtts import gTTS
from playsound import playsound
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def tratar_imagem(imagem):
    #redimensionando a imagem
    img_resize = cv2.resize(imagem, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    #deixando a imagem cinza
    img_cinza = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

    #muando a dilatação e erosão da imagem
    kernel = np.ones((1, 1), np.uint8)
    img_dilat = cv2.dilate(img_cinza, kernel, iterations=1)
    img_eroc = cv2.erode(img_dilat, kernel, iterations=1)

    #retornando arquivo final de imagem
    return img_eroc

def converter_imagem_texto(imagem_tratada):
    #convertendo imagem em texto
    texto = pytesseract.image_to_string(imagem_tratada, lang='por')
    return texto

def reporduzir_audio(texto):
    tts = gTTS(texto, lang="pt-br")
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")


if __name__ == "__main__":
    imagem = cv2.imread('./segundo_modelo.png')
    imagem_tratada = tratar_imagem(imagem)
    texto = converter_imagem_texto(imagem_tratada)
    print(texto)
    reporduzir_audio(texto)