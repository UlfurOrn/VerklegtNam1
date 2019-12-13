from enum import Enum
from DataLayer.IOAPI import IOAPI
from ModelFolder.Airplane import Airplane
from LogicLayer.LogicLayer import LogicLayer


class AirplaneLL(LogicLayer):
    def __init__(self):
        self.IOAPI = IOAPI()
        super().__init__()

    def get_input_type(self, field_index):
        if field_index in [0, 1, 2]:
            return str
        if field_index == 3:
            return int

    def is_valid_input(self, field_index, new_input):
        if field_index == 0:
            return self.is_only_letters(new_input) and new_input != ""

        elif field_index == 3:
            return new_input.isdigit()

        else:
            return True

    def get_input_specifacation(self, field_index):
        if field_index == 0:
            return "insert the name of the airplane"
        elif field_index == 1:
            return "insert the name of the airplane's manufacturer"
        elif field_index == 2:
            return "insert the type of the airplane"
        elif field_index == 3:
            return "insert the amount of seats in the airplane"

    def get_schedule(self, airplane):
        schedule = []
        for voyage in self.IOAPI.get_voyages():
            if voyage.airplane == airplane.get_id():
                schedule.append((self.str_to_datetime(voyage.departure_time),
                                 self.str_to_datetime(voyage.return_time)))
        return schedule

    def get_all(self):
        return self.IOAPI.get_airplanes()

    def add(self, airplane):
        self.IOAPI.add_airplane(airplane)

    # TODO: make this work and consolidate the get_manufacturer function above
    def set_sorting_method(self, sorting_method):
        if sorting_method == AirplaneSortingMethods.ALL_AIRPLANES:
            self.asset_list.sort(key=lambda plane: plane.get_id())
        elif sorting_method == AirplaneSortingMethods.ONLY_IN_USE:
            self.asset_list = list(
                filter(lambda plane: self.in_use(plane), self.asset_list))
        elif sorting_method == AirplaneSortingMethods.ONLY_NOT_IN_USE:
            self.asset_list = list(
                filter(lambda plane: not self.in_use(plane), self.asset_list))
        elif sorting_method == AirplaneSortingMethods.BY_NAME:
            self.asset_list.sort(key=lambda plane: plane.name.lower())
        elif sorting_method == AirplaneSortingMethods.BY_MANUFACTURER:
            self.asset_list.sort(key=lambda plane: plane.manufacturer.lower())


class AirplaneSortingMethods(Enum):
    ALL_AIRPLANES = 0
    ONLY_IN_USE = 1
    ONLY_NOT_IN_USE = 2
    BY_NAME = 3
    BY_MANUFACTURER = 4
