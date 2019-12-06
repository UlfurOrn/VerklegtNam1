class UserInterface:
    def __init__(self, airline):
        self.current_prompt = "hello: "
        self.airline = airline
        # self.input_loop(self)

    # The main input loop
    def input_loop(self):
        user_input = input(self.current_prompt)

    def main_menu(self):
        while True:
            print("\n" * 30)
            print("-------- Main Menu --------")
            print("      1. Employees")
            print("      2. Destinations")
            print("      3. Airplanes")
            print("      4. Voyages")
            print("---------------------------")
            print("\n" * 5)

            user_input = input("Enter command: ")

            if user_input == "1":
                self.list_employees(self.airline.get_all())
            elif user_input == "2":
                print("Destinations")
            elif user_input == "3":
                print("Airplanes")
            elif user_input == "4":
                print("Voyages")
            elif user_input == "q":
                break


    def list_employees(self, employee_dict_list):
        title = "Employee List"
        instructions = ["   c. Create New Employee", "   s. Select Sorting Method", "   b. Back to Main Menu"]
        current_page = 1

        num_pages = len(employee_dict_list) // UserInterface.PAGE_DELIMETER
        if len(employee_dict_list) % UserInterface.PAGE_DELIMETER != 0:
            num_pages += 1

        while True: 
            self.display_screen(title, employee_dict_list, instructions, current_page, num_pages)

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
                self.display_employee(employee_dict_list[(current_page - 1) * 9 + int(user_input) - 1])

            elif user_input == "s":
                return self.select_sorting()

            elif user_input == "b":
                return
    

    def display_employee(self, employee_dict):
        while True:
            print("\n" * 30)
            print("----- Display Employee -----")
            for title, info in employee_dict.items():
                print("{:>10}: {}".format(title, info))
            print("----------------------------")
            print("\n" * 5)

            user_input = input("Enter command:")

            if user_input == "b":
                return


    def display_screen(self, title, dict_list, instructions, current_page, num_pages):

        screen_length = 14 + len(title)

        print("\n" * 30)
        print("------", title, "------")
        for index in range(UserInterface.PAGE_DELIMETER):
            try:
                print(dict_list[(current_page - 1) * UserInterface.PAGE_DELIMETER + index].get_summary())
            except IndexError:
                print("")
        print("-" * screen_length)
        for instruction in instructions:
            print(instruction)
        print("-" * screen_length)
        print("prev(a) Page: {:>2}/{:<2} next(d)".format(current_page, num_pages))
        print("-" * screen_length)
    
    def select_sorting(self):
        while True:
            print("\n" * 30)
            print("------ Sorting Methods ------")
            print("   1. List All Employees")
            print("   2. List All Pilots")
            print("-----------------------------")
            print("\n" * 5)

            user_input = input("Enter command: ")

            if user_input == "1":
                return self.list_employees(self.airline.get_all())

            elif user_input == "2":
                return self.list_employees(self.airline.get_pilots())
            
            elif user_input == "b":
                return



#UserInterface.display_assets([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18],9)


#ui = UserInterface()
#ui.main_menu()
