from DataLayer.IOAPI import IOAPI
from ModelFolder.Employee import Employee
from LogicLayer.LogicLayer import LogicLayer


class EmployeeLL(LogicLayer):

    def __init__(self):
        self.IOAPI = IOAPI()
        super().__init__()

    def get_pilots(self):
        return self.IOAPI.get_pilots()

    def get_attendants(self):
        return self.IOAPI.get_attendants()

    def get_all(self):
        return self.IOAPI.get_employees()

    def get_by_id(self):
        return "To Do"

    def add(self,employee):
        self.IOAPI.add_employee()



