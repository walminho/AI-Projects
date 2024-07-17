# Dependencies
"""
pip install speech_recognition
pip install pyaudio
pip3 install pocketsphinx
"""

# VERSION 1 -- USING A FILE ARCHIVE

import speech_recognition as sr
from os import path

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = "Audio/english.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))