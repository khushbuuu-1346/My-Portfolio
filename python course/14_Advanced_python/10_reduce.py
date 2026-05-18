from functools import reduce 
numbers = [1, 24, 45, 34, 43, 65]
def sum(a,b):
    return a+b 
new = reduce(sum,numbers)
print(new)