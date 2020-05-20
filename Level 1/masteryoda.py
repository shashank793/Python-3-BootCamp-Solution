def master_yoda(text):
    text = text.split(" ")
    return " ".join(text[::-1])

x = master_yoda(input())
print(x)