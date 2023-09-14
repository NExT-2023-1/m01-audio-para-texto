from tkinter import *
import os

from entities.SpeechToText import SpeechToText
from entities.TranslateClass import TranslateClass


def withoutCommand():
    print("")


def speechToTextFile():
    stt = SpeechToText()
    filename = "audio_file_1.wav"
    text = stt.convert_speech_to_text_file(audio_file_path=filename)
    print("Recognized text: ", text)

    mainTraductor = TranslateClass()
    mainTranslate = mainTraductor.translateMethod(text, language_destiny='pt')
    print(f"Original text: {text}")
    print(f"Translated: {mainTranslate}")


def speechToTextMicrophone():
    stt = SpeechToText()
    text = stt.convert_speech_to_text_microphone(microphone_input=True)
    print("Recognized text: ", text)

    mainTraductor = TranslateClass()
    mainTranslate = mainTraductor.translateMethod(text, language_destiny='en')
    print(f"Original text: {text}")
    print(f"Translated: {mainTranslate}")


app = Tk()
app.title("NExT-2023 - M01 Audio To Text")
app.geometry("500x300")
app.configure(background="#dde")

menu = Menu(app)
menuSpeechToText = Menu(menu, tearoff=0)
menuSpeechToText.add_command(
    label="From Audio File (wav)", command=speechToTextFile)
menuSpeechToText.add_command(
    label="From Microphne", command=speechToTextMicrophone)
menuSpeechToText.add_separator()
menuSpeechToText.add_command(label="Close", command=app.quit)
menu.add_cascade(label="Speech To Text", menu=menuSpeechToText)

menuTranslator = Menu(menu, tearoff=0)
menuTranslator.add_command(label="English to portuguese", command=withoutCommand)
menuTranslator.add_command(label="Portuguese to English", command=withoutCommand)
menu.add_cascade(label="Translator", menu=menuTranslator)

menuAbout = Menu(menu, tearoff=0)
menuAbout.add_command(label="Speech to Text/Translator", command=withoutCommand)
menu.add_cascade(label="About", menu=menuAbout)

app.config(menu=menu)
app.mainloop()
