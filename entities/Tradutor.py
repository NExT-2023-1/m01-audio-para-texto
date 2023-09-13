from googletrans import Translator

class Tradutor:
    def __init__(self):
        self.translator = Translator()

    def traduzir(self, texto, idioma_origem='auto', idioma_destino='en'):
        try:
            traducao = self.translator.translate(texto, src=idioma_origem, dest=idioma_destino)
            return traducao.text
        except Exception as e:
            return f"Erro na tradução: {str(e)}"

# Exemplo de uso da classe

"""
tradutor = Tradutor()
texto = "Olá, como você está?"
traducao = tradutor.traduzir(texto, idioma_destino='en')
print(f"Texto original: {texto}")
print(f"Tradução: {traducao}")
"""
