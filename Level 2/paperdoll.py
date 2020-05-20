def paper_doll(text):
    mylist = []
    for i in text[0:]:
        i = i+i+i
        mylist.append(i)
    # pass
    return ''.join(mylist)

# paper_doll(input())
output = paper_doll(input())
print(output)