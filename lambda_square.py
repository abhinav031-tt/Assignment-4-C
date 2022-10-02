'''

Python program to square the elements of a list using map() function.'''


lst = [4, 5, 2, 9]

def num_square(lst):
    return lst ** 2


result = map(num_square, lst)
print("Square the elements of the said list using map():")
print(list(result))