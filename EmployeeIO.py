import csv
from Employee import Employee

class EmployeeIO:

    def __init__(self):
        self.employee_list = []
    

    def add_employee(self, employee):
        self.employee_list.append(employee)
        self.save_employees()

        
    def save_employees(self):
        with open("CSVFolder/employees.csv", "w") as employee_file:
            fieldnames = ["name", "ssn", "address", "home_phone", "work_phone", "email", "plane_type", "job_type", "time_table"]
            
            csv_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for employee in self.employee_list:
                csv_writer.writerow(employee.info_dict)

    
    def load_employees(self):
        if self.employee_list == []:
            
            with open("CSVFolder/employees.csv", "r") as employee_file:
                csv_reader = csv.DictReader(employee_file)

                for info_dict in csv_reader:
                    employee = Employee(dict(info_dict))
                    
                    self.employee_list.append(employee)
        
        return self.employee_list

