from AirplaneLL import AirplaneLL
from ModelFolder.Airplane import Airplane
from HelperUI import HelperUI

class AirplaneUI:
    ALL = 1
    MANUFACTURER = 2

    def __init__(self):
        self.LL = AirplaneLL()
        self.HUI = HelperUI()
    

    def list_airplanes(self, sorting_type=1):
        if sorting_type == AirplaneUI.ALL:
            airplane_list = self.LL.get_all()
        elif sorting_type == AirplaneUI.MANUFACTURER:
            airplane_list = self.LL.get_manufacturer()


        title = "Airplane List"
        instruction_list = ["c. Create new Airplane", "s. Select Sorting Method", "b. Back to Main Menu"]
        current_page = 1

        num_pages = len(airplane_list) // self.HUI.PAGE_DELIMETER
        if len(airplane_list) % self.HUI.PAGE_DELIMETER != 0:
            num_pages += 1
        if num_pages == 0:
            num_pages += 1

        while True:
            self.HUI.list_screen(airplane_list, title, instruction_list, current_page, num_pages)

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
                        self.display_airplane(airplane_list[(current_page - 1) * self.HUI.PAGE_DELIMETER + int(user_input) - 1])
                    except:
                        pass

            elif user_input == "c":
                return self.create_airplane()

            elif user_input == "s":
                return self.airplane_sorting()

            elif user_input == "b":
                return
        
    def display_airplane(self, airplane):
        while True:
            print("\n" * 30)
            print("------ Display Airplane ------")
            self.HUI.display_info(airplane, None)
            print("------------------------------")
            print("  u. Update Airplane")
            print("  v. View Work Plan")
            print("  b. Back to Previous Screen")
            print("------------------------------")
            print("\n" * 5)

            user_input = input("Enter Command: ")

            if user_input == "u":
                self.update_airplane(airplane)

            elif user_input == "b":
                return


    def airplane_sorting(self):
        print("\n" * 30)
        print("------ Sorting Methods ------")
        print("  1. Find all Airplanes")
        print("  2. Sort by Manufacturer")
        print("  3. Airplanes not in Use")
        print("  4. Airplanes in Use")
        print("-----------------------------")
        print("\n" * 5)

        user_input = input("Input Command: ")

        if user_input == "1":
            return self.list_airplanes(AirplaneUI.ALL)
        
        elif user_input == "2":
            return self.list_airplanes(AirplaneUI.MANUFACTURER)
        
        elif user_input == "3":
            pass
        
        elif user_input == "4":
            pass

        elif user_input == "b":
            return


    def create_airplane(self):
        new_airplane = Airplane()

        key_list = new_airplane.get_keys()
        header_list = new_airplane.get_header()
        current_index = 0

        while True:
            print("\n" * 30)
            print("------ New Airplane ------")
            self.HUI.display_info(new_airplane, current_index)
            print("--------------------------")
            print("\n" * 5)

            user_input = input("Enter {}: ".format(header_list[current_index]))

            if current_index == 0 and (user_input == "" or not user_input.isalpha()):
                pass

            else:
                new_airplane.info_dict[key_list[current_index]] = user_input
                current_index += 1
            
            if current_index == len(header_list):
                self.LL.add_airplane(new_airplane)
                return self.list_airplanes(AirplaneUI.ALL)
            print(new_airplane.info_dict)
        
    
    def update_airplane(self, airplane):
        key_list = airplane.get_keys()
        header_list = airplane.get_header()
        current_index = 2

        while True:
            print("\n" * 30)
            print("------ Update Airplane ------")
            self.HUI.display_info(airplane, current_index)
            print("-----------------------------")
            print(" Leave Empty to keep Current")
            print("-----------------------------")
            print("\n" * 5)

            user_input = input("Enter {}: ".format(header_list[current_index]))

            if user_input != "":
                airplane.info_dict[key_list[current_index]] = user_input
            
            current_index += 1

            if current_index == len(header_list):
                self.LL.save_airplanes()