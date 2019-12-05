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
        while True:
            print("\n" * 30)
            print("------ Employee List ------")
            for i in range(len(employee_dict_list)):
                print("   {}: {}".format(i + 1, employee_dict_list[i]["name"]))
            print("---------------------------")
            print("\n" * 5)

            user_input = input("Enter command: ")

            if user_input == "b":
                return
            elif user_input.isdigit():
                self.display_employee(employee_dict_list[int(user_input) - 1])
    

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


    def display_assets(array, page_delimeter):
    	if len(array) % page_delimeter == 0:
    		page_amount = int(len(array)/page_delimeter)
    	else:
    		page_amount = (len(array)//page_delimeter)+1
    	print(page_amount)



#UserInterface.display_assets([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18],9)


#ui = UserInterface()
#ui.main_menu()
