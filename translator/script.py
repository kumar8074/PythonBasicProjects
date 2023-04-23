from translate import Translator
translator=Translator(to_lang='pt')
try:
    with open('contents.txt',mode='r') as my_file:
        text=my_file.read()
        translation=translator.translate(text)
        print(translation)

except FileNotFoundError:
    print('please check your path')        
