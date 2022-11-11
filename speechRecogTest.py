import os
import speech_recognition as sr
import translators as ts
from pathlib import Path

recordPath = str(os.path.join(Path.home(), "Downloads"))
recognizer = sr.Recognizer()

res = {}
i = 1
for file in os.listdir(recordPath):
    # check only text files
    if file.endswith('.wav'):
        res.update({i: file})
        i += 1
print(res)


def recognize(audioData):
    return recognizer.recognize_google(audioData)


def recognizeFromAudio(record):
    recordFile = sr.AudioFile(str(os.path.join(recordPath, record)))
    with recordFile as source:
        audio = recognizer.record(source)
        return recognize(audio)


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        print(type(audio))
        return recognize(audio)


def translate(text, toLang="bn", fromLang="auto"):
    return ts.google(text, to_language=toLang, from_language=fromLang)


file = int(input("Choose file: "))
txt = recognizeFromAudio(res[file])
print("Text -> ", txt)
print("Translated text -> ", translate(txt))
# print(listen())
