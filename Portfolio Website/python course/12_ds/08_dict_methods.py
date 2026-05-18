student = {"harry" : 45, "khushbu" : 45, "marks" : 56 }
print(student)
student["harry"] = 556
print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student.pop("harry"))
print(student)
print(student["marks"]) 
print(student.clear())
print(student.copy())
print(student.fromkeys("khushbu"))