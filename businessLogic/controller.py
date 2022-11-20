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
        self._relation = None
        self._topics_iter = None

            
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
        self._topics_iter = iter(list(self.topic_from_txt()))
    
    # print(my_txt.list_words)
    # print(data_txt.dic_words_frequency)    
    #genera nube de palabras

    def word_cloud(self):
        self._obj_analysis()
        wordClouds = wordCloud(self._data_txt.dic_words_frequency)
        wordClouds.generate_wordcloud_image()
    
    #Diagrama de baras - Torta
    def diagram_pie(self):    
        diagram_pie = Diagrams(self._data_txt.dic_words_frequency,self._topics.getTopics)
        diagram_pie.graph_pie()

    #Relacion entre tema y palabras de la nube
    def _relation_topic_word(self):
        #print(self._topics.getTopics)
        self._relation = wordRelationship(self._data_txt.dic_words_frequency, self._topics.getTopics)
    
    #Dibujar grafo
    def graph(self):
        self._relation_topic_word()
        grapho = RelationshipGraph(self._relation.getRelation)
        grapho.graph()
    
    def topic_from_txt(self):        
        return self._topics.getTopics
    
    def topic(self):
        try:            
            topic = next(self._topics_iter)
            print(topic)
            return topic
        except:
            return 0

# definiciones de las palabras

# for x in data_txt.dic_words_frequency.keys():
#     glossary = Dictionary(x)
#     print(x+':',glossary.definitions)
#     print('\n')