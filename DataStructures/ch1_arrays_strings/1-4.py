#Ch. 1: Arrays and Strings
#Write a method to replace all spaces in a string with '%20'

import re

def replace_space(word):
    word1 = re.sub("\s+", "%20", word.strip())
    return word1

word = "i love seahorses"
print(replace_space(word))
