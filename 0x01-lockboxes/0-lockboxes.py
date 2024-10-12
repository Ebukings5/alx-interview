#!/usr/bin/python3
"""
0-lockboxes.py

This module contains the function canUnlockAll, which determines if all
the boxes can be opened given a list of boxes, where each box may contain
keys to other boxes.

Function:
    canUnlockAll(boxes): Returns True if all boxes can be opened, else False.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of list of int): A list where each element is a list of keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n:
                    stack.append(key)

    return len(opened) == n


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False