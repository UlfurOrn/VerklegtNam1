class Airplane:
    def __init__(self, name="", manufacturer="", plane_type="", seat_cap="", time_table=[]):
        self.name = name
        self.manufacturer = manufacturer
        self.plane_type = plane_type
        self.seat_cap = seat_cap
        self.time_table = time_table

    def get_id(self):
        return self.name

    def get_header(self):
        return ["Name" ,"Manufacturer", "Plane Type", "Seat Capacity"]

    def get_print_info(self):
        return [self.name, self.manufacturer, self.plane_type, self.seat_cap]

    def get_save_info(self):
        return [self.name, self.manufacturer, self.plane_type, self.seat_cap, self.time_table]

    def get_creation_fields(self):
        return [0, 1, 2, 3]

    def get_updatable_fields(self):
        return [0]

    def update_info(self, new_info_list):
        name, manufacturer, plane_type, seat_cap = new_info_list
        self.name = name
        self.manufacturer = manufacturer
        self.plane_type = plane_type
        self.seat_cap = seat_cap

    def __str__(self):
        return "{}: {} {}".format(self.name, self.manufacturer, self.plane_type)
