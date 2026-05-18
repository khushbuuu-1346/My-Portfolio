# file = open("15_Files/khushbu.txt", "r")
# for line in file:
#     print(line)
    
# file.close()


with open("15_Files/khushbu.txt", "r") as file: #context manager
    content = file.read()
    print(content)

