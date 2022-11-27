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
        self._words_iter = None

            
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
        self._words_iter = iter(self._data_txt.words)
    
    
    def word_cloud(self):
        self._obj_analysis()
        wordClouds = wordCloud(self._data_txt.dic_words_frequency)
        wordClouds.generate_wordcloud_image()
    
    
    def diagram_pie(self):    
        diagram_pie = Diagrams(self._data_txt.dic_words_frequency,self._topics.getTopics)
        diagram_pie.graph_pie()

    
    def _relation_topic_word(self):              
        self._relation = wordRelationship(self._data_txt.dic_words_frequency, self._topics.getTopics)
        
    
    
    def graph(self):
        self._relation_topic_word()
        grapho = RelationshipGraph(self._relation.getRelation)
        grapho.graph()
    
    def topic_from_txt(self):        
        return self._topics.getTopics
    
    def topic(self):
        try:            
            topic = next(self._topics_iter)
            return topic
        except:
            return 0
    
    def words(self):
        try:
            word = next(self._words_iter)            
            return word
        except:
            return 0

    def definition_word(self, word):
        glossary = Dictionary(word)
        return glossary.definitions
    
    def validate_acount_words(self):
        if len(self._txt.split(' '))>90:
            return False
        return True
