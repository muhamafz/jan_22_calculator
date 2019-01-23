"""
 test the add() fucntion of the caluclator
"""
from calculator import add
def  test_two_plus_two():
    """
    if given two and two as parameters , 4 should be return
    """
    assert  add(2, 2) == 4

def test_three_and_three():
    """
    if given three and three , six should be given
    """

    assert add(3, 3) == 6
        
