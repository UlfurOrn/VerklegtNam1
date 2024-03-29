from enum import Enum
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

    def get_input_specifacation(self, field_index):
        if field_index == 0:
            return "insert name of the new destination's country"
        elif field_index == 1:
            return "insert the name of the new destination's airport"
        elif field_index == 2:
            return "insert the abreviation for your airport"
        elif field_index == 3:
            return "insert the time it takes to fly to the new destination"
        elif field_index == 4:
            return "insert the distance from Iceland"
        elif field_index == 5:
            return "insert the name of the new destination's contanct"
        elif field_index == 6:
            return "insert the phone number of the new destination's contanct"

    def get_input_type(self, field_index):
        return str

    def is_valid_input(self, field_index, new_input):
        if field_index == 0:  # Country
            return self.is_only_letters(new_input) and new_input != ""
        elif field_index == 1:  # Airport
            return self.is_only_letters(new_input) and new_input != ""
        elif field_index == 2:  # Airport Abbreviation
            return self.is_unique_abreviation(new_input) and new_input != ""
        elif field_index == 3:  # Time
            return self.is_time_format(new_input) and new_input != ""
        elif field_index == 4:  # Distance
            return new_input.isdigit() and new_input != ""
        elif field_index == 5:  # Contact name
            return self.is_only_letters(new_input)
        elif field_index == 6:  # Contact number
            return self.is_only_digits(new_input)
        else:
            return True

    def set_sorting_method(self, sorting_method):
        if sorting_method == DestinationSortingMethods.BY_COUNTRY:
            self.asset_list.sort(key=lambda destination: destination.country)
        elif sorting_method == DestinationSortingMethods.BY_FLIGHT_TIME:
            self.asset_list.sort(
                key=lambda destination: destination.flight_time)
        elif sorting_method == DestinationSortingMethods.BY_FLIGHT_DISTANCE:
            self.asset_list.sort(
                key=lambda destination: destination.flight_dist)


class DestinationSortingMethods(Enum):
    BY_COUNTRY = 0
    BY_FLIGHT_TIME = 1
    BY_FLIGHT_DISTANCE = 2
