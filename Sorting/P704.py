
nums = [-1,0,3,5,9,12]
target = 9

def binarySearch(arr,l,r,x):
    if r>=1:
        mid = l + (r-l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

def search(nums, target):
    left, right= 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) // 2
        
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1

print(search(nums, target))