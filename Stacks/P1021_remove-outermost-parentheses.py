# s = "(()())(())"
s = "(()())(())(()(()))"
# s = "()()"

# def removeOuterParentheses(s):
#     counter = 0
#     ouputList = []
#     temp=''
#     for i in range(len(s)):
#         temp+=s[i]
#         if(s[i] == '('):
#             counter +=1
#         elif(s[i] == ')'):
#             counter -=1
        
#         if(counter == 0):
#             temp = temp[1:len(temp)-1]
#             ouputList.append(temp)
#             temp = ''
    
#     output = ''
#     for i in range(len(ouputList)):
#         output +=ouputList[i]

#     print(output)
#     return output

def removeOuterParentheses(s):
    counter = 0
    stack = []
    for i in range(len(s)): 

        if(s[i] == '('):
            counter+=1
            if counter>=2:
                stack.append(s[i])
        else:
            counter -=1
            if counter >=1:
                stack.append(s[i])
    print(''.join(stack))
    return ''.join(stack)
        


removeOuterParentheses(s)