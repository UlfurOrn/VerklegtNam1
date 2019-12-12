from UILayer.EmployeeUI import EmployeeUI
from UILayer.DestinationUI import DestinationUI
from UILayer.AirplaneUI import AirplaneUI

class OherUI:

    def __init__(self):
        self.EmployeeUI = EmployeeUI()
        self.DestinationUI = DestinationUI()
        self.AirplaneUI = AirplaneUI()
    
    def main_menu(self):
        
        while True:
            print("\n" * 30)
            print("------ Main Menu ------")
            print("   1. Employees")
            print("   2. Airplanes")
            print("   3. Destinations")
            print("   4. Voyages")
            print("-----------------------")
            print("\n" * 5)

            user_input = input("Input Command: ")

            if user_input == "1":
                self.EmployeeUI.list_employees()
            
            elif user_input == "2":
                self.AirplaneUI.list_airplanes()

            elif user_input == "3":
                self.DestinationUI.list_destinations()

            elif user_input == "4":
                pass

            elif user_input == "q":
                break
