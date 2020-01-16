#Ch. 1: Arrays and Strings
#1.4 Compress a given string such that aaabbcdddd to be a3b2c1d4
import string
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
def string_compression(word):
    resulting_list = []
    word_list = split(word)
    word_dic = count(word_list)
    result = {k: v for k, v in word_dic.items() if v != 0}
    for key, value in result.items():
        resulting_list.append(key)
        resulting_list.append(value)
    return resulting_list
def pretty_print(my_list=[], *args):
    result = ''.join(str(e) for e in my_list)
    print(result)


word = "aaabbcddddddeeeeeeeeefghiiiiiijkkkkkkk"
result = string_compression(word)
pretty_print(result)
