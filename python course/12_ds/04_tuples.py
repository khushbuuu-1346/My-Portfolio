a = (1, 34, 35, 56, 67)
print(a)
print(a[2])

b = (3, )#creating tuple with single element
print(b)

tu = (10, 34, 23)
a, b, c = tu
print(a, b, c) #unpacking of tuples

a = (10, 30, 20, 10, 20, 20)
print(a.count(20))
print(a.count(10)) # tuple method called count
print(a.index(20)) #index of first element in occurence
print(a, type(a))