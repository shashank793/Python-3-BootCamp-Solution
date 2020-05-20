def count_primes(num):
    print("Here")
    count = 0
    for val in range(1,num+1):
        if val > 1:
            if val == 2:
                count+=1
            for n in range(2,val//2+2):
                # print(n)
                if (val%n) == 0:
                    break
                else:
                    if n == val//2+1:
                        # print(val)
                        count+=1

count_primes(100)