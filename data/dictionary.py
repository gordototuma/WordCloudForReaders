from pyrae import dle

class Dictionary():

    def __init__(self, word):
        self._word = word
        self._definitions = []
        self._definition()

    
    @property
    def definitions(self):
        return self._definitions


    def _consult(self):
        result = dle.search_by_word(self._word)
        return result.to_dict()

    
    def _definition(self):
        try:
            article = self._consult()['articles'][0]
            for x in range(len(article['definitions'])):
                self._definitions.append(article['definitions'][x]['sentence']['text'])
        except:
            self._definitions.append("Error al buscar la palabra")