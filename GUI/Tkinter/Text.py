import tkinter as tk


root = tk.Tk()

#More on texts in Label

#To access any value i.e text of label_1, do: label_1['text']
#To view all the keys of a tkinter widget, do ie. label.keys()
#Learn to use StringVar as shown below


label_1 = tk.Label(root, text="This is the first line\nSecond\nAnd this is the longest of all, the third",
                   font="Bloodlust 30", bg="red", fg='white', justify=tk.RIGHT)
label_1.pack()


spacer = tk.Label(root, text="", font="Bloodlust 30")
spacer.pack()

label_2 = tk.Label(root, text="This is the first line\nSecond\nAnd this is the longest of all, the third", font="Bloodlust 30", bg="black", fg='green', justify=tk.RIGHT)
label_2.pack()

label_2["text"] = "This is the changed text"

print('TEXT IS: {}'.format(label_2['text']))

for i in label_2.keys():
    print(i)


#USING StringVar; can be used for labels, entry
    
var_1 = tk.StringVar()
label_3 = tk.Label(root, text="String var Text modifier", font="Bloodlust 30", bg="white", fg='black', justify=tk.RIGHT, textvariable=var_1)
label_3.pack()

var_1.set("Text has been modified using StringVar")

root.mainloop()
