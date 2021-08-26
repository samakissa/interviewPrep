# test 1
nums = [2,5,1,3,4,7]
n = 3

# test 2
# nums = [1,2,3,4,4,3,2,1]
# n = 4

# test 3
# nums = [1,1,2,2]
# n = 2

def shuffle(nums,n):
        temp=[]
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[n+i])
        print(temp)
        return temp

shuffle(nums,n)