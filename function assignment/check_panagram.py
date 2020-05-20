import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    x = set(alphabet)-set(str1.lower().replace(" ",""))
    if len(x) == 0:
        print(True)
    else:
        print("Not a Panagram")

ispangram("The quick brown fox jumps over the lazy dog")