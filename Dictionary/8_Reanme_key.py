student = {
    "name": "Priya",
    "age": 22
}

student["full_name"] = student["name"]
del student["name"]
print(student)

# built in method
student["full_name"] = student.pop("name")
print(student)