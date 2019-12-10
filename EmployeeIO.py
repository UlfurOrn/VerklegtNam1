import csv
from Employee import Employee


class EmployeeIO:
    def __init__(self):
        self.employee_list = []

    def get_all(self):
        return self.load_employees()

    def add_employee(self, employee):
        self.employee_list.append(employee)
        self.save_employees()

    def save_employees(self):
        with open("CSVFolder/employees.csv", "w",
                  encoding="utf8") as employee_file:
            csv_writer = csv.writer(employee_file)

            for employee in self.employee_list:
                csv_writer.writerow(employee.get_save_info())

    def load_employees(self):
        if self.employee_list == []:

            with open("CSVFolder/employees.csv", "r",
                      encoding="utf8") as employee_file:
                csv_reader = csv.reader(employee_file)

                for line in csv_reader:
                    name, ssn, address, hphone, wphone, email, plane_type, job_type, time_table = line
                    employee = Employee(name, ssn, address, hphone, wphone,
                                        email, plane_type, job_type,
                                        time_table)

                    self.employee_list.append(employee)

        return self.employee_list
