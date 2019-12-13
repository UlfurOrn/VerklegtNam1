import datetime
from enum import Enum
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

    def check_time_table(self, time_table, departure_time, arrival_time):
        DEPARTURE = 0
        ARRIVAL = 1

        if len(time_table) == 0:
            return True
        if time_table[0][DEPARTURE] > arrival_time:
            return True
        if time_table[-1][ARRIVAL] < departure_time:
            return True
        for i in range(len(time_table)):
            if time_table[i + 1][DEPARTURE] > arrival_time:
                if time_table[i][ARRIVAL] < departure_time+datetime.timedelta(day=1):
                    return True
                else:
                    return False

    def is_valid_input(self, field_index, new_input):
        if field_index == 0:
            return self.is_only_letters(new_input) and new_input != ""

        elif field_index == 1:
            return new_input.isdigit() and self.is_unique_ssn(new_input) and new_input != ""

        elif field_index == 6:
            return new_input != ""

        elif field_index == 7:
            return new_input != ""

        else:
            return True


    def set_sorting_method(self, sorting_method):
        if sorting_method == EmployeeSortingMethods.ALL_EMPLOYEES:
            self.asset_list.sort()
        elif sorting_method == EmployeeSortingMethods.PILOTS:
            self.get_pilots()
        elif sorting_method == EmployeeSortingMethods.ATTENDANTS:
            self.get_attendants()
        elif sorting_method == EmployeeSortingMethods.IS_WORKING:
            self.asset_list = filter(lambda employee: employee.in_use(), self.asset_list)
        elif sorting_method == EmployeeSortingMethods.IS_AVAILABLE:
            self.asset_list = filter(lambda employee: not employee.in_use(), self.asset_list)



class EmployeeSortingMethods(Enum):
    ALL_EMPLOYEES = 0
    PILOTS = 1
    ATTENDANTS = 2
    IS_WORKING = 3
    IS_AVAILABLE = 4
    
