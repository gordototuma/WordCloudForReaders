from data.textReader import textReader
from data.wordProcessor import wordProcessor
from data.wordCloud import wordCloud
from data.dictionary import Dictionary

txt = "Ingrese acá su lectura"

my_txt = textReader(txt)
data_txt = wordProcessor(my_txt.list_words)

print(my_txt.list_words)
print(data_txt.dic_words_frequency)

#genera nube de palabras

wordClouds = wordCloud(data_txt.dic_words_frequency)
wordClouds.generate_wordcloud_image()

# definiciones de las palabras

for x in data_txt.dic_words_frequency.keys():
    glossary = Dictionary(x)
    print(x+':',glossary.definitions)
    print('\n')