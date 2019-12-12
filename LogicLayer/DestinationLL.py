from DataLayer.IO import IO
from ModelFolder.Destination import Destination
from LogicLayer import LogicLayer

class DestinationLL(LogicLayer):

    def __init__(self):
        self.IO = IO()
    

    def get_all(self):
        destination_list = self.IO.get_destinations()
        return sorted(destination_list, key=lambda k: k.country)

    
    def add_destination(self, destination):
        self.IO.add_destination(destination)


    def save_destinations(self):
        self.IO.save_destinations()


