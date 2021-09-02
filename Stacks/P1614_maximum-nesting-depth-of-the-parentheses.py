from collections import deque 

s = "(1+(2*3)+((8)/4))+1"

# s = "(1)+((2))+(((3)))"

# s = "1+(2*3)/(2-1)"

# s = "1"

def maxDepth(s):
    stack = deque()
    for i in range(len(s)):
        if s[i] == '(' or s[i] == ')':
            stack.append(s[i])
    counter = 0
    max = 0
    while len(stack) > 0:
        temp = stack.pop()
        if(temp == ')'):
            counter +=1
        else:
            counter -=1
        
        if max < counter:
            max = counter
    
    print(max) 
    return max


maxDepth(s)