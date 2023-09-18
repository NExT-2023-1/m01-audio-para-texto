from googletrans import Translator
from tkinter import filedialog
import os

class TranslatorManager:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, language_origin='auto', language_destiny='en'):
        try:
            traductor = self.translator.translate(
                text, src=language_origin, dest=language_destiny)
            return traductor.text
        except Exception as e:
            return f"Error in translation: {str(e)}"
        
    def translatorenglishtextfile(self):
        # Open a dialog window to select the text file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            # Read file contents in English
            with open(file_path, 'r', encoding='utf-8') as file:
                english_text = file.read()

            # Translate the text into Portuguese
            portuguese_text = self.translator.translate(english_text, src='en', dest='pt').text

            destination_directory = 'text_files(translated)/'
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            # Name the output file 'file_name_translated.txt'
            output_file_name = os.path.splitext(os.path.basename(file_path))[0] + "_translated.txt"
            full_path = os.path.join(destination_directory, output_file_name)

            # Write translated text to a new file
            with open(full_path, 'w', encoding='utf-8') as translated_file:
                translated_file.write(portuguese_text)

            print(english_text)
            print()
            print(portuguese_text)
            print()
            print(f"Translation completed and saved in '{full_path}'.")
            print()

    def translatorportuguesetextfile(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                portuguese_text = file.read()

            english_text = self.translator.translate(portuguese_text, src='pt', dest='en').text
            
            destination_directory = 'text_files(translated)/'
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            output_file_name = os.path.splitext(os.path.basename(file_path))[0] + "_translated.txt"
            full_path = os.path.join(destination_directory, output_file_name)

            with open(full_path, 'w', encoding='utf-8') as translated_file:
                translated_file.write(english_text)

            print(portuguese_text)
            print()
            print(english_text)
            print()
            print(f"Translation completed and saved in '{full_path}'.")
            print()
