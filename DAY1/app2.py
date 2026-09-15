import sys
print("Python version")
print(sys.version)
print("My current python version is:",sys.version) # Using comma separation - way-1
print("My Current python version is:{}".format(sys.version)) # Using str.format() - way-2
print(f"My Current python version is: {sys.version}") # Using f-string - way-3 