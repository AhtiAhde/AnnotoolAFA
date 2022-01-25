import pytest

from modules.book_analytics import BookAnalytics

def test_parse_book_content():
    ba = BookAnalytics("64317.txt.utf-8", book_path="tests/mocks")
    paragraphs, title = ba.parse()
    for paragraph in paragraphs:
        print([paragraph])
    assert len(paragraphs) == 28
    assert title == "The Great Gatsby"