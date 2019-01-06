# From the book Python Algorithms:
# "When in doubt, use brute force" Ken Thompson

# Implementing Adjacency Lists and the likes
# In python, we can represent a set with {} for example: {1, 2, 3, 4, 5}
# We can use the add function to add elements to a set and the remove function to remove elements
# Note: To create an empty set we need to use set() because {} is an empty dictionar


# We can represent a graph like so:

a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},  # a
    {c, e},  # b
    {d},  # c
    {e},  # d
    {f},  # e
    {c, g, h},  # f
    {f, h},  # g
    {f, g}  # h
]

# And we can find the neighbors using N[v] where v is some vertex in the graph
print(f"The neighbors of a are: {N[a]}")
print(f"The neighbors of b are: {N[b]}")
print("And so on ...")
print("We can find out if a vertex is a neighbor of some other vertex or not")
print(f"Is b a neighbor of a? \n {b in N[a]}")
print("We can also find the degree of a node")
print(f"The degree of a is: {len(N[a])}")
print(f"The degree of f is: {len(N[f])}")


W = {
    "a" : set('bcdef'),
    "b" : set('ce'),
    "c" : set('d'),
    "d" : set('e'),
    "f" : set('cgh'),
    "g" : set('fh'),
    "h" : set('fg')
}

print(f"The neighbors of a in W is: {W['a']}")
print(f"The neighbors of b in W are: {W['b']}")
print("Again, and so on...")
print(f"Is b a neighbor of a in W? {'b' in W['a']}")
print("The degree of f is: " + str(len(W['f'])))

#     a b c d e f g h
N = [[0,1,1,1,1,1,0,0], # a
    [0,0,1,0,1,0,0,0], # b
    [0,0,0,1,0,0,0,0], # c
    [0,0,0,0,1,0,0,0], # d
    [0,0,0,0,0,1,0,0], # e
    [0,0,1,0,0,0,1,1], # f
    [0,0,0,0,0,1,0,1], # g
    [0,0,0,0,0,1,1,0]] # h

f = N[a][b] # Neighborhood membership
print("Are a and b neighbors? " + str(f))
a, b, c, d, e, f, g, h = range(8)
d = sum(N[f]) # Degree
print("What is the degree of f? " + str(d))
