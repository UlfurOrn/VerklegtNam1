from DestinationIO import DestinationIO
from Destination import Destination

class DestinationLL:

    def __init__(self):
        self.IO = DestinationIO()
    

    def get_all(self):
        destination_list = self.IO.load_destinations()
        return sorted(destination_list, key=lambda k: k.info_dict["country"])

    
    def add_destination(self, destination):
        self.IO.add_destination(destination)


    def save_destinations(self):
        self.IO.save_destinations()


