import os
import re
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.sentiment import SentimentIntensityAnalyzer

class BookAnalytics():
    def __init__(self, book, book_path="static/books"):
        self.book_path = book_path
        self.book = book
        nltk.download([
            "names",
            "stopwords",
            "state_union",
            "twitter_samples",
            "movie_reviews",
            "averaged_perceptron_tagger",
            "vader_lexicon",
            "punkt",
        ])
    
    def parse(self):
        windows = []
        title = ""
        book_started = False
        buffer = []
        i = 0
        sia = SentimentIntensityAnalyzer()
        book_text = PlaintextCorpusReader(self.book_path + "/", self.book)
        for line in book_text.paras():
            line = line[0]
            print(line)
            i += 1
            if book_started:
                buffer += line
                print(len(buffer))
                if len(line) + len(buffer) > 100:
                    buffer = re.compile(r"\s+").sub(" ", " ".join(buffer)).strip()
                    windows.append({
                        "text": buffer,
                        "sentiment": sia.polarity_scores(buffer)
                    })
                    buffer = []
            # These ought to be strategy a pattern, that will handle
            # multiple types of books; books released under different
            # licenses follow different patterns; most follow this
            print(" ".join(line))
            if title == "" and "Title : " in " ".join(line):
                title = " ".join(line)[8:]
            if not book_started:
                print("not started", line)
                if "START OF THIS PROJECT GUTENBERG EBOOK" in " ".join(line):
                    book_started = True
                if "START OF THE PROJECT GUTENBERG EBOOK" in " ".join(line):
                    book_started = True

        return windows, re.compile(r"\s+").sub(" ", title).strip()