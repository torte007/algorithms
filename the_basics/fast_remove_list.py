# If we want to remove elements fast that are inside of a list and we don't care about the order of the list
# then we can just switch the position of the item that we want to remove with the last and make a call to pop

l = list(range(10))
def rem(index, l):
    if index < len(l):
        l[index] = l[len(l) - 1]
        l.pop()
        return l
rem(2, l)
print("done 1")

# This is faster than using the remove method
l = list(range(10))
l.remove(2)
print("done 2")
