from AirplaneIO import AirplaneIO
from Airplane import Airplane

class AirplaneLL:

    def __init__(self):
        self.IO = AirplaneIO()
    

    def get_all(self):
        return self.IO.load_airplanes()


    def get_manufacturer(self):
        plane_list = self.get_all()
        return sorted(plane_list, key=lambda k: k.info_dict["manufacturer"])

    
    def add_airplane(self, airplane):
        self.IO.add_airplane(airplane)


    def save_airplanes(self):
        self.IO.save_airplanes()
