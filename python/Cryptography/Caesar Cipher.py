
#In this type of cipher: Each letter of plain text is replaced by a letter with some fixed number of positions down wit alphabets.
#E.g: ABC = XYZ

msg = input("Enter message: ")

cipherText = ''

for i in msg:
     x = ord(i)
     x += 5
     cipherText += chr(x)

print("CIPHER: ", cipherText)
