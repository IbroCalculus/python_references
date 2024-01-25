class Employee:
    salary = 5000       # Varaibles are static by default
    salary_increment = 1.05  # .05 (5%) increment

    # CREATE A CONSTRUCTOR
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


    # ======================== To define a static method ====================
    @staticmethod
    def personDetail2():
        return f'Salary: {Employee.salary}'

    @classmethod
    def anotherStaticMethod(cls):
        print("This is another way of declaring a static method!")

    # ======================== toString ====================
    def __str__(self):
        return f'FIRSTNAME: {self.fName}, SURNAME: {self.sName}, AGE: {self.age}'



emp_1 = Employee("Ibrahim", "Suleiman", "ibsuleiman9@gmail.com", "$95,0000")
emp_2 = Employee("Musa", "Aboy", "ibrahimsmusa9@gmail.com", "$115,000")


# CALLING A METHOD INSIDE A CLASS
print('\nFull Details1')
emp_1.fullDetails()
print('\nFull Details2')
Employee.fullDetails(emp_2)
