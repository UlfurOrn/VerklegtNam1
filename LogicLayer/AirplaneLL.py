from enum import Enum
from DataLayer.IO import IO
from ModelFolder.Airplane import Airplane
from LogicLayer.LogicLayer import LogicLayer


class AirplaneLL(LogicLayer):
    def __init__(self):
        self.IO = IO()
        super().__init__()

    def get_manufacturer(self):
        plane_list = self.IO.get_all_airplanes()
        return sorted(plane_list, key=lambda k: k.info_dict["manufacturer"])

    def get_all(self):
        return self.IO.get_airplanes()

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
