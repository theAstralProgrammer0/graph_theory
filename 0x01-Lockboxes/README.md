# Lockboxes

## Problem Statement

<blockquote>

You have n number of locked boxes in front of you. Each box is numbered

sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

</blockquote>


## Prototype

```function
def canUnlockAll(boxes)
```

## Parameters

- ```boxes``` is a <strong>list of lists</strong>

- Each list in ```boxes``` is a ```box```

- A ```key``` is any of the numbers within a ```box``` 

## Constraints

- Any ```key``` with the same number as the index of a ```box``` opens that ```box```

- You can assume all ```key```s will be positive integers

- There can be ```key```s that do not have ```box```es

- The first box ```boxes[0]``` is unlocked

- Return ```True``` if <strong>all boxes</strong> can be opened, else return ```False```

