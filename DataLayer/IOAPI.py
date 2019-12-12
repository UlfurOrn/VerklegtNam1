from DataLayer.AirplaneIO import AirplaneIO
from DataLayer.DestinationIO import DestinationIO
from DataLayer.EmployeeIO import EmployeeIO
from DataLayer.VoyageIO import VoyageIO


class IOAPI:
    def __init__(self):
        self.voyage = VoyageIO()
        self.destination = DestinationIO()
        self.employee = EmployeeIO()
        self.airplane = AirplaneIO()

    def get_airplanes(self):
        return self.airplane.get_all()

    def get_destinations(self):
        return self.destination.get_all()

    def get_employees(self):
        return self.employee.get_all()

    def get_voyages(self):
        return self.voyage.get_all()

    def get_airplane_by_id(self):
        return self.airplane.get_by_id()

    def get_destination_by_id(self):
        return self.destination.get_by_id()

    def get_employee_by_id(self):
        return self.employee.get_by_id()

    def get_voyage_by_id(self):
        return self.voyage.get_by_id()

    def save(self):
        self.voyage.save()
        self.destination.save()
        self.airplane.save()
        self.employee.save()

    def load(self):
        self.voyage.load()
        self.destination.load()
        self.airplane.load()
        self.employee.load()

    def add_destination(self, destination):
        self.destination.add(destination)
        self.destination.save()

    def add_airplane(self, airplane):
        self.airplane.add(airplane)
        self.airplane.save()

    def add_voyage(self, voyage):
        self.voyage.add(voyage)
        self.voyage.save()

    def add_employee(self, employee):
        self.employee.add(employee)
        self.employee.save()
