import csv
import json
from ModelFolder.Employee import Employee


class EmployeeIO:
    def __init__(self):
        self.employees = {}
        self.plane_types = {}
        self.attendants = []
        self.pilots = []

    def get_all(self):
        return self.load()

    def get_by_id(self, item_id):
        return self.employees[item_id]

    def add(self, employee):

        self.employees[employee.ssn] = employee
        if(employee.job_type == "Captain" or employee.job_type == "Co Pilot"):
            self.pilots.append(employee.ssn)
            try:
                self.plane_types[employee.plane_type].append(employee.ssn)
            except KeyError:
                self.plane_types[employee.plane_type] = [employee.ssn]
        elif(employee.job_type == "Senior Attendant" and employee.job_type == "Attendant"):
            self.attendants.append(employee.ssn)

    def save(self):
        with open("Data/employees.json", "w") as employee_file:
            employee_file.write(
                json.dumps(
                    [employee.get_save_info() for employee in self.employees.values()]))

    def load(self):
        if self.employees == {}:
            with open("Data/employees.json", "r") as employee_file:
                for line in json.loads(employee_file.read()):
                    name, ssn, address, hphone, wphone, email, plane_type, job_type, time_table = line
                    employee = Employee(name, ssn, address, hphone, wphone,
                                        email, plane_type, job_type,
                                        time_table)
                    self.add(employee)
        return list(self.employees.values())
