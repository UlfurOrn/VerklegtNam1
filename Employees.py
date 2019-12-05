from datetime import datetime
import csv


class Employee(dict):
    def is_pilot(self):
        return self["role"] == "Pilot"
      
class EmployeeContainer:
    def __init__(self):
        self._employees = {}
        self.attendants = []
        self.pilots = []
        self.load_csv()

    def __str__(self):
        return "".join([
            str(k) + ": " + str(v) + "\n"
            for (k, v) in self._employees.items()
        ])

    def add(self, employee):
        self._employees[employee["ssn"]] = employee
        if employee["role"] == "Pilot":
            self.pilots.append(employee["ssn"])
        else:
            self.attendants.append(employee["ssn"])

    def load_csv(self):
        self._employees = {}
        with open("../UPDATEDSTUDENTDATA/Crew.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add(Employee(row))

    def get_attendants(self):
        return [self._employees[kt] for kt in self.attendants]
    
    def get_pilots(self):
        return [self._employees[kt] for kt in self.pilots]

    def get_all(self):
        return [self._employees[kt] for kt in self._employees.keys()]

    # def hire_employee(self, name, social, mobile, home_phone, address, email,
    #                   plane_type, job_type):
    #     cemployee = Employee(name, social, mobile, home_phone, address, email,
    #                          plane_type, job_type, self.airline.id_counter)

    #     self.airline.assets[self.airline.id_counter] = cemployee
    #     self.all.append(self.airline.id_counter)
    #     if job_type:
    #         self.pilots.append(self.airline.id_counter)
    #     else:
    #         self.attendants.append(self.airline.id_counter)
    #     self.airline.id_counter += 1

    # def update_employee(self, cid, updates):
    #     cemployee = self.airline.assets[cid]
    #     cemployee.update_variable(updates[0], "mobile")
    #     cemployee.update_variable(updates[1], "home_phone")
    #     cemployee.update_variable(updates[2], "address")
    #     cemployee.update_variable(updates[3], "email")
    #     cemployee.update_variable(updates[4], "plane")

emps = EmployeeContainer()
print(emps)
print("alsdkjfa;lskdjfals;kjdfl;askdjf;laskdjf;lkj")
print(emps.get_pilots())
