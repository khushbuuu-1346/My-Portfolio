fruits = {"apple" , "banana", "oranges"}
print(fruits, type(fruits))


my_set = {2, 24, 56, 35, 34}
my_set.add(36)
print(my_set)
my_set.remove(34)#throws  error the element is not present
print(my_set)
my_set.discard(459)# even if the element is not present it simply ignores
print(my_set)
my_set.pop()
print(my_set)