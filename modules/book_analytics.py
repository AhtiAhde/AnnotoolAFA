"""
Book Analytics module.

Module for performing the necessary book analysis in order to
provide prioritized list of paragraphs to annotate.
"""

import re
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.sentiment import SentimentIntensityAnalyzer

class BookAnalytics():
    """
    Book Analytics class.

    Class for performing the necessary book analysis in order to
    provide prioritized list of paragraphs to annotate.
    """

    def __init__(self, book, book_path="static/books"):
        """
        Construct the class.

        Arguments:
        book - the name of the book at the book_path
        book_path - the path to book (overriden for tests)
        """
        self.book_path = book_path
        self.book = book
        # NLTK is mostly for data science and for that reason it
        # always wants to ensure some remote resources are downloaded
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
        """
        Parse method.

        Parses the book to paragraphs with necessary metadata arranged as
        prioritized list (still TODO).
        """
        windows = []
        title = ""
        book_started = False
        buffer = []
        i = 0
        sia = SentimentIntensityAnalyzer()
        book_text = PlaintextCorpusReader(self.book_path + "/", self.book)

        # Go through all the paragraphs of the book and parse content
        for para in book_text.paras():
            for line in para:
                i += 1
                # We do not want to parse Gutenberg meta data
                if book_started:
                    buffer += line
                    # if we will exceed the windo limit of 100 words, append buffer
                    # to a window and start a new one
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
                if title == "" and "Title : " in " ".join(line):
                    title = " ".join(line)[8:]

                if not book_started:
                    if "START OF THIS PROJECT GUTENBERG EBOOK" in " ".join(line):
                        book_started = True
                    if "START OF THE PROJECT GUTENBERG EBOOK" in " ".join(line):
                        book_started = True

        return windows, re.compile(r"\s+").sub(" ", title).strip()
