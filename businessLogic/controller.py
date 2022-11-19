from data.textReader import textReader
from data.wordProcessor import wordProcessor
from data.wordCloud import wordCloud
from data.dictionary import Dictionary
from data.topic import Topic
from data.wordRelationship import wordRelationship
from data.relationshipGraph import RelationshipGraph
from data.diagrams import Diagrams

class Controller():
    
    def __init__(self):
        self._txt = None 
        self._my_txt = None
        self._data_txt = None
        self._topics = None
            
    @property
    def txt(self):
        return self._txt
    
    @txt.setter
    def txt(self, txt):
        self._txt = txt

    def _obj_analysis(self):
        self._my_txt = textReader(self.txt)
        self._data_txt = wordProcessor(self._my_txt.list_words)
        self._topics = Topic(self.txt)
    
    # print(my_txt.list_words)
    # print(data_txt.dic_words_frequency)    
    #genera nube de palabras

    def word_cloud(self):
        self._obj_analysis()
        wordClouds = wordCloud(self._data_txt.dic_words_frequency)
        wordClouds.generate_wordcloud_image()

# definiciones de las palabras

# for x in data_txt.dic_words_frequency.keys():
#     glossary = Dictionary(x)
#     print(x+':',glossary.definitions)
#     print('\n')

#Temas del texto
# print(topics.getTopics)

#Relacion entre tema y palabras de la nube
#relation = wordRelationship(data_txt.dic_words_frequency, topics.getTopics)

#Dibujar grafo
#grapho = RelationshipGraph(relation.getRelation)
#grapho.graph()

#Diagrama de baras - Torta

# diagram_pie = Diagrams(data_txt.dic_words_frequency,topics.getTopics)
# diagram_pie.graph_pie()