import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from catalogpy.catalog import elencation, ordination, order_longer, order_shortest, remove_words

def test_elencation():
    words = ['apple', 'banana', 'pear', 'kiwi']
    result = elencation(words, max_len=5)
    assert result == "apple\nkiwi\npear"

def test_ordination():
    words = ['apple', 'banana', 'pear', 'kiwi']
    result = ordination(words, max_len=5)
    assert result == "1. apple\n2. kiwi\n3. pear"

def test_order_longer():
    words = ['cat', 'horse', 'dog', 'elephant']
    result = order_longer(words, min_len=4)
    assert result == "elephant\nhorse"

def test_order_shortest():
    words = ['cat', 'horse', 'dog', 'elephant']
    result = order_shortest(words, max_len=3)
    assert result == "cat\ndog"

def test_remove_words():
    words = ['cat', 'horse', 'dog', 'elephant']
    result = remove_words(words, min_len=4, max_len=6)
    assert result == "horse"