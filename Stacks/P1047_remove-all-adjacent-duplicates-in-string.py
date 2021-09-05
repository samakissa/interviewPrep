# s = "abbaca"
s = "azxxzy"

def removeDuplicates(s):
    stack = []
    for i in range(len(s)):
        if stack and (stack[len(stack)-1] == s[i]):
            stack.pop()
        else:
            stack.append(s[i])
    print("".join(stack))
    return "".join(stack)


removeDuplicates(s)
