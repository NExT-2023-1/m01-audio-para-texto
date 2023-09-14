from googletrans import Translator

class TranslateClass:                      
    def __init__(self):
        self.translator = Translator()      

    def translateMethod(self, text, language_origin='auto', language_destiny='en'):        
        try:
            traductor = self.translator.translate(text, src=language_origin, dest=language_destiny)
            return traductor.text
        except Exception as e:
            return f"Error in translation: {str(e)}"

# Exemplo de uso da classe

"""
tradutor = Tradutor()
texto = "Olá, como você está?"
traducao = tradutor.traduzir(texto, idioma_destino='en')
print(f"Texto original: {texto}")
print(f"Tradução: {traducao}")
"""
