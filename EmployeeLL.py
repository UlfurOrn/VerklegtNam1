from EmployeeIO import EmployeeIO
from Employee import Employee
from LogicLayer import LogicLayer

class EmployeeLL(LogicLayer):

    def __init__(self):
        self.IO = EmployeeIO()


    def get_pilots(self):
        return self.IO.get_pilots()
    

    def get_attendants(self):
        return self.IO.get_attendants()



