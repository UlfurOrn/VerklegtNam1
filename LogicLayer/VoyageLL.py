from enum import Enum
from DataLayer.IOAPI import IOAPI
from LogicLayer.LogicLayer import LogicLayer
from ModelFolder.Voyage import Voyage
from ModelFolder.Destination import Destination
from ModelFolder.Airplane import Airplane


class VoyageLL(LogicLayer):
    def __init__(self):
        self.IOAPI = IOAPI()
        super().__init__()

    def get_voyages_time_period(self,time_start, time_end):


    def get_employees_in_voyage(self, voyage):
        return_array = []
        for i in voyage.pilots:
            return_array.append(self.IOAPI.get_employee_by_id(i))
        for i in voyage.attendants:
            return_array.append(self.IOAPI.get_employee_by_id(i))
        return return_array

    def add_employee_to_voyage(self, voyage, employee):
        employee.time_table.append(voyage.id)
        if employee.job_type == "Captain":
            voyage.pilots[0] = employee
        elif employee.job_type == "Co Pilots":
            voyage.pilots[1] = employee
        elif employee.job_type == "Super Attendant":
            voyage.attendants[0] = employee
        elif employee.job_type == "attendant":
            voyage.attendants.append(employee)

    def add_airplane_to_voyage(self, voyage, airplane):
        airplane.time_table.append(voyage.id)
        voyage.airplane = airplane.id

    def is_unique_departure(self, new_departure_str):
        new_departure_time = self.str_to_datetime(new_departure_str)
        voyage_list = self.get_all()

        for voyage in voyage_list:
            if voyage.departure_time == new_departure_time:
                return False
        return True

    def is_valid_arrival(self, new_input, voyage):
        destination = self.get_destination_by_id(self, voyage.id)
        dest_flight_time = destination.flight_time
        if new_input > self.string_to_datetime(
                voyage.departure) + dest_flight_time:
            return True
        else:
            return False

    def get_all(self):
        return self.IOAPI.get_voyages()

    def add(self, voyage):
        self.IOAPI.add_voyage(voyage)

    def get_input_type(self,field_index):
        return [
            Destination,
            str,
            str,
            Airplane,
            list,
            list,
            int,
        ][field_index]

    def get_input_specification(self, field_index):
        return [
        'press "p" to pick a destination to fly to\n',
        'insert the time of departure "yyyy-mm-dd HH:MM"\n',
        'insert the time of departure returning to Iceland "yyyy-mm-dd HH:MM"\n',
        'if you have selected a timeframe press "p" to select the Airplane to fly with\n',
        'if you have selected a plane press "p" to select a pilot who has the authorization to fly it\n',
        'if you have selected a timeframe press "p" to select an Attendant\n'
        'insert the amount of seats sold this voyage\n'
        ][field_index]

    def is_valid_input(self, field_index, new_input):
        if field_index == 1:
            return self.is_datetime_format(new_input)
        elif field_index == 2:
            return self.is_dateti_format(new_input)
        elif field_index == 6:
            return new_input.is_digit()

    def set_sorting_method(self, sorting_method):
        if sorting_method == VoyageSortingMethods.BY_DESTINATION:
            self.asset_list.sort(key=lambda voyage: voyage.destination)
        elif sorting_method == VoyageSortingMethods.BY_DEPARTURE_TIME:
            self.asset_list.sort(key=lambda voyage: voyage.departure_time)

class VoyageSortingMethods(Enum):
    BY_DESTINATION = 0
    BY_DEPARTURE_TIME = 1
