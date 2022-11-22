import re

class textReader():

    def __init__(self, text):

        self._text = text
        self._words = []
        self._stopWords = set()
        self._readOpinions()
        self._sanatize_words()

    @property
    def list_words(self):
        return self._words


    def _readOpinions(self):
        self._words = self._text.split(' ')
        
    
    def _sanatize_words(self):

        self._stop_words()
        words = [re.sub(r'[.,()"\'-?:!;¿]', '', x).lower() for x in self._words if re.sub(r'[.,()"\'-?:!;¿]', '', x).lower() not in self._stopWords]
        self._words = words
        
        
    def _stop_words(self):
        self._stopWords = {'cómo','puede','muy','estos','su','esto','sín','sin','o','para','también', 'casi', 'través', 'solo', 'que', 'durante', 'un', 'vez', 'qué', 'entre', 'como', 'allí', 'cualquiera', 'y', 'han', 'por', 'las', 'pero', 'podría', 'cada', 'siempre', 'al', 'la', 'haga', 'están', 'después', 'cualquier', 'acerca', 'sin', 'incluso', 'más', 'según', 'los', 'son', 'hay', 'otro', 'a', 'todo', 'de', 'allá', 'ya', 'abajo', 'contra', 'se', 'ambos', 'una', 'mucho', 'alrededor', 'detrás', 'con', 'el', 'excepto', 'poco', 'si', 'misma', 'etc', 'antes', 'arriba', 'lo', 'ser', 'hacer', 'fueron', 'porque', 'aunque', 'menos', 'es', 'además', 'no', 'en', 'antemano'}
