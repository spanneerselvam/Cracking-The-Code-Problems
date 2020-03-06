#Ch. 1: Arrays and Strings
#Write an alogorithm such that if an element in an MXN matrix is 0, it's entire
#row and column are set to 0
import random, pandas
def pretty_print(arr):
    for row in arr:
        print(*row)
def matrix(rows, columns):
    array = [[random.randint(0,9) for i in range(columns)] for j in range(rows)]
    print("Original Matrix: ")
    pretty_print(array)
    return array
def zero_check(array):
    indices_pairs = [(row,col) for row in range(len(array)) for col in range(len(array[0])) if array[row][col] == 0]
    for indices_pair in indices_pairs:
        row, col = indices_pair
    for i in range(len(array[0])):
        array[row][i] = 0
    for i in range(len(array)):
        array[i][col] = 0
    print("New Array:")
    pretty_print(array)


m = matrix(3,4)
zero_check(m)
