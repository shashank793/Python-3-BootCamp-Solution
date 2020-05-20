def has_33(nums):
    last = nums[0]
    for index in nums[1:]:
        if index == last:
            return True
        last = index
    return False

mylist = [3,1,3]
output = has_33(mylist)
print(output)