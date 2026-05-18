coordinates = (10, 20)
print(coordinates)
print(coordinates[0])


#coordinates[0] = 50 # error cause tuple is immutable

corlist = list(coordinates)

corlist[0]= 50
print(corlist)

coordinates = tuple(corlist)
print(coordinates)