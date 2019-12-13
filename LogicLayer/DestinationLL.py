from DataLayer.IOAPI import IOAPI
from ModelFolder.Destination import Destination
from LogicLayer.LogicLayer import LogicLayer


class DestinationLL(LogicLayer):
    def __init__(self):
        self.IOAPI = IOAPI()
        super().__init__()

    def get_all(self):
        destination_list = self.IOAPI.get_destinations()
        return sorted(destination_list, key=lambda k: k.country)

    def add(self, destination):
        self.IOAPI.add_destination(destination)

    def save(self):
        self.IOAPI.save_destinations()

    def is_unique_abreviation(self, new_abreviation):
        destination_list = self.get_all()

        for destination in destination_list:
            if destination.abrev == new_abreviation:
                return False
        return True

    def get_input_type(self):
        if field_index == 0:
            return str

        elif field_index == 1:
            return str
        elif field_index == 2:
            return str
        elif field_index == 3:
           return str
        elif field_index == 4:
            return int
        elif field_index == 5:
            return str
        elif field_index == 6:
            return int
    def is_valid_input(self, field_index, new_input):
        if field_index == 0:
            return self.is_only_letters(new_input) and new_input != ""

        elif field_index == 1:
            return self.is_only_letters(new_input) and new_input != ""

        elif field_index == 2:
            return self.is_unique_abreviation(new_input) and new_input != ""

        elif field_index == 3:
            return self.is_time_format(new_input)

        elif field_index == 4:
            return new_input.isdigit()

        elif field_index == 5:
            return self.is_only_letters(new_input)

        elif field_index == 6:
            return self.is_only_digits(new_input)

        else:
            return True
