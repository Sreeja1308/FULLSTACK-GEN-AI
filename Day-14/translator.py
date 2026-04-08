from googletrans import Translator
translator=Translator()
result = translator.translate("How are you today",dest='te')
print("Translated Text:",result.text)