from googletrans import Translator

translator = Translator()

src_text = "Hello, how are you?"
res = translator.translate(src_text, src="auto", dest="fr")  # fr=French
print("Original:", src_text)
print("Translated:", res.text)
