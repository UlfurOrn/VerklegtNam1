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

    def is_pilot(self, employee):
        return employee.job_type == "Captain" or employee.job_type == "Co Pilot"

    def get_attendants(self):
        return self.IOAPI.get_attendants()

    def get_all(self):
        return self.IOAPI.get_employees()

    def get_by_id(self, item_id):
        return self.IOAPI.get_employee_by_id(item_id)

    def add(self, employee):
        self.IOAPI.add_employee(employee)

    def is_unique_ssn(self, new_ssn):
        employee_list = self.get_all()

        try:
            self.IOAPI.employee.employees[new_ssn]
            return False
        except KeyError:
            return True

    def show_busy_destination(self, departure_str, arrival_str):
        busy_destination = self.get_is_busy_and_free(self.get_all(), departure_str, arrival_str)[0]

        return_list = []

        for employee in busy_destination:
            return_list.append(str(employee[0])+" "+str(employee[1].abrev))

        return return_list


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
        elif field_index in [3,4]:
            return self.is_only_digits(new_input)
        else:
            return True

    def get_input_type(self, field_index):
        return str

    def get_input_specification(self, field_index):
        if field_index == 0:
            return "insert the name of the new employee"
        elif field_index == 1:
            return "insert the social security number of the new employee"
        elif field_index == 2:
            return "insert the address of the new employee"
        elif field_index == 2:
            return "insert the home phone of the new employee"
        elif field_index == 3:
            return "insert the mobile phone of the new employee"
        elif field_index == 4:
            return "insert the email address of the new employee"
        elif field_index == 5:
            return "insert the plane type the employee is allowed to operate(leave empty if attendant)"
        elif field_index == 6:
            return "insert the title of the new employee's position"

    def set_sorting_method(self, sorting_method):
        self.load_asset_list()
        if sorting_method == EmployeeSortingMethods.ALL_EMPLOYEES:
            self.asset_list.sort(key=lambda e: e.name)
        elif sorting_method == EmployeeSortingMethods.PILOTS:
            self.asset_list = list(filter(lambda employee: employee.is_pilot(), self.asset_list))
        elif sorting_method == EmployeeSortingMethods.ATTENDANTS:
            self.asset_list = list(filter(lambda employee: employee.is_attendant(), self.asset_list))
        elif sorting_method == EmployeeSortingMethods.IS_WORKING:
            self.asset_list = list(filter(lambda employee: self.in_use(employee), self.asset_list))
        elif sorting_method == EmployeeSortingMethods.IS_AVAILABLE:
            self.asset_list = list(filter(lambda employee: not self.in_use(employee), self.asset_list))


    def get_week_schedule(self, asset, week_start, week_end):
        schedule = []
        for voyage in asset.time_table:
            voyage = self.IOAPI.get_voyage_by_id(voyage)
            if voyage.departure_time > week_start and voyage.return_time < week_end:
                schedule.append(voyage)
        return voyage


    def get_pilots_ordered_by_plane_type(self):
        total = []
        for plane_type in self.IOAPI.employee.plane_types.values():
            for pilot in plane_type:
                total.append(self.get_by_id(pilot))
        return total





class EmployeeSortingMethods(Enum):
    ALL_EMPLOYEES = 0
    PILOTS = 1
    ATTENDANTS = 2
    IS_WORKING = 3
    IS_AVAILABLE = 4
