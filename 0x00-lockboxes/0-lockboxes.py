#!/usr/bin/python3
"""Method for if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Can be opened or not?"""
    keys = [0]
    for key in keys:
        # this print the key
        for i in boxes[key]:
            if i not in keys and i < len(boxes):
                keys.append(i)
    if len(keys) == len(boxes):
        return True
    return False
