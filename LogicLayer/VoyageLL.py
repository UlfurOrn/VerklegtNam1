from DataLayer.IOAPI import IOAPI
from LogicLayer.LogicLayer import LogicLayer
from ModelFolder.Voyage import Voyage


class VoyageLL(LogicLayer):
    def __init__(self):
        self.IOAPI = IOAPI()
        super().__init__()

    def get_voyage_info(self, voyage):
        return_value = str(voyage)
        destination = IOAPI.get_destination_by_id(voyage.destination)
        airplane = IOAPI.get_airplane_by_id(voyage.airplane)
        string += "{} KEF --> {} \n".format(self.destination.departure_time,
                                            self.destination.abrev)
        string += "{} {}<-- KEF \n".format(self.destination.departure_time,
                                           self.destination.abrev)

        return return_value

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
        if field_index == 1:
            return str
        elif field_index == 2:
            return str
        elif field_index == 6:
            return int


    def is_valid_input(self, field_index, new_input, voyage):
        if field_index == 1:
            if self.is_date_format(new_input):
                return self.is_unique_departure(new_input)
            else:
                return False

        elif field_index == 2:
            if self.is_date_format(new_input):
                return self.is_valid_arrival(new_input,voyage)
            else:
                return False
        elif field_index == 6:
            if new_input < self.IOAPI.get_airplane_by_id(voyage).seat_cap and new_input.is_digit():
                return True
            else:
                False
        else:
            return True
