'''
Pig latin translator example solution
'''

def pig_latin(word):
    first_word = word[0]
    if first_word in 'aeiou':
        return word+'ay'
    else:
        return word[1:]+first_word+'ay'


word = pig_latin(input())
print(word)