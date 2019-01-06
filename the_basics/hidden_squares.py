from random import randrange
import timeit

L = [randrange(100) for i in range(1000000)]
print(42 in L)

S = set(L)
print(42 in S)

# membership checks are linear for lists and constant for sets
# Using a list would give you quadratic running time, whereas using a set would be linear.
