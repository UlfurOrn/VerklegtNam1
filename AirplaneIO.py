import csv
from Airplane import Airplane


class AirplaneIO:
    def __init__(self):
        self.airplanes = {}
        self.load()

    def get_all(self):
        return self.load_airplanes()

    def get_by_id(self, item_id):
        return self.airplanes[item_id]

    def add(self, airplane):
        self.airplanes[airplane.ID] = airplane

    def save(self):
        with open("CSVFolder/airplanes.csv", "w",
                  encoding="utf8") as airplane_file:
            csv_writer = csv.writer(airplane_file)

            for airplane in list(self.airplanes.values()):
                csv_writer.writerow(airplane.get_save_info())

    def load(self):
        if self.airplanes == {}:

            with open("CSVFolder/airplanes.csv", "r",
                      encoding="utf8") as airplane_file:
                csv_reader = csv.reader(airplane_file)

                for line in csv_reader:
                    name, manufacturer, plane_type, seat_cap, time_table = line
                    airplane = Airplane(name, manufacturer, plane_type,
                                        seat_cap, time_table)

                    self.add(airplane)

        return list(self.airplanes.values())
