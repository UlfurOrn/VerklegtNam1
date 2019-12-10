from Destination import Destination
from Employee import Employee
from Airplane import Airplane
from DestinationLL import DestinationLL
from EmployeeLL import EmployeeLL
from AirplaneLL import AirplaneLL
from HelperUI import HelperUI


class Command:
    def __init__(self, character, description="", next_menu=None):
        self.character = character
        self.description = description
        self.next_menu = next_menu

    def __str__(self):
        return "  " + self.character + ". " + self.description


class State:
    def __init__(self, title="", commands={}):
        self.title = title
        self.commands = commands

class Menu:
    def title(self):
        return ""

    def commands(self):
        return {}

    def has_list(self):
        return False

    def listing(self):
        return ""

    def prompt(self):
        return "Input Command: "

    def commands_printable(self):
        return "\n".join([str(e) for e in self.commands().values()])

    def selected(self, user_input):
        command = self.commands().get(user_input, None)
        if command == None:
            return self  # TODO: punish the user
        else:
            return command.next_menu


class MainMenu(Menu):
    def title(self):
        return "Main menu"

    def commands(self):
        return {
            "1": Command("1", "Employees", EmployeeMenu()),
            "2": Command("2", "Airplanes", AirplaneMenu()),
            "3": Command("3", "Destinations", DestinationMenu()),
            "4": Command("4", "Voyages", VoyageMenu()),
            "q": Command("q", "Quit the program"),
        }


class Asset(Menu):
    def __init__(self):
        self.HUI = HelperUI()
        self.asset_list = self.logic.get_all()
        self.page_length = 9
        self.current_page = 1
        self.page_count = 1 + (len(self.asset_list)//9)

    def commands(self, sorts=True):
        result = {
            "c": Command("c", "Create new " + self.asset, EditingMenu(self)),
            "b": Command("b", "Back to main menu", MainMenu()),
        }
        if sorts:
            result["s"] = Command("s", "Select sorting method", 6)
        return result

    def title(self):
        return self.asset + " list"

    def has_list(self):
        return True

    def listing(self):
        return "\n".join(["  {}: {}".format(1 + i, e.get_summary()) for i,e in enumerate(self.asset_list)])

    def selected(self, user_input):
        if user_input.isdigit():
            return EditingMenu(self, self.asset_list[int(user_input) - 1])
        else:
            return super().selected(user_input)


class EmployeeMenu(Asset):
    def __init__(self):
        self.asset = "Employee"
        self.logic = EmployeeLL()
        super().__init__()

    def new(self):
        return Employee()


class AirplaneMenu(Asset):
    def __init__(self):
        self.asset = "Airplane"
        self.logic = AirplaneLL()
        super().__init__()

    def new(self):
        return Airplane()


class DestinationMenu(Asset):
    def __init__(self):
        self.asset = "Destination"
        self.logic = DestinationLL()
        super().__init__()

    def commands(self):
        return super().commands(True)

    def new(self):
        return Destination()


class VoyageMenu(Asset):
    def __init__(self):
        self.asset = "Voyage"
        self.logic = EmployeeLL()
        super().__init__()

    def commands(self):
        return super().commands(True)


class EditingMenu(Asset):
    def __init__(self, thing, focused_asset=None):
        self.thing = thing
        self.new_asset = thing.new() if focused_asset is None else focused_asset
        self._title = "New" if focused_asset is None else "Update"
        self.current_index = 0

    def title(self):
        return self._title + " " + self.thing.asset

    def commands(self):
        result = {
            "b": Command("b", "Back to " + self.thing.asset + " list", self.thing),
        }
        return result

    def listing(self):
        key_list = self.new_asset.get_keys()
        header_list = self.new_asset.get_header()
        arrow_pos = [
            " <---" if self.current_index == pos else ""
            for pos in range(len(header_list))
        ]
        return "\n".join(["{:>13}: {}{}".format(header, self.new_asset[key], arrow) for header, key, arrow in zip(header_list, key_list, arrow_pos)])

    def prompt(self):
        return "Enter {}: ".format(self.new_asset.get_header()[self.current_index])


class UserInterface:
    def __init__(self):
        self.HUI = HelperUI()
        self.menu = MainMenu()
        self._separator_length = 1

    def header(self):
        fluff = "-" * 6
        header = fluff + " " + self.menu.title() + " " + fluff
        self._separator_length = len(header)
        return header

    def separator(self):
        return "-" * self._separator_length

    def loop(self):
        while True:
            self.HUI.clear_screen()
            print(self.header())
            if self.menu.has_list():
                print(self.menu.listing())
                print(self.separator())
            print(self.menu.commands_printable())
            print(self.separator())

            user_input = input(self.menu.prompt())

            self.menu = self.menu.selected(user_input)
            if user_input == "q":
                return # we outa here

