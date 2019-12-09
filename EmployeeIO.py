import csv
from Employee import Employee

class EmployeeIO():
    """ 
    def __init__(self):
        self.employee_list = []
    

    def add_employee(self, employee):
        self.employee_list.append(employee)
        self.save_employees()

        
    def save_employees(self):
        with open("VerklegtNam1/CSVFolder/employees.csv", "w") as employee_file:
            fieldnames = ["name", "ssn", "address", "home_phone", "work_phone", "email", "plane_type", "job_type", "time_table"]
            
            csv_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for employee in self.employee_list:
                csv_writer.writerow(employee.info_dict)

    
    def load_employees(self):
        if self.employee_list == []:
            
            with open("VerklegtNam1/CSVFolder/employees.csv", "r") as employee_file:
                csv_reader = csv.DictReader(employee_file)

                for info_dict in csv_reader:
                    employee = Employee(dict(info_dict))
                    
                    self.employee_list.append(employee)
        
        return self.employee_list

"""
    def __init__(self):
        self._employees = {}
        self.attendants = []
        self.pilots = []
        self.load()

    def __str__(self):
        return "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._employees.items()
        ])

    def load(self):
        self._load_csv()

    def add(self, employee):
        self._employees[employee["ssn"]] = employee
        if employee["job_type"] == "Co Pilot" or employee["job_type"] == "Captain":
            self.pilots.append(employee["ssn"])
        else:
            self.attendants.append(employee["ssn"])

    def _load_csv(self):
        self._employees = {}
        with open("CSVFolder/employees.csv", encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add(Employee(row))

    def get_attendants(self):
        return [self._employees[kt] for kt in self.attendants]
    
    def get_pilots(self):
        return [self._employees[kt] for kt in self.pilots]

    def get_all(self):
        return list(self._employees.values())