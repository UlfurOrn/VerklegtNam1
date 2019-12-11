import csv
from Employee import Employee


class EmployeeIO:
    def __init__(self):
        self.employees = {}
        self.attendants = []
        self.pilots = []

    def get_all(self):
        return self.load()

    def add(self, employee):
        self.employees[employee.ssn] = employee
        if(employee.job_type == "Captain" and employee.job_type == "Co Pilot"):
            self.pilots.append(employee.ssn)
        elif(employee.job_type == "Senior Attendant" and employee.job_type == "Attendant"):
            self.attendants.append(employee.ssn)


    def save(self):
        with open("CSVFolder/employees.csv", "w",
                  encoding="utf8") as employee_file:
            csv_writer = csv.writer(employee_file)

            for employee in list(self.employees.values()):
                csv_writer.writerow(employee.get_save_info())

    def load(self):
        if self.employees == {}:

            with open("CSVFolder/employees.csv", "r",
                      encoding="utf8") as employee_file:
                csv_reader = csv.reader(employee_file)

                for line in csv_reader:
                    name, ssn, address, hphone, wphone, email, plane_type, job_type, time_table = line
                    employee = Employee(name, ssn, address, hphone, wphone,
                                        email, plane_type, job_type,
                                        time_table)

                    self.add(employee)

        return list(self.employees.values())
