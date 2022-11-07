import spacy

class wordRelationship():

    def __init__(self, words, topics):
        self._words = words
        self._topics = topics
        self._relationship_word_topic = []
        self._save_relationship()
    

    @property
    def getRelation(self):
        return self._relationship_word_topic
    

    def _relationship_words(self, word, topic):
        
        nlp = spacy.load('es_core_news_md')
        token = lambda word: nlp(word)[0]
        score_words = lambda w1, w2: token(w1).similarity(token(w2))
        return score_words(topic, word)
    

    def _save_relationship(self):

        for x in self._topics:
            if x[1] != 1: continue
            for y in self._words.keys():                                
                if self._relationship_words(y,x[0]) >= 0.5:                    
                    self._relationship_word_topic.append((x[0],y))
                




    
    