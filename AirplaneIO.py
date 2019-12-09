import csv
from Airplane import Airplane

class AirplaneIO:

    def __init__(self):
        self.airplane_list = []
    

    def add_airplane(self, airplane):
        self.airplane_list.append(airplane)
        self.save_airplanes()

        
    def save_airplanes(self):
        with open("CSVFolder/airplanes.csv", "w") as airplane_file:
            fieldnames = ["name" ,"manufacturer", "plane_type", "seat_cap", "time_table"]
            
            csv_writer = csv.DictWriter(airplane_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for airplane in self.airplane_list:
                csv_writer.writerow(airplane.info_dict)

    
    def load_airplanes(self):
        if self.airplane_list == []:
            
            with open("CSVFolder/airplanes.csv", "r") as airplane_file:
                csv_reader = csv.DictReader(airplane_file)

                for info_dict in csv_reader:
                    airplane = Airplane(dict(info_dict))
                    
                    self.airplane_list.append(airplane)
        
        return self.airplane_list
