from EmployeeIO import EmployeeIO
from Employee import Employee

class EmployeeLL:

    def __init__(self):
        self.IO = EmployeeIO()
    

    def get_all(self):
        return self.IO.load_employees()


    def get_pilots(self):
        pilot_list = []
        employee_list = self.get_all()

        for employee in employee_list:
            if employee.get_job() == "Captain" or employee.get_job() == "Co Pilot":
                pilot_list.append(employee)
        
        return pilot_list
    

    def get_attendants(self):
        attendant_list = []
        employee_list = self.get_all()

        for employee in employee_list:
            if employee.get_job() == "Super Attendant" or employee.get_job() == "Attendant":
                attendant_list.append(employee)
        
        return attendant_list

    
    def add_employee(self, employee):
        self.IO.add_employee(employee)


    def save_employees(self):
        self.IO.save_employees()


