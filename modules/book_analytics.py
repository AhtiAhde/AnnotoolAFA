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

    def parse_windows(self):
        """
        Parse method.

        Parses the book to paragraph windows with necessary metadata
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

    def _extract_compound(self, windows):
        """
        Private method extract compound.

        For extracting compound values for ranking.
        Arguments:
        windows - a list of paragraph text windows extracted from book
        """
        compound = []
        for window in windows:
            compound.append(window['sentiment']['compound'])

        return compound

    def _extract_mov_avg(self, compound):
        """
        Private method extract_mov_avg.

        For extracting moving average values for ranking.
        Arguments:
        compound - a list of compound values per windows extracted from book
        """
        # Fix this for a bit better way to avoid miss indexing
        mov_avg = [0, 0]

        for i in range(len(compound)):
            if i > 4:
                mov_avg.append(sum(compound[i-5:i]) / 5)

        return mov_avg

    def _extract_inter_sum(self, compound):
        """
        Private method extract_inter_sum.

        For extracting interval sum values for ranking.
        Arguments:
        compound - a list of compound values per windows extracted from book
        """
        # Fix this for a bit better way to avoid miss indexing
        inter = []
        inter_sum = []

        for i in range(len(compound)):
            if i < len(compound) - 1:
                inter.append(abs(compound[i] - compound[i +1]))
            if i > 4:
                inter_sum.append(sum(inter[i-5:i]) / 5)

        return inter_sum

    def rank_windows(self, windows, alg="inter_sum"):
        """
        Rank windows method.

        Builds a ranked list of the windows
        """
        # All methods will need this
        compound = self._extract_compound(windows)

        # Populate ranking
        rank = []
        if alg=="inter_sum":
            inter_sum = self._extract_inter_sum(compound)
            rank = inter_sum
        if alg=="mov_avg":
            mov_avg = self._extract_mov_avg(compound)
            rank = mov_avg
        if alg=="compound":
            rank = compound

        # Build the objects with ranks
        # Note: we need to be careful with not mixing up with the different
        # lengths of windows and ranks and remember how each has been done
        rank_windows = []
        print("--------------------------")
        print(rank, windows)
        for i in range(len(rank)):
            rank_windows.append({
                "para_id": i,
                "text": windows[i]['text'],
                "rank": rank[i]
            })

        # Do the ranking
        rank_windows.sort(key=lambda x: x['rank'])
        return rank_windows
