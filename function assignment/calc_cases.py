def up_low(s):
    is_upper = 0
    is_lower = 0
    for char in s[:]:
        if char.isupper() is True:
            is_upper+=1
        elif char.islower() is True:
            is_lower+=1

    print(f'No. of Upper case characters : {is_upper} \n\
No. of Lower case Characters : {is_lower}')


text = "Hello Mr. Rogers, how are you this fine Tuesday?"
# input()
up_low(text)