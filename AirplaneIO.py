import csv
from Airplane import Airplane


class AirplaneIO:
    def __init__(self):
        self.airplanes = {}

    def get_all(self):
        return self.load_airplanes()

    def add(self, airplane):
        self.airplanes[airplane.id] = airplane

    def save_airplanes(self):
        with open("CSVFolder/airplanes.csv", "w",
                  encoding="utf8") as airplane_file:
            csv_writer = csv.writer(airplane_file)

            for airplane in self.airplane_list:
                csv_writer.writerow(airplane.get_save_info())

    def load_airplanes(self):
        if self.airplane_list == []:

            with open("CSVFolder/airplanes.csv", "r",
                      encoding="utf8") as airplane_file:
                csv_reader = csv.reader(airplane_file)

                for line in csv_reader:
                    name, manufacturer, plane_type, seat_cap, time_table = line
                    airplane = Airplane(name, manufacturer, plane_type,
                                        seat_cap, time_table)

                    self.add(airplane)

        return self.airplane_list
