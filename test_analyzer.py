import pytest

from analyzer import count_words, count_characters, count_vowels, reverse_text

def test_count_words():
    assert count_words("Hello World") == 3

def test_count_characters():
    assert count_characters("Hello") == 5

def test_count_vowels():
    assert count_vowels("Hello") == 2

def test_reverse_text():
    assert reverse_text("Hello") == "olleH"