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


class StateSpace:
    def __init__(self):
        self.current = 0
        self.states = {
            0:
            State(
                "Main Menu", {
                    "1": Command("1", "Employees", 1),
                    "2": Command("2", "Airplanes", 2),
                    "3": Command("3", "Destinations", 3),
                    "4": Command("4", "Voyages", 4),
                    "q": Command("q", "Quit the program"),
                }),
            1:
            State(
                "Employees", {
                    "c": Command(
                        "c",
                        "Create new employee",
                        5,
                    ),
                    "s": Command("s", "Select sorting method", 6),
                    "b": Command("b", "Back to main menu", 0),
                }),
            2:
            State("Airplanes"),
            3:
            State("Destinations"),
            4:
            State("Voyages"),
            5:
            State("New "),
        }

    def title(self):
        return self.states[self.current].title

    def commands(self):
        return self.states[self.current].commands

    def transition(self, user_input):
        command = self.states[self.current].commands.get(user_input, None)
        if command == None:
            pass  # punish the user
        else:
            self.current = command.transition
        print("hwer ", command.transition)


class Menu:
    def title(self):
        return ""

    def commands(self):
        return {}

    def has_list(self):
        return False

    def listing(self):
        return ""

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
        self.current_page = 0

    def commands(self, sorts=True):
        result = {
            "c": Command("c", "Create new " + self.asset, CreationMenu(self)),
            "b": Command("b", "Back to main menu", MainMenu()),
        }
        if sorts:
            result["s"] = Command("s", "Select sorting method", 6)
        return result

    def has_list(self):
        return True

    def listing(self):
        for i in range(9):
            try:
                print("  {}: {}".format(
                    1 + i,
                    self.asset_list[(self.current_page)+i].get_summary()))
            except IndexError:
                print("")
        # self.HUI.list_screen(self.asset_list, self.title(), [], 1,1)


class EmployeeMenu(Asset):
    def __init__(self):
        self.asset = "employee"
        self.logic = EmployeeLL()
        super().__init__()

    def title(self):
        return "Employee list"


class AirplaneMenu(Asset):
    def __init__(self):
        self.asset = "airplane"
        self.logic = AirplaneLL()
        super().__init__()

    def title(self):
        return "Airplane list"


class DestinationMenu(Asset):
    def __init__(self):
        self.asset = "destination"
        self.logic = DestinationLL()
        super().__init__()

    def title(self):
        return "Destination list"

    def commands(self):
        return super().commands(True)


class VoyageMenu(Asset):
    def __init__(self):
        self.asset = "voyage"
        self.logic = EmployeeLL()
        super().__init__()

    def title(self):
        return "Voyage list"

    def commands(self):
        return super().commands(True)


class CreationMenu(Menu):
    def __init__(self, thing):
        self.thing = thing

    def title(self):
        return "New " + self.thing.asset

    def commands(self):
        return {}


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

            user_input = input("Input Command: ")

            self.menu = self.menu.selected(user_input)
            if user_input == "q":
                return

    def old_loop(self, asset_name="Asset"):
        asset_list = self.LL.get_all()

        title = asset_name + " List"
        instruction_list = [
            "c. Create new " + asset_name, "b. Back to Main Menu"
        ]
        current_page = 1

        num_pages = len(asset_list) // self.HUI.PAGE_DELIMETER
        if len(asset_list) % self.HUI.PAGE_DELIMETER != 0:
            num_pages += 1
        if num_pages == 0:
            num_pages += 1

        while True:
            self.HUI.list_screen(asset_list, title, instruction_list,
                                 current_page, num_pages)

            user_input = input("Enter command: ")

            if user_input == "d":
                if current_page == num_pages:
                    current_page = 1
                else:
                    current_page += 1

            elif user_input == "a":
                if current_page == 1:
                    current_page = num_pages
                else:
                    current_page -= 1

            elif user_input.isdigit():
                if int(user_input) >= 1 and int(
                        user_input) <= self.HUI.PAGE_DELIMETER:
                    try:
                        self.display_asset(asset_list[(current_page - 1) *
                                                      self.HUI.PAGE_DELIMETER +
                                                      int(user_input) - 1])
                    except:
                        pass

            elif user_input == "c":
                return self.create_asset()

            elif user_input == "b":
                return
