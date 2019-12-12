class Destination:

    def __init__(self, country="", airport="", abrev="", flight_time="", flight_dist="", contact_name="", contact_num=""):
        self.country = country
        self.airport = airport
        self.abrev = abrev
        self.flight_time = flight_time
        self.flight_dist = flight_dist
        self.contact_name = contact_name
        self.contact_num = contact_num


    def get_header(self):
        return ["Country" ,"Airport", "Abreviation", "Time", "Distance", "Contact country", "Contact Num"]

    def get_print_info(self):
        return [self.country, self.airport, self.abrev, self.flight_time, self.flight_dist, self.contact_name, self.contact_num]

    def get_save_info(self):
        return [self.country, self.airport, self.abrev, self.flight_time, self.flight_dist, self.contact_name, self.contact_num]

    def get_creation_fields(self):
        return [0, 1, 2, 3, 4, 5, 6]

    def get_updatable_fields(self):
        return [5, 6]

    def update_info(self, new_info_list):
        country, airport, abrev, flight_time, flight_dist, contact_name, contact_num = new_info_list
        self.country = country
        self.airport = airport
        self.abrev = abrev
        self.flight_time = flight_time
        self.flight_dist = flight_dist
        self.contact_name = contact_name
        self.contact_num = contact_num

    def __str__(self):
        return "{} ({})".format(self.country, self.airport)
