def multiply(lst):
    print(lst)
    last = lst[0]
    flag = False

    for i in lst[1:]:
        if flag == False:
            total = i*last
        elif flag == True:
            total = total*i
        flag = True

    print(total)

lst = [1, 2, 3,4]
multiply(lst)
