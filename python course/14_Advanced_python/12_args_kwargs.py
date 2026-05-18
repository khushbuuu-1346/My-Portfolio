# def sum(*args):
#     total = 0 
#     for item in args:
#         total+= item
#     return total 

# print(sum(475,4,334,23,4))

def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, marie=3234, harry = 343, jay= 34)        
