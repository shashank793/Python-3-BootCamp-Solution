for number in range(1,101):
    if (number % 3) == 0:
        if (number % 5) == 0:
            print(f"{number} FizzBuzz")
        else:
            print(f"{number} : Fizz")
    elif (number % 5) == 0:
        print(f"{number} Buzz")