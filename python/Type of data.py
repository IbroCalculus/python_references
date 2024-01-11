
# ============================= CHECKING DATA TYPE ==========================

full_name = "Ibrahim Calculus"
id_number = 23456

print("Data type", type(full_name))
print("Data type", type(id_number))

if type(id_number) == str:
    print("It is a string datatype")
elif type(id_number) == int:
    print("It is an integer datatype")
else:
    print("It is non of the above")

# ========================== TYPE CASTING ===================================
x = '45'
y = int(x)
z = float(x)
print(z*2)



