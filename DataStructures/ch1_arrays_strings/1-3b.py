#Extra Problem
#Use Recursion to write all possible permutations of a string
import math
def permutations_length(w1):
    return math.factorial(len(w1))
def permute(w1):
    permutations = []
    my_word = list(w1)
    if len(w1) == 0:
        return permutations
    elif len(w1) == 1:
        permutations.append(w1)
    else:
        for i in range(len(w1)):
            first_element = my_word[i]
            remanding_list = my_word[:i] + my_word[i+1:]
            for p in permute(remanding_list):
                permutations.append([first_element] + p)
    return permutations
def pretty_print(my_list=[], *args):
    permutations = [''.join(x) for x in my_list]
    return permutations


w1 = "abc"
print("Number of Permutations:", permutations_length(w1))
permutations = permute(w1)
print("List of Permutations for string {} are {}: ".format(w1, pretty_print(permutations)))
