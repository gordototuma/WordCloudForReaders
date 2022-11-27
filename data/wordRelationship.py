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
        counter = 0
        for x in self._topics:
            if x[1] != 1: continue
            counter_two = 0
            for y in self._words.keys():                                
                if self._relationship_words(y,x[0]) >= 0.5:                    
                    #print(x[0],y)
                    self._relationship_word_topic.append((x[0],y))
                    counter_two = counter_two+1
                    if counter_two==3: break
            counter = counter+1
            if counter==3: break
                




    
    