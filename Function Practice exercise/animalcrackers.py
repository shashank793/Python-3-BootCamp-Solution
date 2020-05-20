def animal_crackers(text):
    words=text.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False

if __name__ == "__main__":
    status = animal_crackers(input())
    print(status)