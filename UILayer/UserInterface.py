from sys import platform
from os import system

from UILayer.Abstract import *
from UILayer.Listing import EmployeeMenu
from UILayer.Listing import AirplaneMenu
from UILayer.Listing import DestinationMenu
from UILayer.Listing import VoyageMenu

class MainMenu(Menu):
    def title(self):
        return "Main menu"

    def commander(self):
        return Commander(
            Command("1", "Employees", EmployeeMenu, self),
            Command("2", "Airplanes", AirplaneMenu, self),
            Command("3", "Destinations", DestinationMenu, self),
            Command("4", "Voyages", VoyageMenu, self),
            Command("q", "Quit the program"),
        )


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
