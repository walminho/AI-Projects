# Dependencies
"""
pip install speech_recognition
pip install pyaudio
pip3 install pocketsphinx
"""

#VERSION 2 -- RECORDING AN AUDIO

import speech_recognition as sr

# Cria um reconhecedor
recognizer = sr.Recognizer()

# audio record
with sr.Microphone() as source:
    print("Diga algo:")
    audio = recognizer.listen(source)

try:
    # Using the Google Web Speech API to recognize the audio
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Você disse: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API não entendeu o áudio")
except sr.RequestError as e:
    print("Não foi possível requisitar resultados do Google Web Speech API; {0}".format(e))
