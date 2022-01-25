import os
import re

class BookAnalytics():
    def __init__(self, book, book_path="static/books"):
        self.book_path = book_path
        self.book = book
    
    def parse(self):
        paragraphs = []
        title = ""
        book_started = False
        buffer = ""
        i = 0
        with open(self.book_path + "/" + self.book, "r") as book_text:
            for line in book_text:
                i += 1
                if book_started:
                    buffer += line
                    # We assume that only paragraphs longer than 15 are meaningful
                    if len(line) == 1:
                        buffer = re.compile(r"\s+").sub(" ", buffer).strip()
                        paragraphs.append(buffer)
                        buffer = ""
                # These ought to be strategy a pattern, that will handle
                # multiple types of books; books released under different
                # licenses follow different patterns; most follow this
                if title == "" and "Title: " in line:
                    title = line[7:]
                if not book_started:
                    if "START OF THIS PROJECT GUTENBERG EBOOK" in line:
                        book_started = True
                    if "START OF THE PROJECT GUTENBERG EBOOK" in line:
                        book_started = True
    
        return paragraphs, re.compile(r"\s+").sub(" ", title).strip()