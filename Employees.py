from datetime import datetime
import csv


class Employee:
    def __init__(self,
                 social=0,
                 name="",
                 role="",
                 rank="",
                 license="",
                 address="",
                 mobile=0,
                 home_phone=0,
                 email="",
                 job_type="",
                 current_id=0):
        self.social = social
        self.name = name
        self.role = role
        self.rank = rank
        self.license = license
        self.address = address
        self.mobile = mobile
        self.home_phone = home_phone
        self.email = email
        self.id = current_id
        self.schedule = [
            [datetime(2019, 10, 23, 10, 30),
             datetime(2019, 10, 30, 10, 30)],
            [datetime(2019, 12, 1, 10, 30),
             datetime(2019, 12, 1, 2, 30)],
            [datetime(2019, 12, 3, 10, 30),
             datetime(2019, 12, 3, 12, 30)]
        ]

    def update_variable(self, value, variable):
        if variable != "":
            if (variable == "mobile"):
                self.mobile = value
            if (variable == "home phone"):
                self.home_phone = value
            if (variable == "address"):
                self.address = value
            if (variable == "email"):
                self.email = value
            if (variable == "plane" and self.role):
                self.plane_type = value
            if (variable == "rank"):
                self.role = not self.role

    def employee_info(self):
        return [
            self.id, self.name, self.social, self.mobile, self.home_phone,
            self.address, self.email, self.plane_type
        ]

    def __str__(self):
        return "id: " + str(
            self.id) + "\nname: " + self.name + "\nmobile phone: " + str(
                self.mobile) + "\nhome phone: " + str(
                    self.home_phone
                ) + "\naddress: " + self.address + "\nemail: " + self.email


class EmployeeContainer:
    def __init__(self, airline=None):
        self._employees = {}
        with open("../UPDATEDSTUDENTDATA/Crew.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                newEmployee= Employee(*[row[reader.fieldnames[i]] for i in range(7)])
                self._employees[newEmployee.social] = newEmployee
        self.all = []
        self.attendants = []
        self.pilots = []
        self.airline = airline

    def __str__(self):
        return "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._employees.items()
        ])
        

    def hire_employee(self, name, social, mobile, home_phone, address, email,
                      plane_type, job_type):
        cemployee = Employee(name, social, mobile, home_phone, address, email,
                             plane_type, job_type, self.airline.id_counter)

        self.airline.data_collection[self.airline.id_counter] = cemployee
        self.all.append(self.airline.id_counter)
        if job_type:
            self.pilots.append(self.airline.id_counter)
        else:
            self.attendants.append(self.airline.id_counter)
        self.airline.id_counter += 1

    def update_employee(self, current_id, updates):
        cemployee = self.airline.data_collection[current_id]
        cemployee.update_variable(updates[0], "mobile")
        cemployee.update_variable(updates[1], "home_phone")
        cemployee.update_variable(updates[2], "address")
        cemployee.update_variable(updates[3], "email")
        cemployee.update_variable(updates[4], "plane")
        cemployee.update_variable(updates[5], "rank")



print(EmployeeContainer().get_employees())
