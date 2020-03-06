#Ch. 1: Arrays and Strings
#Given an image representing by an NxN matrix, where each pixel in the image is 4 byes,
#write a method to rotate the image by 90 degrees. Can you do this in place?
#Things to think about: last column turns to first row, first column turns to last row
import random
def pretty_print(arr):
    for row in arr:
        print(*row)
def matrix(rows):
    columns = rows
    arr = [[random.randint(0,9) for i in range(columns)] for j in range(rows)]
    print("Original Matrix: ")
    pretty_print(arr)
    return arr
def rotate_matrix(m):
    new_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
    print("New Matrix: ")
    pretty_print(new_m)


m = matrix(3)
rotate_matrix(m)
