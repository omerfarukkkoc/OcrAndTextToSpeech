# -*- coding: utf-8 -*-
"""
Created on 23 Mar 2018

@author: omerfarukkoc
"""

from PIL import Image
import pytesseract

import cv2

from gtts import gTTS

import pygame

image = 'text4.jpg'

print("1-Fotoğraf Alınıyor...")
img = cv2.imread(image)

print("2-OCR Yapılıyor...")
im = Image.open(image)
ocrText = pytesseract.image_to_string(im, lang='tur')

print("3-Dönüştürülüyor...")
tts = gTTS(text=ocrText, lang='tr')
tts.save("speech.mp3")

print("\nFotoğraftan Algılanan Text:\n")
print(ocrText)

cv2.putText(img, "Cikmak icin ESC'e Basin", (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.imshow('Fotograf', img)

print("\n4-Seslendiriliyor...")
pygame.mixer.init()
pygame.mixer.music.load("speech.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print("--Kullanıcı Çıkış Yaptı--")
        break
    continue
print("5-Uygulama Sonlandı")
cv2.destroyAllWindows()