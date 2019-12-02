from Employees import *
from Destinations import *
from Routes import *

class Airway:
    def __init__(self):
        self.employees = []
        self.attendants = []
        self.pilots = [] 
        self.assets = {}
        self.id_counter = 1

cair = Airway()

cair.hire_employee("siggi",251135,652584,22325,"spain-drive 21","siggi@sigg.is",False)



for i in cair.employees:
    print(cair.assets[i])
