from datetime import datetime
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

    def get_time_schedule(self, asset, time_start, time_end):
        schedule = []
        for voyage in asset.time_table:
            voyage = self.IOAPI.get_voyage_by_id(voyage)
            if voyage.departure_time > week_start and voyage.return_time < week_end:
                schedule.append(voyage)
        return voyage


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

    def get_asset_at(self, index):
        return self.asset_list[self._current_page * self.page_length + index -
                               1]

    def set_final_page(self):
        self._current_page = self.total_pages - 1

    def intersects_schedule(self, asset, time):
        first, last = time if time is tuple else (time, time)
        for (start, end) in self.get_schedule(asset):
            if start < time and time < end:
                return True
        return False

    def in_use(self, asset):
        return self.intersects_schedule(asset, datetime.now())

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
        return False

    def is_busy_during_period(self, asset, departure_str, arrival_str):
        departure_time, arrival_time = (self.str_to_datetime(departure_str),
                                        self.str_to_datetime(arrival_str))
        asset_time_table = asset.time_table

        time_table_to_check = []
        if len(asset_time_table) >=1:
            for voyage_id in asset_time_table:
                print(asset.time_table)
                if voyage_id is not "":
                    voyage = self.IOAPI.get_voyage_by_id(voyage_id)
                    time_table_to_check.append(
                        self.text_to_datetime(voyage.departure_time,
                                              voyage.return_time))
                    if not self.check_time_table(time_table_to_check, departure_time,
                                                 arrival_time):
                        return voyage
        return False


    def get_is_busy_and_free(self, asset_list, departure_str, arrival_str):
        departure_time, arrival_time = (self.str_to_datetime(departure_str),
                                        self.str_to_datetime(arrival_str))

        busy = []
        free = []

        for asset in self.asset_list:
            voyage_if_busy = self.is_busy(asset, departure_str, arrival_str)
            if voyage_if_busy:
                busy.append((asset,voyage_if_busy))
            else:
                free.append(asset)

        return busy, free

    def is_only_letters(self, string):
        for c in string.strip():
            if c != " ":
                if not c.isalpha():
                    return False
        else:
            return True

    def is_only_digits(self, string):
        return string.isdigit()

    def is_datetime_format(self, string):
        try:
            datetime.fromisoformat(string)
            return True
        except:
            return False

    def str_to_datetime(self, string):
        return datetime.fromisoformat(string)

    def str_to_time_delta(self, string):
        hour, minute = string.split(":")
        datetime.timedelta(hour=int(hour), minute=int(minute))

    def get_all(self):
        return self.IOAPI.load()

    def add(self, asset):
        self.IOAPI.add(asset)
        self.save()

    def save(self):
        self.IOAPI.save()

    def load(self):
        self.IOAPI.load()
