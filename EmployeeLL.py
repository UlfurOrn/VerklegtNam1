from EmployeeIO import EmployeeIO
from Employee import Employee

class EmployeeLL:

    def __init__(self):
        self.IO = EmployeeIO()
    

    def get_all(self):
        return self.IO.get_all()


    def get_pilots(self):
        return self.IO.get_pilots()
    

    def get_attendants(self):
        return self.IO.get_attendants()

    
    def add_employee(self, employee):
        self.IO.add_employee(employee)


    def save_employees(self):
        self.IO.save_employees()


