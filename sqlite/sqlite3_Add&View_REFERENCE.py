import tkinter as tk
import sqlite3

root = tk.Tk()

conn = sqlite3.connect('address_book.db')
c = conn.cursor()
'''
c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )
            """)
'''

f_name_label = tk.Label(root, text='First Name:')
f_name_label.grid(row=0,column=0, sticky=tk.W)
f_name = tk.Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20)


l_name_label = tk.Label(root, text='Last Name:')
l_name_label.grid(row=1,column=0, sticky=tk.W)
l_name = tk.Entry(root, width=30)
l_name.grid(row=1,column=1, padx=20)


address_label = tk.Label(root, text='Address:')
address_label.grid(row=2,column=0, sticky=tk.W)
address = tk.Entry(root, width=30)
address.grid(row=2,column=1, padx=20)


city_label = tk.Label(root, text='city:')
city_label.grid(row=3,column=0, sticky=tk.W)
city = tk.Entry(root, width=30)
city.grid(row=3,column=1, padx=20)


state_label = tk.Label(root, text='State:')
state_label.grid(row=4,column=0, sticky=tk.W)
state = tk.Entry(root, width=30)
state.grid(row=4,column=1, padx=20)


zipcode_label = tk.Label(root, text='Zipcode:')
zipcode_label.grid(row=5,column=0, sticky=tk.W)
zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5,column=1, padx=20)

def submit():

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        
        }

    )

    conn.commit()
    conn.close()

    
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)

submit_btn = tk.Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6,column=0, columnspan=2)

def show():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    values = c.fetchall()
    for  i in values:
        print(i, end='\n')

    conn.commit()
    conn.close()

show_btn = tk.Button(root, text='Show Records', command=show)
show_btn.grid(row=7, column=0, columnspan=2)

def show_name():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    values = c.fetchall()

    for value in values:
        print('NAMES:',value[0],value[1])

    conn.commit()
    conn.close()

show_name_btn = tk.Button(root, text='Show Names Only', command=show_name)
show_name_btn.grid(row=8, column=0, columnspan=2)

conn.commit()
conn.close()

root.mainloop()
