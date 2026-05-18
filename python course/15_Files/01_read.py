file = open("15_Files/khushbu.txt", "r")
content = file.read()
print(content)
file.close()


try:
    file= open("khushbu.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not Found")