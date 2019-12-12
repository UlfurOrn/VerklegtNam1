from DestinationLL import DestinationLL
from Destination import Destination
from HelperUI import HelperUI

class DestinationUI:

    def __init__(self):
        self.LL = DestinationLL()
        self.HUI = HelperUI()
    

    def list_destinations(self):
        destination_list = self.LL.get_all()

        title = "Destination List"
        instruction_list = ["c. Create new Destination", "b. Back to Main Menu"]
        current_page = 1

        num_pages = len(destination_list) // self.HUI.PAGE_DELIMETER
        if len(destination_list) % self.HUI.PAGE_DELIMETER != 0:
            num_pages += 1
        if num_pages == 0:
            num_pages += 1

        while True:
            self.HUI.list_screen(destination_list, title, instruction_list, current_page, num_pages)

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
                        self.display_destination(destination_list[(current_page - 1) * self.HUI.PAGE_DELIMETER + int(user_input) - 1])
                    except:
                        print("hello")
                        pass

            elif user_input == "c":
                return self.create_destination()

            elif user_input == "b":
                return
        
    def display_destination(self, destination):
        while True:
            print("\n" * 30)
            print("------ Display Destination ------")
            self.HUI.display_info(destination, None)
            print("------------------------------")
            print("  u. Update Destination")
            print("  b. Back to Previous Screen")
            print("------------------------------")
            print("\n" * 5)

            user_input = input("Enter Command: ")

            if user_input == "u":
                self.update_destination(destination)

            elif user_input == "b":
                return


    def create_destination(self):
        new_destination = Destination({"country": "", "airport": "", "abrev": "", "flight_time": "", "flight_dist": "", "contact_name": "", "contact_num": ""})
        key_list = new_destination.get_keys()
        header_list = new_destination.get_header()
        current_index = 0

        while True:
            print("\n" * 30)
            print("------ New Destination ------")
            self.HUI.display_info(new_destination, current_index)
            print("--------------------------")
            print("\n" * 5)

            user_input = input("Enter {}: ".format(header_list[current_index]))

            if current_index == 0 and (user_input == "" or not user_input.isalpha()):
                pass

            else:
                new_destination[key_list[current_index]] = user_input
                current_index += 1
            
            if current_index == len(header_list):
                self.LL.add(new_destination)
                return self.list_destinations()
        
    
    def update_destination(self, destination):
        key_list = destination.get_keys()
        header_list = destination.get_header()
        current_index = 2

        while True:
            print("\n" * 30)
            print("------ Update Destination ------")
            self.HUI.display_info(destination, current_index)
            print("-----------------------------")
            print(" Leave Empty to keep Current")
            print("-----------------------------")
            print("\n" * 5)

            user_input = input("Enter {}: ".format(header_list[current_index]))

            if user_input != "":
                destination[key_list[current_index]] = user_input
            
            current_index += 1

            if current_index == len(header_list):
                self.LL.save_destinations()
                

