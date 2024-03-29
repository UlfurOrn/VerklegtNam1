from copy import copy
class Voyage:
    def __init__(self,
                 destination="",
                 departure_time="",
                 return_time="",
                 airplane="",
                 pilot_list=[],
                 attendant_list=[],
                 seats_sold=0):
        self.destination = destination
        self.departure_time = departure_time
        self.return_time = return_time
        self.airplane = airplane
        self.pilot_list = pilot_list
        self.attendant_list = attendant_list
        self.seats_sold = seats_sold

    def get_id(self):
        return str(self.departure_time)

    def get_header(self):
        return [
            "Destination", "Departure", "Arrival", "Airplane", "Pilots",
            "Attendants", "Seats Sold"
        ]

    def get_print_info(self):
        return [
            self.destination, self.departure_time, self.return_time,
            self.airplane, self.pilot_list, self.attendant_list,
            self.seats_sold
        ]

    def get_save_info(self):
        return [
            self.destination, self.departure_time, self.return_time,
            self.airplane, self.pilot_list, self.attendant_list,
            self.seats_sold
        ]

    def get_creation_fields(self):
        return [0, 1, 2, 3, 4, 5, 6]

    def get_updatable_fields(self):
        return [4, 5, 6]

    def update_info(self, new_info_list):
        destination, departure_time, return_time, airplane, pilot_list, attendant_list, seats_sold = new_info_list
        self.destination = destination
        self.departure_time = departure_time
        self.return_time = return_time
        self.airplane = airplane
        self.pilot_list = copy(pilot_list)
        self.attendant_list = copy(attendant_list)
        self.seats_sold = seats_sold

    def __str__(self):
        return "KEF --> {} @ {} | KEF <-- {} @ {}".format(self.destination, self.departure_time, self.destination, self.departure_time)
