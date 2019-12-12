from DataLayer.IO import IO
from ModelFolder.Employee import Employee
from LogicLayer import LogicLayer


class EmployeeLL(LogicLayer):

    def __init__(self):
        self.IO = IO()

    def get_pilots(self):
        return self.IO.get_pilots()

    def get_attendants(self):
        return self.IO.get_attendants()

    def get_all(self):
        return self.IO.get_employees()

    def add(self,employee):
        self.IO.add_employee()



