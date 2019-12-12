import datetime
from DataLayer.IOAPI import IOAPI


class LogicLayer:
    def __init__(self):
        self._current_page = 0
        self.page_length = 9
        self.load_asset_list()

    def load_asset_list(self):
        self.asset_list = self.get_all()
        self.total_pages = self._total_pages()

    def get_page(self):
        return self.asset_list[self._current_page *
                               self.page_length:(self._current_page + 1) *
                               self.page_length]

    def set_sorting_method(self, sorting_method):
        raise NotImplementedError(
            "set_sorting_method should be overridden by each subclass")

    def get_page_to_print(self):
        page_to_print = self.get_page()
        page_to_print += [""] * (self.page_length - len(page_to_print))
        return page_to_print

    def _total_pages(self):
        num_pages = len(self.asset_list) // self.page_length
        if len(self.asset_list) % self.page_length != 0:
            num_pages += 1
        return num_pages

    def get_current_page(self):
        return self._current_page + 1

    def current_page_size(self):
        return len(self.get_page())

    def change_page(self, change):
        self._current_page = (self._current_page + change) % self.total_pages

    def get_asset_at(self, number):
        return self.asset_list[self._current_page * self.page_length + number -
                               1]

    def set_final_page(self):
        self._current_page = self.total_pages - 1

    def check_time_table(self, time_table, departure_time, arrival_time):
        DEPARTURE = 0
        ARRIVAL = 1

        if len(time_table) == 0:
            return True
        if time_table[0][DEPARTURE] > arrival_time:
            return True
        if time_table[-1][ARRIVAL] < departure_time:
            return True
        for i in range(len(time_table)):
            if time_table[i + 1][DEPARTURE] > arrival_time:
                if time_table[i][ARRIVAL] < departure_time:
                    return True
                else:
                    return False

    def text_to_datetime(self, departure_str, arrival_str):
        departure_time = datetime.datetime(departure_str)
        arrival_time = datetime.datetime(arrival_str)
        return departure_time, arrival_time

    def get_available(self, departure_str, arrival_str):
        departure_time, arrival_time = self.text_to_datetime(
            departure_str, arrival_str)

        return_list = []

        for asset in self.asset_list:
            asset_time_table = asset.time_table

            time_table_to_check = []
            for voyage_id in asset_time_table:
                voyage = self.IO.get_voyage_by_id(voyage_id)
                time_table_to_check.append([
                    self.text_to_datetime(voyage.departure_time,
                                          voyage.departure_return_time)
                ])

                if self.check_time_table(time_table_to_check, departure_time,
                                         arrival_time):
                    return_list.append(asset)

        return return_list

    def is_only_letters(self, string):
        for c in string.strip():
            if c != " ":
                if not c.isalpha():
                    return False
        else:
            return True

    def is_only_numbers(self, string):
        for c in string:
            if not c.isdigit():
                return False
        else:
            return True

    def is_date_format(self, string):
        try:
            datetime.datetime.strptime(string, "‰d/%m/%Y %H:%M")
            return True
        except ValueError:
            return False

    def is_time_format(self, string):
        try:
            datetime.datetime.striptime(string, "%H:%M")
            return True
        except ValueError:
            return False

    def get_all(self):
        return self.IOAPI.load()

    def add(self, asset):
        self.IOAPI.add(asset)
        self.save()

    def save(self):
        self.IOAPI.save()

    def load(self):
        self.IOAPI.load()
