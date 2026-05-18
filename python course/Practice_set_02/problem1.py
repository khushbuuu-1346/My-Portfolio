num = {2 , 3, 4, 5, 5, 7, 7, 8}
print(num)

my_dict = {"chips" : 20, "kurkure" : 30 , "bhujia": 40}
highest_value = max(my_dict.keys())
print(my_dict)
print(highest_value)


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)   # merges dict2 into dict1
print(dict1)          # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
