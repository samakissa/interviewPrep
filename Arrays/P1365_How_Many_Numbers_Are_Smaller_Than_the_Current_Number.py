# Test 1
nums = [8,1,2,2,3]

# Test 2
# nums = [6,5,4,8]

# Test 3
# nums = [7,7,7,7]

def smallerNumbersThanCurrent(nums):
        result = []
        sorted_nums = sorted(nums)
        for n in nums:
          result.append(sorted_nums.index(n))
        print(result)
        return result


smallerNumbersThanCurrent(nums)