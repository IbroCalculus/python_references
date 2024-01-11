for i in range(1, 6):
    print("*" * i)


print("\n\n")
for i in range(1, 11, 2):
    print(("*"*i).center(10))


print("\n\n")
for i in range(1, 11, 2):
    print(("*"*i).center(10, "="))


print("\n\n")
symbol = input("Enter the symbol/character to use in your tree: ")
height = int(input("Enter the height of the tree: "))

for i in range(1, (2*height)+1, 2):
    print((symbol*i).center(2*height))

print("\n\n")

for i in range(1, (2*height)+1, 2):
    print((symbol*i).center(2*height, "-"))
