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

    def add_destination(self, destination):
        self.IOAPI.add_destination(destination)

    def save_destinations(self):
        self.IOAPI.save_destinations()
