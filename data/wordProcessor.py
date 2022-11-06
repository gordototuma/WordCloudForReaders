class wordProcessor():

    def __init__(self, words):

        self._words = words
        self._word_frequency_dic = {}
        self._calculate_statistics_words()
    
    @property
    def words(self):
        return self._words
    
    @property
    def dic_words_frequency(self):
        return self._word_frequency_dic
        
    
    def _calculate_frequency(self, word):
        return self._words.count(word)


    def _add_Word_and_frequency(self, word, frequency):
        self._word_frequency_dic[word] = frequency

    
    def _calculate_statistics_words(self):

        for x in self._words:
            self._add_Word_and_frequency(x.lower(),self._calculate_frequency(x))