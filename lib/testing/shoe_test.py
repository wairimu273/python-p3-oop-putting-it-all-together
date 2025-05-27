# shoe_test.py
"""Shoe Test Module"""
import pytest
from shoe import Shoe  # Corrected: Import Shoe, not Book

def test_has_brand_and_size():
    """module has the brand and size passed to __init__, and values can be set to new instance."""
    shoe = Shoe("Nike", 10)
    assert shoe.brand == "Nike"
    assert shoe.size == 10

def test_requires_int_size(capsys):
    """module prints 'size must be an integer' if size is not an integer."""
    shoe = Shoe("Nike", "invalid")
    captured = capsys.readouterr()
    assert captured.out == "size must be an integer\n"
    assert shoe.size == 0

def test_can_cobble(capsys):
    """module says that the shoe has been repaired."""
    shoe = Shoe("Nike", 10)
    shoe.cobble()
    captured = capsys.readouterr()
    assert captured.out == "Your shoe is as good as new!\n"

def test_cobble_makes_new():
    """module creates an attribute on the instance called 'condition' and set equal to 'New' after repair."""
    shoe = Shoe("Nike", 10)
    shoe.cobble()
    assert shoe.condition == "New"