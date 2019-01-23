"""
 test the add() fucntion of the caluclator
"""
from calculator import add
def  test_two_plus_two():
    """
    if given two and two as parameters , 4 should be return
    """
    assert  add(2, 2) == 4
     
