from gtts import gTTS
import pygame
tts = gTTS(text='merhaba ömer faruk nasılsın napıyorsun ne var ne yok konya altınekin', lang='tr')
tts.save("textToSpeech.mp3")

pygame.mixer.init()
pygame.mixer.music.load("textToSpeech.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
