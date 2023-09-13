from tkinter import *
import os

from entities.SpeechToText import SpeechToText
from entities.Tradutor import Tradutor

def semComando():
    print("")

def speechToTextFile():
    stt = SpeechToText()
    filename = "audio_file_1.wav"
    text = stt.convert_speech_to_text_file(audio_file_path=filename)
    print("Recognized text: ", text)

    tradutor = Tradutor()
    traducao = tradutor.traduzir(text, idioma_destino='pt')
    print(f"Texto original: {text}")
    print(f"Tradução: {traducao}")

def speechToTextMicrophone():
    stt = SpeechToText()
    text = stt.convert_speech_to_text_microphone(microphone_input=True)
    print("Recognized text: ", text)

    tradutor = Tradutor()
    traducao = tradutor.traduzir(text, idioma_destino='en')
    print(f"Texto original: {text}")
    print(f"Tradução: {traducao}")

app = Tk()
app.title("NExT-2023 - M01 Audio To Text")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus=Menu(app)
menuSpeechToText=Menu(barraDeMenus, tearoff=0)
menuSpeechToText.add_command(label="From Audio File (wav)", command=speechToTextFile)
menuSpeechToText.add_command(label="From Microphne", command=speechToTextMicrophone)
menuSpeechToText.add_separator()
menuSpeechToText.add_command(label="Close", command=app.quit)
barraDeMenus.add_cascade(label="Speech To Text", menu=menuSpeechToText)

menuTranslator=Menu(barraDeMenus, tearoff=0)
menuTranslator.add_command(label="English to portuguese", command=semComando)
menuTranslator.add_command(label="Portuguese to English", command=semComando)
barraDeMenus.add_cascade(label="Translator", menu=menuTranslator)

menuSobre=Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Speech to Text/Translator", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()
