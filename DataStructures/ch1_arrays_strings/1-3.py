#Ch. 1: Arrays and Strings
#1-3 Given two strings, write a method to decide if one is a permutation of the other
#Process: split the two words by characters after checking if length is the same.

import string
#First put the word into array/list of characters
#ie: 'geeks' = ['g', 'e', 'e', 'k', 's']
def split(word):
    return [char for char in word]

#Next use a hashmap/dictionary to parse the list and keep track of how many
#   times a specific letter is used in the string
def count(my_list=[], *args):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    #This creates a dictionary d={a:0, b:0, c:0, etc.}
    for char in my_list:
        d[char] += 1
    #for d[char] ie d['g'] increment the value by 1
    return d

def check_length(w1, w2):
    value = False
    if len(w1) == len(w2):
        value = True
    return value

def is_permutation(w1, w2):
    result = False
    if check_length(w1, w2) == True:
        w1_list = split(w1)
        w2_list = split(w2)
        d1 = count(w1_list)
        d2 = count(w2_list)
        if d1 == d2:
            result = True
    return result

w1 = "abccccc"
w2 = "baccccd"

result = is_permutation(w1, w2)
print(result)
