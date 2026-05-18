numbers = [1, 2, 3, 4, 5, 43]
def square(x):
    return x*x
new = list(map(square,numbers))
print(new)

numbers = [ 1, 23, 45, 4, 56]
new = list(map(lambda x : x**2, numbers))
print(new)