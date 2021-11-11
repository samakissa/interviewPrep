from typing import List
input = [[1,-1],[-1,-1]]
count = 0
def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    for x in grid:
        for y in x:
            if y < 0:
                count = count+1
    print(count)
    return count

countNegatives(input)
