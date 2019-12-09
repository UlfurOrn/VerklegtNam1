from HelperUI import HelperUI

class UserInterface:
    def __init__(self, logicLayer):
        self.LL = logicLayer
        self.HUI = HelperUI()

    def list_self(self):
        asset_list = self.LL.get_all()

        title = "Asset List"
        instruction_list = ["c. Create new Asset", "b. Back to Main Menu"]
        current_page = 1

        num_pages = len(asset_list) // self.HUI.PAGE_DELIMETER
        if len(asset_list) % self.HUI.PAGE_DELIMETER != 0:
            num_pages += 1
        if num_pages == 0:
            num_pages += 1

        while True:
            self.HUI.list_screen(asset_list, title, instruction_list, current_page, num_pages)

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
                if int(user_input) >= 1 and int(user_input) <= self.HUI.PAGE_DELIMETER:
                    try:
                        self.display_asset(asset_list[(current_page - 1) * self.HUI.PAGE_DELIMETER + int(user_input) - 1])
                    except:
                        pass

            elif user_input == "c":
                return self.create_asset()

            elif user_input == "b":
                return
