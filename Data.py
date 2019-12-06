from Aircraft import *
from Destinations import *
from Employees import *
from Routes import *


class DataInterface:
    def __init__(self):
        self.aircraft = AircraftContainer()
        self.destinations = DestinationContainer()
        self.employees = EmployeeContainer()
        self.routes = RouteContainer()
        self.aircraft.load()
        self.destinations.load()
        self.employees.load()
        self.routes.load()

    def get_employees(self, attendants=True, pilots=True):
        if attendants and pilots:
            return self.employees.get_all()
        elif attendants:
            return self.employees.get_attendants()
        elif pilots:
            return self.employees.get_pilots()
        else:
            return []
    
