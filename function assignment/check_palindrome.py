def palindrome(str):
    str = str.lower()
    if " " in str:
        str = str.replace(" ","")
    if str == str[::-1]:
        print(True)
    else:
        print(False)

palindrome(input())

