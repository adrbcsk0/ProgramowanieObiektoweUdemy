class Employee:

    employeesCount = 0

    def __init__(self, name, surname, email, m_salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.m_salary = m_salary
        Employee.employeesCount +=1

    def get_annual_salary(self):
        yearlySalary = self.m_salary * 12
        print(f"{self.name} {self.surname}'s yearly salary is",yearlySalary )



janek = Employee("Jan", "Kowalski", "jk@mail.com", 2000)
franek = Employee("Franciszek", "Jankowski", "fj@mail.com", 2200)
baranek = Employee("Baranek", "Bananek", "bb@mail.com", 12000)



employeesList = []
employeesList.append(janek)
employeesList.append(franek)
employeesList.append(baranek)

for e in employeesList:
    Employee.get_annual_salary(e)

print ("W bazie jest obecnie:", Employee.employeesCount, "pracowników")