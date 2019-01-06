# When prototyping or even finalizing data structures such as trees,
# it can be useful to have a flexible class that will allow you
# to specify arbitrary attributes in the constructor.

# the Bunch pattern (named by ale Martelli in the Python Cookbook) can come in handy.


class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self

# now to test it we can do somethign like
x = Bunch(name="Tomas Ortega", message="Hello world", id="12345")
print("The name of x is x.name: " + x.name)
print("The message of x is x.message: " + x.message)
