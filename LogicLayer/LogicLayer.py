import datetime
from DataLayer.IO import IO


class LogicLayer:
    def __init__(self):
        self.asset_list = self.get_all()
        self._current_page = 1

    def get_page(self, page_delimiter=9):
        return_value = self.asset_list[(self._current_page - 1) *
                                  page_delimiter:self._current_page * page_delimiter]
        return_value += [""] * (page_delimiter - len(return_value))
        return return_value

    def total_pages(self, page_delimiter=9):
        num_pages = len(self.asset_list) // page_delimiter
        if num_pages % page_delimiter != 0:
            num_pages += 1
        if num_pages == 0:
            num_pages += 1
        return num_pages

    def get_current_page(self):
        return self._current_page

    def current_page_size(self):
        return 9 # TODO: Úlfur útfæra plz

    def change_page(self, user_input, num_pages, _current_page):
        if user_input == "a":
            if _current_page == 1:
                _current_page = num_pages
            else:
                _current_page -= 1
        elif user_input == "d":
            if _current_page == num_pages:
                _current_page = 1
            else:
                _current_page += 1
        return _current_page

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
        return self.IO.load()

    def add(self, asset):
        self.IO.add(asset)
        self.save()

    def save(self):
        self.IO.save()

    def load(self):
        self.IO.load()
