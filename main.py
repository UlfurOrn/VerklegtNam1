from Employees import *
from Destinations import *
from Routes import *

class Airway:
    def __init__(self):
        self.employees = EmployeeContainer(self)
        self.assets = {}
        self.id_counter = 1


cair = Airway()

cair.employees.hire_employee("siggi","251135","652584","22325","spain-drive 21","siggi@sigg.is",False)



for i in cair.employees.all:
    print(cair.assets[i])
print()
cair.employees.update_employee(1,["","","spain-drive 23",""])

for i in cair.employees.all:
    print(cair.assets[i])
