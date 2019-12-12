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

    def get_all(self):
    	return self.IOAPI.get_airplanes()