from DataLayer.IOAPI import IOAPI
from ModelFolder.Airplane import Airplane
from LogicLayer.LogicLayer import LogicLayer

class AirplaneLL(LogicLayer):

    def __init__(self):
        self.IO = IOAPI()
        self.MA = Airplane()

    def get_manufacturer(self):
        plane_list = self.IO.get_all_airplanes()
        return sorted(plane_list, key=lambda k: k.info_dict["manufacturer"])