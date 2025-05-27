# book_test.py
"""Book Test Module"""
import pytest
from book import Book
def test_has_title_and_page_count():
    """module has the title and page_count passed into __init__, and values can be set to new instance."""
    book = Book("Sample Title", 100)
    assert book.title == "Sample Title"
    assert book.page_count == 100
def test_requires_int_page_count(capsys):
    """module prints 'page_count must be an integer' if page_count is not an integer."""
    book = Book("Sample Title", "invalid")
    captured = capsys.readouterr()
    assert captured.out == "page_count must be an integer\n"
    assert book.page_count == 0
def test_can_turn_page(capsys):
    """module outputs 'Flipping the page...wow, you read fast!' when method turn_page() is called"""
    book = Book("Sample Title", 100)
    book.turn_page()
    captured = capsys.readouterr()
    assert captured.out == "Flipping the page...wow, you read fast!\n"