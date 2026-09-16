p1 = ["Laptop", 75000, "Electronics"]
p2 = ["Backpack", 1200, "Accessories"]
p3 = ["Notebook", 80, "Stationery"]

print(f"About {p1[0]} details:-")
for var in p1:
    print(f"{var}")
    
p1.append(5)
p2.append(6)
p3.append(4)
print(p1)
print(p2)
print(p3)