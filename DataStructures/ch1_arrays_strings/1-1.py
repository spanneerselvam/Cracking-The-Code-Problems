#Ch. 1: Arrays and Strings
#1.1 Implement alogorithm to determine if a string has all unique characters what if you cannot use additional data structures
#Use a hashmap

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
def is_unique(myDictionary):
    result = True;
    for key, value in myDictionary.items():
        if value > 1:
            result = False
            return result;
    return result;


word = "sai"
my_list = split(word)
myDictionary = count(my_list)
result = is_unique(myDictionary)
print(result)
