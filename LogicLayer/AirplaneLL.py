from AirplaneIO import AirplaneIO
from ModelFolder.Airplane import Airplane
from LogicLayer import LogicLayer

class AirplaneLL(LogicLayer):

    def __init__(self):
        self.IO = AirplaneIO()

    def get_manufacturer(self):
        plane_list = self.IO.get_all_airplanes()
        return sorted(plane_list, key=lambda k: k.info_dict["manufacturer"])