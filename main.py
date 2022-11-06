from data.textReader import textReader
from data.wordProcessor import wordProcessor
from data.wordCloud import wordCloud
from data.dictionary import Dictionary
from data.topic import Topic
from data.wordRelationship import wordRelationship

txt = 'El criptoanálisis es la rama de criptografía que estudia cómo romper códigos y criptosistemas. El criptoanálisis crea técnicas para romper cifrados, en particular por métodos más eficientes que una búsqueda por fuerza bruta. Además de los métodos tradicionales como el análisis de frecuencia y el índice de coincidencia, el criptoanálisis incluye métodos más recientes, como el criptoanálisis lineal o el criptoanálisis diferencial, que puede romper cifrados más avanzados.'

my_txt = textReader(txt)
data_txt = wordProcessor(my_txt.list_words)
topics = Topic(txt)

# print(my_txt.list_words)
print(data_txt.dic_words_frequency)

#genera nube de palabras

# wordClouds = wordCloud(data_txt.dic_words_frequency)
# wordClouds.generate_wordcloud_image()

# definiciones de las palabras

# for x in data_txt.dic_words_frequency.keys():
#     glossary = Dictionary(x)
#     print(x+':',glossary.definitions)
#     print('\n')

#Temas del texto
print(topics.getTopics)

#Relacion entre tema y palabras de la nube
relation = wordRelationship(data_txt.dic_words_frequency, topics.getTopics)

print(relation.getRelation)