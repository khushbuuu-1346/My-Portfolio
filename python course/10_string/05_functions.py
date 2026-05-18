'''M = "Meet"
W =len(M)#lenth of string including the spaces
print(W)

print(M.upper(),M) #uppercase of string
print(M.lower(),M) #lowercase of string 
print(M.capitalize()) #capitalizes the first char
print(M.title()) #first char of each word is capitalized
'''

#Removing whtespaces
'''text = " Hello World"
print(text.strip)
print(text.lstrip)
print(text.rstrip)'''

text = "Python is fun"
print(text.find("is"))
print(text.replace("fun",'awesome'))

'''text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)'''

text = "Apples,Bananas,Pineapples"
print(text.split(","))
print((",").join(["Apples,Bananas,Pineapples"]))


text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())