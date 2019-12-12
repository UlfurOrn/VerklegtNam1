from ModelFolder.Destination import Destination
from ModelFolder.Employee import Employee
from ModelFolder.Airplane import Airplane
from ModelFolder.Voyage import Voyage
from LogicLayer.DestinationLL import *
from LogicLayer.EmployeeLL import *
from LogicLayer.AirplaneLL import *
from LogicLayer.VoyageLL import *
from sys import platform
from os import system


class Command:
    def __init__(self,
                 character,
                 description="",
                 command=None,
                 arguments=None,
                 show=True):
        self.character = character
        self.description = description
        self._command = command
        self.arguments = arguments
        self.show = show

    def __str__(self):
        return "  " + self.character + ". " + self.description

    def __call__(self):
        return self.invoke()

    def is_none(self):
        return self._command == None

    def invoke(self):
        return self._command() if self.arguments is None else self._command(
            self.arguments)


class Commander:
    def __init__(self, *commander):
        self._commands = {}
        for command in commander:
            self._commands[command.character] = command

    def __getitem__(self, key):
        return self._commands[key]

    def __iter__(self):
        return filter(lambda c: c.show, iter(self._commands.values()))

    def add(self, command):
        self._commands[command.character] = command

    def has(self, key):
        return self._commands.get(key, None)


class Menu:
    def title(self):
        raise NotImplementedError()
        return ""

    def commander(self):
        raise NotImplementedError()
        return Commander()

    def has_list(self):
        return False

    def prompt(self):
        return "Input Command: "

    def message_to_user(self):
        return ""

    def needs_legend(self):
        return False

    def commands_printable(self):
        return "\n".join([str(e) for e in self.commander()])

    def _invoke_comand(self, user_input):
        command = self.commander().has(user_input)
        if command == None or command.is_none():
            return self  # TODO: punish the user
        else:
            return command.invoke()

    def handle_input(self, user_input):
        return self._invoke_comand(user_input)


class MainMenu(Menu):
    def title(self):
        return "Main menu"

    def commander(self):
        return Commander(
            Command("1", "Employees", EmployeeMenu),
            Command("2", "Airplanes", AirplaneMenu),
            Command("3", "Destinations", DestinationMenu),
            Command("4", "Voyages", VoyageMenu),
            Command("q", "Quit the program"),
        )


class Asset(Menu):
    def __init__(self):
        self.page_length = 9
        self.current_page = 1

    def __call__(self, sorting_method=0):
        self.sorting_method = sorting_method
        return self

    def commander(self, sorts=True):
        result = Commander(
            Command("c", "Create new " + self.asset, CreationMenu, self),
            Command("b", "Back to main menu", MainMenu),
        )
        if sorts:
            result.add(Command("s", "Select sorting method", SortingMenu,
                               self))
        if self.needs_legend():
            result.add(Command("a", "previous page", lambda: self._change_page(-1), show=False))
            result.add(Command("d", "next page", lambda: self._change_page(1), show=False))
        return result

    def sorting_commands(self):
        raise NotImplementedError("sorting commands missing for " + self.asset)
        return Commander()

    def title(self):
        return self.asset + " list"

    def has_list(self):
        return True

    def listing(self):
        return "\n".join([
            "  {}: {}".format(1 + i, e) for i, e in enumerate(self.logic.get_page_to_print())
        ])

    def needs_legend(self):
        return self.logic.total_pages > 1

    def page_legend(self):
        return "  prev(a) {:>2}/{} next(d)".format(self.logic.get_current_page(), self.logic.total_pages)

    def _change_page(self, shift):
        self.logic.change_page(shift)
        return self

    def handle_input(self, user_input):
        if user_input.isdigit() and 0 < int(user_input) <= self.logic.current_page_size():
            # pass the selected asset to the new editing menu
            return UpdateMenu(self, self.logic.get_asset_at(int(user_input)))
        else:
            return self._invoke_comand(user_input)



class EmployeeMenu(Asset):
    def __init__(self):
        self.asset = "Employee"
        self.logic = EmployeeLL()
        super().__init__()

    def new(self):
        return Employee()


class AirplaneMenu(Asset):
    def __init__(self, sorting_method=0):
        self.asset = "Airplane"
        self.logic = AirplaneLL()
        self.sorting_method = sorting_method
        super().__init__()

    def new(self):
        return Airplane()

    def sorting_commands(self):
        return Commander(
            Command("1", "Find all Airplanes", self, AirplaneSortingMethods.ALL_AIRPLANES),
            Command("2", "Airplanes not in use", self, AirplaneSortingMethods.ONLY_NOT_IN_USE),
            Command("3", "Airplanes in use", self, AirplaneSortingMethods.ONLY_IN_USE),
            Command("4", "Sort by Manufacturer", self, AirplaneSortingMethods.BY_MANUFACTURER),
            Command("b", "Back to " + self.asset + " list", self),
        )


class DestinationMenu(Asset):
    def __init__(self):
        self.asset = "Destination"
        self.logic = DestinationLL()
        super().__init__()

    def commander(self):
        return super().commander(False)

    def new(self):
        return Destination()


class VoyageMenu(Asset):
    def __init__(self):
        self.asset = "Voyage"
        self.logic = VoyageLL()
        super().__init__()

    def commander(self):
        return super().commander(False)

    def new(self):
        return Voyage()


class EditingMenu(Menu):
    def __init__(self, mother):
        self.mother = mother
        self.asset_fields = self.new_asset.get_print_info()
        self.current_index = 0
        self.confirming = False

    def title(self):
        return self._title + " " + self.mother.asset

    def commander(self):
        result = Commander(
            Command(
                "b", "Back to " + self.mother.asset +
                " list and discard all changes", self.mother),
            Command("c", "Confirm changes", self._confirm),
        )
        if self._valid_index() != self.editable_fields[0]:
            result.add(Command("w", "Previous field", lambda: self._with_shifted_field(-1)))
        if self._valid_index() != self.editable_fields[-1]:
            result.add(Command("s", "Next field", lambda: self._with_shifted_field(1)))
        return result

    def has_list(self):
        return True

    def _valid_index(self):
        return self.editable_fields[self.current_index]

    def listing(self):
        header_list = self.new_asset.get_header()
        return "\n".join([
            "{:>13}: {}{}".format(header, info,
                                  " <---" if i == self._valid_index() else "")
            for i, (header,
                    info) in enumerate(zip(header_list, self.asset_fields))
        ])

    def prompt(self):
        return "Enter {}: ".format(
            self.new_asset.get_header()[self.current_index])

    def handle_input(self, user_input):
        command = self.commander().has(user_input)
        if command == None:
            self.asset_fields[self._valid_index()] = user_input
            self._with_shifted_field(1)
            return self
        return command.invoke()

    def _confirm(self):
        self.new_asset.update_info(self.asset_fields)
        return self.mother

    def _with_shifted_field(self, change):
        self.current_index = (self.current_index + change) % len(self.editable_fields)
        return self

class UpdateMenu(EditingMenu):
    def __init__(self, mother, focused_asset):
        self.new_asset = focused_asset
        self._title = "Update"
        self.editable_fields = self.new_asset.get_updatable_fields()
        super().__init__(mother)


class CreationMenu(EditingMenu):
    def __init__(self, mother):
        self.new_asset = mother.new()
        self._title = "New"
        self.editable_fields = self.new_asset.get_creation_fields()
        super().__init__(mother)

class SortingMenu(Menu):
    def __init__(self, mother):
        self.mother = mother

    def title(self):
        return "Sorting " + self.mother.asset + "s"

    def commander(self):
        return self.mother.sorting_commands()


class UserInterface:
    def __init__(self):
        self.menu = MainMenu()
        self._separator_length = 1

    def header(self):
        fluff = "-" * 6
        header = fluff + " " + self.menu.title() + " " + fluff
        self._separator_length = len(header)
        return header

    def clear_screen(self):
        if platform == "win32":
            system("cls")
        else:
            system("clear")

    def separator(self):
        return "-" * self._separator_length

    def loop(self):
        while True:
            self.clear_screen()
            print(self.header())
            if self.menu.has_list():
                print(self.menu.listing())
                print(self.separator())
            print(self.menu.commands_printable())
            print(self.separator())
            if self.menu.has_list() and self.menu.needs_legend():
                print(self.menu.page_legend())
                print(self.separator())

            user_input = input(self.menu.prompt())

            self.menu = self.menu.handle_input(user_input)
            if user_input == "q":
                return  # we outa here