import csv
from Airplane import Airplane

class AirplaneIO:

    def __init__(self):
        self.airplane_list = []
    
    def add_airplane(self, airplane):
        self.airplane_list.append(airplane)
        self.save_airplanes()

        
    def save_airplanes(self):
        with open("CSVFolder/airplanes.csv", "w", encoding="utf8") as airplane_file:
            csv_writer = csv.writer(airplane_file)

            for airplane in self.airplane_list:
                csv_writer.writerow(airplane.get_save_info())

    
    def load_airplanes(self):
        if self.airplane_list == []:
            
            with open("CSVFolder/airplanes.csv", "r", encoding="utf8") as airplane_file:
                csv_reader = csv.reader(airplane_file)

                for line in csv_reader:
                    name, manufacturer, plane_type, seat_cap, time_table = line
                    airplane = Airplane(name, manufacturer, plane_type, seat_cap, time_table)
                    
                    self.airplane_list.append(airplane)
        
        return self.airplane_list
