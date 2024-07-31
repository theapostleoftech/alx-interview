#!/usr/bin/python3
"""
Module for lockboxes
"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened.

    Number of boxes is n.
    Each box is numbered sequentially from 0 to n - 1 and each box may
    contain keys to the other boxes.
    Key with the same number as a box opens that box.
    You can assume all keys will be positive integers.
    There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.

    Args:
        boxes (List[List[int]]): list of lists of integers.

    Returns:
        boolean: True if all boxes can be unlocked, by using all the keys
        available in all the reachable boxes, and False otherwise.
    """
    
    opened = {0}
    
    line = [boxes[0]]
    
    while line:
        
        box = line.pop(0)
        
        for key in box:
           
            if key not in opened and key < len(boxes):
                
                opened.add(key)
               
                line.append(boxes[key])
    
    return len(opened) == len(boxes)
