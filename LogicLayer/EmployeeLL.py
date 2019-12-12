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

    def add(self, employee):
        self.IOAPI.add_employee(employee)

    def is_unique_ssn(self, new_ssn):
        employee_list = self.get_all()

        for employee in employee_list:
            if employee.ssn == new_ssn:
                return False
        return True

    def is_valid_input(self, field_index, new_input):
        if field_index == 0:
            return self.is_only_letters(new_input) and new_input != ""
        elif field_index == 1:
            return new_input.isdigit() and self.is_unique_ssn(
                new_input) and new_input != ""
        elif field_index == 6:
            return new_input != ""
        elif field_index == 7:
            return new_input != ""
        else:
            return True
