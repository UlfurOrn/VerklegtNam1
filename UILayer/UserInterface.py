from ModelFolder.Destination import Destination
from ModelFolder.Employee import Employee
from ModelFolder.Airplane import Airplane
from ModelFolder.Voyage import Voyage
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.AirplaneLL import AirplaneLL
from LogicLayer.VoyageLL import VoyageLL
from UILayer.HelperUI import HelperUI


class Command:
    def __init__(self,
                 character,
                 description="",
                 command=None,
                 arguments=None):
        self.character = character
        self.description = description
        self._command = command
        self.arguments = arguments

    def __str__(self):
        return "  " + self.character + ". " + self.description

    def is_none(self):
        return self._command == None

    def invoke(self):
        return self._command() if self.arguments is None else self._command(
            self.arguments)


class Commander:
    def __init__(self, *commands):
        self._commands = {}
        for command in commands:
            self._commands[command.character] = command

    def __getitem__(self, key):
        return self._commands[key]

    def __iter__(self):
        return iter(self._commands.values())

    def add(self, command):
        self._commands[command.character] = command

    def has(self, key):
        return self._commands.get(key, None)


class Menu:
    def title(self):
        raise NotImplementedError()
        return ""

    def commands(self):
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
        return "\n".join([str(e) for e in self.commands()])

    def handle_input(self, user_input):
        command = self.commands().has(user_input)
        if command == None or command.is_none():
            return self  # TODO: punish the user
        else:
            return command.invoke()


class MainMenu(Menu):
    def title(self):
        return "Main menu"

    def commands(self):
        return Commander(
            Command("1", "Employees", EmployeeMenu),
            Command("2", "Airplanes", AirplaneMenu),
            Command("3", "Destinations", DestinationMenu),
            Command("4", "Voyages", VoyageMenu),
            Command("q", "Quit the program"),
        )


class Asset(Menu):
    def __init__(self):
        self.HUI = HelperUI()
        self.asset_list = self.logic.get_all()
        self.page_length = 9
        self.current_page = 1
        self.page_count = self.logic.total_pages(self.asset_list, self.page_length)

    def __call__(self, sorting_method=0):
        self.sorting_method = sorting_method
        return self

    def commands(self, sorts=True):
        result = Commander(
            Command("c", "Create new " + self.asset, EditingMenu, self),
            Command("b", "Back to main menu", MainMenu),
        )
        if sorts:
            result.add(Command("s", "Select sorting method", SortingMenu,
                               self))
        return result

    def title(self):
        return self.asset + " list"

    def has_list(self):
        return True

    def listing(self):
        return "\n".join([
            "  {}: {}".format(1 + i, e) for i, e in enumerate(self.logic.get_page(self.asset_list, self.current_page, self.page_length))
        ])

    def needs_legend(self):
        return False
        return self.logic.is_paginated()

    def page_legend(self):
        return "prev(a) " + self.logic.current_page(
        ) + "/" + self.logic.total_pages() + " next(d)"

    def handle_input(self, user_input):
        self.current_page = self.logic.change_page(user_input, self.page_count, self.current_page)

        if user_input.isdigit() and int(user_input) <= len(self.asset_list):
            # pass the selected asset to the new editing menu
            return EditingMenu(self, self.asset_list[int(user_input) - 1])
        else:
            return super().handle_input(user_input)



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
            Command("1", "Find all Airplanes", self),
            Command("2", "Sort by Manufacturer", self),
            Command("3", "Airplanes not in use", self),
            Command("4", "Airplanes in use", self),
            Command("b", "Back to " + self.asset + " list", self),
        )


class DestinationMenu(Asset):
    def __init__(self):
        self.asset = "Destination"
        self.logic = DestinationLL()
        super().__init__()

    def commands(self):
        return super().commands(False)

    def new(self):
        return Destination()


class VoyageMenu(Asset):
    def __init__(self):
        self.asset = "Voyage"
        self.logic = VoyageLL()
        super().__init__()

    def commands(self):
        return super().commands(False)

    def new(self):
        return Voyage()


class EditingMenu(Menu):
    def __init__(self, mother, focused_asset=None):
        self.mother = mother
        self.new_asset = mother.new(
        ) if focused_asset is None else focused_asset
        self.asset_fields = self.new_asset.get_print_info()
        self._title = "New" if focused_asset is None else "Update"
        self.updatable_fields = self.new_asset.get_updatable_fields()
        self.current_index = 0
        self.confirming = False

    def title(self):
        return self._title + " " + self.mother.asset

    def commands(self):
        commander = Commander(
            Command(
                "b", "Back to " + self.mother.asset +
                " list and discard all changes", self.mother),
            Command("c", "Confirm changes", self._confirm),
        )
        if self._valid_index() != self.updatable_fields[0]:
            commander.add(Command("w", "Previous field", self._with_shifted_field(-1)), )
        if self._valid_index() != self.updatable_fields[-1]:
            commander.add(Command("s", "Next field", self._with_shifted_field(1)), )
        return commander

    def has_list(self):
        return True

    def _valid_index(self):
        return self.updatable_fields[self.current_index]

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
        commanded = super().handle_input(user_input)
        if commanded == self:
            self.asset_fields[self._valid_index()] = user_input
            self.current_index += 1
            print(self.current_index)
            if self.current_index >= len(self.updatable_fields):
                self.current_index = 0
            return self
        else:
            return commanded

    def _confirm(self):
        self.new_asset.update_info(self.asset_fields)
        return self.mother

    def _with_shifted_field(self, change):
        self.current_index = (self.current_index + change) % len(self.updatable_fields)
        return lambda: self

class SortingMenu(Menu):
    def __init__(self, mother):
        self.mother = mother

    def title(self):
        return "Sorting " + self.mother.asset + "s"

    def commands(self):
        return self.mother.sorting_commands()


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
            if self.menu.has_list() and self.menu.needs_legend():
                print(self.menu.page_legend())
                print(self.separator())

            user_input = input(self.menu.prompt())

            self.menu = self.menu.handle_input(user_input)
            if user_input == "q":
                return  # we outa here
