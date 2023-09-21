"""
Sample tests for pytest

Examples
--------
Run all functions that start with test_*.py or *_test.py
>>> poetry run pytest
"""

def increment(x):
    return x+1 

def test_increment_pass():
    assert increment(3) == 4

def test_increment_fail():
    """You shall not pass!"""
    assert increment(3) == "4"