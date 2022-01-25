import pytest

from modules.book_importer import BookImporter

def test_parse_book_content():
    importer = BookImporter(None, book_path="tests/mocks")
    paragraphs, title = importer._parse_book_content("64317.txt.utf-8")
    for paragraph in paragraphs:
        print([paragraph])
    assert len(paragraphs) == 28
    assert title == "The Great Gatsby"