def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        elif b<a:
            return b
        else:
            return "Equal"
    elif a%2==0 or b%2==0:
        if a>b:
            return a
        elif b>a:
            return b
    else:
        if a>b:
            return a
        elif b>a:
            return b

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    output = lesser_of_two_evens(a,b)
    print(output)

