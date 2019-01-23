"""
a calculator library
"""

def add(*args):
    answer = 0
    for value in args:
        answer += value
    return answer

def test_negative_value():
    """
    negative"""
    assert add(-1,-1,-1,-1,-1) == -5
