def almost_there(n): #checks if in range within 100 or 200
    if (n in range(90,111)) or (n in range(190,211)):
        return True
    else:
        return False

output = almost_there(int(input()))
print(output)