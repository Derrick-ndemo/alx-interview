#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 
0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    # List to keep track of which boxes have been unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True

    # Initialize a queue with the first box
    queue = [0]

    while queue:
        # Get the next box
        current_box = queue.pop(0)

        # Go through the keys in the current box
        for key in boxes[current_box]:
            # If the key is a valid box number and that box hasn't been unlocked yet
            if 0 <= key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
