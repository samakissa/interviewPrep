# Test 1
candies = [2,3,5,1,3]
extraCandies = 3

# Test 2
# candies = [4,2,1,1,2]
# extraCandies = 1

# Test3
# candies = [12,1,12]
# extraCandies = 10

def kidsWithCandies(candies, extraCandies):
    max = 0
    result = []
    for i in range(len(candies)):
        if max < candies[i]:
            max = candies[i]

    for i in range(len(candies)):
        if candies[i]+extraCandies>=max:
            result.append(True)
        else:
            result.append(False)

    print(result)
    return result




kidsWithCandies(candies, extraCandies)