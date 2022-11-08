import matplotlib.pyplot as plt


class Diagrams():

    def __init__(self, words, topics):
        self._all_words = words
        self._all_topics = topics
        #self._topics_relevants = []
        self._words_relevants = []
        self._words_relevants_frequency = []
        self._frequency_relevant_words()
        self._most_relevant_words()
    
    def _frequency_relevant_words(self):
        for x in self._all_words.values():
            if x >= 2:
                self._words_relevants_frequency.append(x)


    def _most_relevant_words(self):
        for x in self._all_words.keys():
            if self._all_words[x] >= 2:
                self._words_relevants.append(x)
    

    def graph_pie(self):
        colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        plt.pie(self._words_relevants_frequency, labels=self._words_relevants, autopct="%0.1f %%", colors=colores)
        plt.axis("equal")
        plt.show()
