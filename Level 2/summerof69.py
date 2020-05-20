def summer_69(arr):
    sum = 0
    arr = sorted(arr)
    for index in arr[0:]:
        if index in range(6,10):
            print(index)
            pass
        else:
            sum = sum + index
    return sum

output = summer_69([11,1,9,5,6,7,8,9,2])
print(output)