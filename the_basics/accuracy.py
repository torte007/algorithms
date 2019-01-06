# This module might be important for financial applications, where you need exact calculations with a certain number of decimals.
from decimal import *
from math import sqrt

print(sum(Decimal("0.1") for i in range(10)))
# So instead for returning 0.999999, it will return 1.0

x = sum(Decimal("0.1") for i in range(10))

print(x == Decimal("1.0"))

# To achieve higher accuracy, you’ll need to rewrite your expressions.
# Consider, for example, the expression sqrt(x+1)-sqrt(x), where we assume that x is very big.
# The thing to do would be to get rid of the risky subtraction.
# By multiplying and dividing by sqrt(x+1)+sqrt(x), we end up
# with an expression that is mathematically equivalent to the original
# but where we have eliminated the subtraction: 1.0/(sqrt(x+1)+sqrt(x))

u = 8762348761.13

y = sqrt(u + 1) - sqrt(u)
print(y)
y = 1.0/(sqrt(u) + sqrt(u + 1))
print(y)

print("As you can see, even though the expressions are equivalent mathematically, they give different answers (with the latter being more accurate).")
