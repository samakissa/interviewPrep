array = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
def countMatches(items, ruleKey, ruleValue):
    index = -1
    counter = 0
    if(ruleKey =="type"):
        index = 0
    elif(ruleKey == "color"):
        index = 1
    elif(ruleKey == "name"):
        index = 2
        
    if (index != -1):
        for i in range(len(items)):
            if items[i][index] == ruleValue:
                counter = counter + 1
    print(counter)
    return counter

countMatches(array, ruleKey, ruleValue)
