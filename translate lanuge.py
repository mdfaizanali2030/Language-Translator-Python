from translate import Translator
fr=input('from language:')
to=input('to language:')

translator=Translator(from_lang=fr,to_lang=to)

txt=input('enter text:')
translation=translator.translate(txt)
print(translation)
