import wikipedia
from mstranslator import Translator
translator = Translator("8dc97e03193b4674b160cfe2b07c8223")
print(translator.translate('Привет, мир!', lang_from='ru', lang_to='en'))
import wikipedia
wikipedia.set_lang("en")
mlen = wikipedia.page("machine learning")
en_content=mlen.content
wikipedia.set_lang("fr")
#print(mlen.content)
mlfr = wikipedia.page("machine learning")
fr_content=mlfr.content
#print(mlfr.content)
