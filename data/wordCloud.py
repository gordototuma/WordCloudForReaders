from wordcloud import WordCloud

class wordCloud():

    def __init__(self, word_frequency):
        self._word_frequency = word_frequency

    
    def generate_wordcloud_image(self):
        wc = WordCloud()
        wc.generate_from_frequencies(self._word_frequency)        
        wc.to_file("./wc.png")
        