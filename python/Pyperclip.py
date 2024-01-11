import pyperclip as ppclip

x = input("Enter your name: ")
ppclip.copy(x)
input()
print(ppclip.paste())
print("Pasted")