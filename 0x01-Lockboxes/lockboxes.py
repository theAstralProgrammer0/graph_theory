def canUnlockAll(boxes):
    visited = 0
    i = 0
    next = 1
    end = len(boxes) - 1 
    
    while visited < len(boxes):
        next = find_next(boxes[i], next, end)
        if next < 0:
            break
        i = next
        visited += 1

    if visited >= len(boxes) - 1:
        return True
    return False

def find_next(box, next, end):
    if next >= end:
        return -1

    for i in range(len(box)):
        if box[i] == next:
            return box[i]
    return find_next(box, 1 + next, end)
