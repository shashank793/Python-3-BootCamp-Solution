def old_macdonald(name):
    x =  list(name)
    x[0] = x[0].upper()
    x[3] = x[3].upper()
    return ''.join(x)

name = old_macdonald('shahsank')
print(name)