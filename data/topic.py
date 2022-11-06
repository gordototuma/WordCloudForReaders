import textrazor
from googletrans import Translator
import resources.creds as credentials

class Topic():

    def __init__(self, text):
        self._text = text
        self._topics_from_txt = set()
        self._topic = self._topics()
        self._topic_in_dic(self._topic)
        self._translate_topics()
        


    @property
    def getTopics(self):
        return self._topics_from_txt
    
    
    def _topics(self):
        textrazor.api_key = credentials.api_key
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze(self._text)        
        return response
    

    def _topic_in_dic(self, response_topics):       

        for entity in response_topics.topics():    
            if(0.5<=entity.score <=1):                
                self._topics_from_txt.add((entity.label.lower(), entity.score))                 
            else: break        
    

    def _translate_topics(self):        

        topics = self._topics_from_txt
        self._topics_from_txt = set()
        translator = Translator()

        for x in topics:            
            translation = translator.translate(x[0], dest='es')
            self._topics_from_txt.add((translation.text.lower(), x[1]))

                