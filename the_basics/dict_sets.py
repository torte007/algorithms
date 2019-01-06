# Important information on Dictionaries and Sets in python.
# In python we can use a function called hash() which calls the __hash__ method from the class of the argument.

print(f"The hash of 42 is {hash(42)}")
print(f"The hash of \"Hello world\" is {hash('Hello world')}")

# The hash value can be constructed in essentially constant time.
# This is the mechanism that is used in dictionaries, which are implemented using so-called hash tables.
# Set are implemented using the same mechanism.

# Note:
# For other uses of hashing, such as in cryptography, there is the standard library module hashlib.
