from Employee import *
from Destination import *

class Airway:
    def __init__(self):
        self.employees = []
        self.attendants = []
        self.pilots = [] 
        self.assets = {}
        self.id_counter = 1

    def hire_employee(self,name,mobile,home_phone, address, email,job_type):
        cemployee = Employee(name,mobile,home_phone,address,email,job_type,self.id_counter)
        
        self.assets[self.id_counter] = cemployee
        self.employees.append(self.id_counter)
        if job_type:
            self.pilots.append(self.id_counter)
        else:
            self.attendants.append(self.id_counter)
        self.id_counter+=1

cair = Airway()

cair.hire_employee("siggi",52584,22325,"spain-drive 21","siggi@sigg.is",False)



for i in cair.employees:
    print(cair.assets[i])
