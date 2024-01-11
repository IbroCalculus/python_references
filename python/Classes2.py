
class Employee:

    salary_increment = 1.05     #.05 (5%) increment

    #CREATE A CONSTRUCTOR
    def __init__(self, fName, sName, eMail, salary):
        self.fName = fName
        self.sName = sName
        self.eMail = eMail
        self.salary = salary
        self.fullName = f'{fName} {sName}'

    def fullDetails(self):
        print(f'First Name: {self.fName} \n'
              f'Surname: {self.sName} \n'
              f'Email: {self.eMail} \n'
              f'Salary: {self.salary} \n'
              f'FullName: {self.fullName} \n')

    def apply_increment(self):
        self.salary = int(self.salary * self.salary_increment)

emp_1 = Employee("Ibrahim", "Suleiman", "ibsuleiman9@gmail.com", "$95,0000")
emp_2 = Employee("Musa", "Aboy", "ibrahimsmusa9@gmail.com", "$115,000")

'''
 INSTEAD OF:
emp_1.fName = "Ibrahim"
emp_1.sName = "Suleiman"
emp_1.eMail = "ibsuleiman9@gmail.com"
emp_1.salary = "$95,000"

emp_2.fName = "Musa"
emp_2.sName = "Aboy"
emp_2.eMail = "ibrahimsmusa9@gmail.com"
emp_2.salary = "$115,000"
'''

print(emp_1.eMail)
print(emp_2.eMail)
print(f'You are Welcome Mr {emp_1.fullName}')

#CALLING A METHOD INSIDE A CLASS
print('\nFull Details1')
emp_1.fullDetails()
print('\nFull Details2')
Employee.fullDetails(emp_2)
print("-------------\n")

print(f'Without salary increment: {emp_1.salary}')
#emp_1.apply_increment()
print(f'After salary increment: {emp_1.salary}')
print("-----------------\n")
