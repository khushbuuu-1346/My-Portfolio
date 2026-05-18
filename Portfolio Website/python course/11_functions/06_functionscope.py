def sum(a,b):
    c =  a + b 
    return c 
print(sum(5,6))
print(sum(365,873))


def average(a,b,c):
    d = ( a + b + c)/3
    print(d)
    g = 45 # Its a local variable
    
average(3,4,5)

g = 8764  # Its global variable
print(average(4,53,5))
print(g)

x = 67
def my_func():

    x = 20
    print(x)
my_func() 
print(x)   



def sum(a,b):
    print("Im summing")
    c = a + b
    global z # modifying from local to  global
    z = 34 # becomes global and not local
    return c
z = 35
print(sum(734, 34))
print(z)