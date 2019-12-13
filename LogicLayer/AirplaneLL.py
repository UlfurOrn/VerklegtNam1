from enum import Enum
from DataLayer.IOAPI import IOAPI
from ModelFolder.Airplane import Airplane
from LogicLayer.LogicLayer import LogicLayer


class AirplaneLL(LogicLayer):
    def __init__(self):
        self.IOAPI = IOAPI()
        super().__init__()

    def get_manufacturer(self):
        plane_list = self.IOAPI.get_all_airplanes()
        return sorted(plane_list, key=lambda k: k.info_dict["manufacturer"])

    def get_input_type(self, field_index):
    	if field_index in [0,1,2]:
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

    def in_use(self, airplane):
        self.check_time_table(airplane)

    def get_all(self):
        return self.IOAPI.get_airplanes()

    def add(self, airplane):
        self.IOAPI.add_airplane(airplane)

    # TODO: make this work and consolidate the get_manufacturer function above
    def set_sorting_method(self, sorting_method):
        if sorting_method == AirplaneSortingMethods.ALL_AIRPLANES:
            self.asset_list.sort()
        elif sorting_method == AirplaneSortingMethods.ONLY_IN_USE:
            self.asset_list = filter(lambda plane: plane.in_use(),
                                     self.asset_list)
        elif sorting_method == AirplaneSortingMethods.ONLY_NOT_IN_USE:
            self.asset_list = filter(lambda plane: not plane.in_use(),
                                     self.asset_list)
        elif sorting_method == AirplaneSortingMethods.BY_MANUFACTURER:
            self.asset_list.sort(key=lambda plane: plane.manufacturer)


class AirplaneSortingMethods(Enum):
    ALL_AIRPLANES = 0
    ONLY_IN_USE = 1
    ONLY_NOT_IN_USE = 2
    BY_MANUFACTURER = 3
