def spy_game(nums):
    mylist = []
    for index in nums[0:]:
        if index == 0 or index == 7:
            index = str(index)
            mylist.append(index)
    mystr = ''.join(mylist)
    if mystr == '007':
        return True
    else:
        return False

output = spy_game([1,0,2,4,0,5,7])
