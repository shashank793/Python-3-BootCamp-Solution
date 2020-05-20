def blackjack(a,b,c):
    
    if (a in range(1,12)) and (b in range(1,12)) and (c in range(1,12)):
        sum = a + b + c
        if sum <= 21:
            return sum
        elif (a == 11 or b == 11 or c == 11) and (sum > 21):
            return sum-10
        else:
            return "BUST"
    else:
        return "Enter number 1 and 11"

    # pass

output = blackjack(int(input()),int(input()),int(input()))
print(output)