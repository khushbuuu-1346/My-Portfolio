my_sets = {1, 2, 3, 3, 4}
print(my_sets) #3 only print once , set cannot have duplicate elements
my_sets.add(5)
print(my_sets)
my_sets.remove(2)
print(my_sets)


a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)
d = a.intersection(b)
diff = a.difference(b)

print(c,d,diff)

