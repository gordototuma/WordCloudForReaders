from data.textReader import textReader
from data.wordProcessor import wordProcessor
from data.wordCloud import wordCloud
from data.dictionary import Dictionary
from data.topic import Topic
from data.wordRelationship import wordRelationship
from data.relationshipGraph import RelationshipGraph
from data.diagrams import Diagrams

txt = 'La heroína es un polvo blanco o marrón o una sustancia pegajosa negra. Es una droga opioide proveniente de la morfina, una sustancia natural en el capullo de la amapola o adormidera asiática. Se puede mezclar con agua y se inyecta con una aguja. La heroína también puede ser fumada o inhalada por la nariz. Todas estas formas de consumir heroína la envían al cerebro muy rápido, lo que la hace muy adictiva. Los principales problemas de salud de la heroína incluyen abortos espontáneos, infecciones del corazón y muerte por sobredosis. Las personas que se inyectan la droga también corren el riesgo de contraer enfermedades infecciosas, incluyendo el VIH/SIDA y la hepatitis. El uso regular de la heroína puede conducir a su tolerancia. Esto significa que los usuarios necesitan más cantidad de la droga para tener el mismo efecto. Las dosis altas generan con el tiempo dependencia a la heroína. Si los usuarios dependientes dejan la droga, tienen síntomas de abstinencia. Estos incluyen agitación, dolor muscular y óseo, diarrea, vómitos y escalofríos con "piel de gallina".'

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
#relation = wordRelationship(data_txt.dic_words_frequency, topics.getTopics)

#Dibujar grafo
#grapho = RelationshipGraph(relation.getRelation)
#grapho.graph()

#Diagrama de baras - Torta

diagram_pie = Diagrams(data_txt.dic_words_frequency,topics.getTopics)
diagram_pie.graph_pie()




