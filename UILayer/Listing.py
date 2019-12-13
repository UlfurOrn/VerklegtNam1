from ModelFolder.Destination import Destination
from ModelFolder.Employee import Employee
from ModelFolder.Airplane import Airplane
from ModelFolder.Voyage import Voyage
from LogicLayer.DestinationLL import *
from LogicLayer.EmployeeLL import *
from LogicLayer.AirplaneLL import *
from LogicLayer.VoyageLL import *

from UILayer.Abstract import *

class Asset(Menu):
    def __init__(self, mother):
        self.mother = mother
        self.page_length = 9
        self.current_page = 1

    def __call__(self, sorting_method=0):
        self.sorting_method = sorting_method
        return self

    def commander(self, sorts=True):
        result = Commander(
            Command("c", "Create new " + self.asset, EditingMenu, (self, None, True)),
            Command("b", "Back to main menu", lambda: self.mother),
        )
        if sorts:
            result.add(Command("s", "Select sorting method", SortingMenu,
                               self))
        if self.needs_legend():
            result.add(
                Command("a",
                        "previous page",
                        lambda: self._change_page(-1),
                        show=False))
            result.add(
                Command("d",
                        "next page",
                        lambda: self._change_page(1),
                        show=False))
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
            "  {}: {}".format(1 + i, e)
            for i, e in enumerate(self.logic.get_page_to_print())
        ])

    def needs_legend(self):
        return self.logic.total_pages > 1

    def page_legend(self):
        return "  prev(a) {:>2}/{} next(d)".format(
            self.logic.get_current_page(), self.logic.total_pages)

    def _change_page(self, shift):
        self.logic.change_page(shift)
        return self

    def handle_input(self, user_input):
        if user_input.isdigit(
        ) and 0 < int(user_input) <= self.logic.current_page_size():
            # pass the selected asset to the new editing menu
            return EditingMenu(self, self.logic.get_asset_at(int(user_input)))
        else:
            return self._invoke_comand(user_input)


class SortingMenu(Menu):
    def __init__(self, mother):
        self.mother = mother

    def title(self):
        return "Sorting " + self.mother.asset + "s"

    def commander(self):
        return self.mother.sorting_commands()


class EmployeeMenu(Asset):
    def __init__(self, mother):
        self.asset = "Employee"
        self.logic = EmployeeLL()
        super().__init__(mother)

    def new(self):
        return Employee()

    def sorting_commands(self):
        return Commander(
            Command("1", "List all employees", self,
                    AirplaneSortingMethods.ALL_AIRPLANES),
            Command("2", "List all pilots", self,
                    AirplaneSortingMethods.ONLY_NOT_IN_USE),
            Command("3", "List all assistants", self,
                    AirplaneSortingMethods.ONLY_IN_USE),
            Command("4", "Sort by name", self,
                    AirplaneSortingMethods.BY_MANUFACTURER),
            Command("b", "Back to " + self.asset + " list", self),
        )


class AirplaneMenu(Asset):
    def __init__(self, mother, sorting_method=0):
        self.asset = "Airplane"
        self.logic = AirplaneLL()
        self.sorting_method = sorting_method
        super().__init__(mother)

    def new(self):
        return Airplane()

    def sorting_commands(self):
        return Commander(
            Command("1", "Find all Airplanes", self,
                    AirplaneSortingMethods.ALL_AIRPLANES),
            Command("2", "Airplanes not in use", self,
                    AirplaneSortingMethods.ONLY_NOT_IN_USE),
            Command("3", "Airplanes in use", self,
                    AirplaneSortingMethods.ONLY_IN_USE),
            Command("4", "Sort by Manufacturer", self,
                    AirplaneSortingMethods.BY_MANUFACTURER),
            Command("b", "Back to " + self.asset + " list", self),
        )


class DestinationMenu(Asset):
    def __init__(self, mother):
        self.asset = "Destination"
        self.logic = DestinationLL()
        super().__init__(mother)

    def commander(self):
        return super().commander(False)

    def new(self):
        return Destination()


class VoyageMenu(Asset):
    def __init__(self, mother):
        self.asset = "Voyage"
        self.logic = VoyageLL()
        super().__init__(mother)

    def commander(self):
        return super().commander(False)

    def new(self):
        return Voyage()


class EditingMenu(Menu):
    def __init__(self, mother, focused_asset, creating=False):
        self.creating = creating
        if creating:
            self.focused_asset = mother.new()
            self._title = "New"
            self.editable_fields = self.focused_asset.get_creation_fields()
        else:
            self.focused_asset = focused_asset
            self._title = "Update"
            self.editable_fields = self.focused_asset.get_updatable_fields()
        self.mother = mother
        self.asset_fields = self.focused_asset.get_print_info()
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
        input_type = self.mother.logic.get_field_input_type(self._valid_index())
        if input_type != str:
            result.add(Command("pa", "Pick " + input_type.__name__(), SelectionMenu, (self, get_menu_from_type(input_type))))
        return result

    def _confirm(self):
        self.focused_asset.update_info(self.asset_fields)
        if self.creating:
            self.mother.logic.add(self.focused_asset)
            self.mother.logic.set_final_page()
        return self.mother

    def has_list(self):
        return True

    def _valid_index(self):
        return self.editable_fields[self.current_index]

    def listing(self):
        header_list = self.focused_asset.get_header()
        return "\n".join([
            "{:>17}: {}{}".format(header, info,
                                  " <---" if i == self._valid_index() else "")
            for i, (header,
                    info) in enumerate(zip(header_list, self.asset_fields))
        ])

    def prompt(self):
        return "Enter {}: ".format(
            self.focused_asset.get_header()[self.current_index])

    def handle_input(self, user_input):
        command = self.commander().has(user_input)
        if command == None:
            # self.mother.logic.is_valid_input(self._valid_index(), user_input)
            self.asset_fields[self._valid_index()] = user_input
            self._with_shifted_field(1)
            return self
        return command.invoke()

    def _with_shifted_field(self, change):
        self.current_index = (self.current_index + change) % len(self.editable_fields)
        return self


class SelectionMenu(Asset):
    def __init__(self, mother, sibling):
        self.mother = mother
        self.sibling = sibling(self.mother)
        self.asset = self.sibling.asset
        self.logic = self.sibling.logic

    def commander(self):
        return Commander(
            Command("b", "Back to editing menu", lambda: self.mother)
        )

    def handle_input(self, user_input):
        if user_input.isdigit(
        ) and 0 < int(user_input) <= self.logic.current_page_size():
            # pass the selected asset to the new editing menu
            self.mother.asset_fields[self.mother._valid_index()] = self.logic.get_asset_at(int(user_input)).get_id()
            return self.mother
        else:
            return self._invoke_comand(user_input)
        return self

def get_menu_from_type(input_type):
    if input_type == Airplane:
        return AirplaneMenu
    if input_type == Destination:
        return DestinationMenu
    if input_type == Employee:
        return EmployeeMenu
    if input_type == Voyage:
        return VoyageMenu
