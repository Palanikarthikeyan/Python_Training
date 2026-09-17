# Dictionary example using keys(), values(), and items()
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}

print("keys():", student.keys())
print("values():", student.values())
print("items():", student.items())

print("\nIterating keys:")
for key in student.keys(): # Vs for key in student:
    print(key)             #         print(key) - display list of keys

print("\nIterating values:")
for value in student.values(): # for key in student:
    print(value)               #      print(student[key]) # print(student.get(key))

print("\nIterating items:")
for key, value in student.items():    # for key in student:
    print(key, ":", value)            #    print(f'{key} - {student[key]}')

# Recap - list -> Listname.pop() ->remove_lastindex
#                 Listname.pop(index) -> remove_nthindex_value 
#
#  dict -> dictname.pop('OldKey') ->remove_value
