names = ["Nahn", "Crep", "Elhn", "Orks"]
#index     0        1       2      3
print(names[2]) # Access element by index
names[1] = "CrepVN"
print(names[1])
print(len(names)) # Length of list
del names[0] # Delete by index
names.remove("Orks") # Delete by value
names.append("Ornas") # Add element to the final of the list
names.insert(8, "Heux") # Add element to the direct index
for name in names:
    print(name)
for i in range(len(names)):
    print(i+1, end=". ")
    print(names[i])
    
