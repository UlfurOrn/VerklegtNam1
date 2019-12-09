from EmployeeLL import EmployeeLL
from Employee import Employee
from HelperUI import HelperUI

class EmployeeUI:
    ALL = 1
    PILOTS = 2
    ATTENDANTS = 3

    def __init__(self):
        self.LL = EmployeeLL()
        self.HUI = HelperUI()
    

    def list_employees(self, sorting_type=1):
        if sorting_type == EmployeeUI.ALL:
            employee_list = self.LL.get_all()
        elif sorting_type == EmployeeUI.PILOTS:
            employee_list = self.LL.get_pilots()
        elif sorting_type == EmployeeUI.ATTENDANTS:
            employee_list = self.LL.get_attendants()

        title = "Employee List"
        instruction_list = ["c. Create new Employee", "s. Select Sorting Method", "b. Back to Main Menu"]
        current_page = 1

        num_pages = len(employee_list) // self.HUI.PAGE_DELIMETER
        if len(employee_list) % self.HUI.PAGE_DELIMETER != 0:
            num_pages += 1
        if num_pages == 0:
            num_pages += 1

        while True:
            self.HUI.list_screen(employee_list, title, instruction_list, current_page, num_pages)

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
                    self.display_employee(employee_list[(current_page - 1) * self.HUI.PAGE_DELIMETER + int(user_input) - 1])

            elif user_input == "c":
                return self.create_employee()

            elif user_input == "s":
                return self.employee_sorting()

            elif user_input == "b":
                return
        
    def display_employee(self, employee):
        while True:
            print("\n" * 30)
            print("------ Display Employee ------")
            self.HUI.display_info(employee)
            print("------------------------------")
            print("  u. Update Employee")
            print("  v. View Work Plan")
            print("  b. Back to Previous Screen")
            print("------------------------------")
            print("\n" * 5)

            user_input = input("Enter Command: ")

            if user_input == "u":
                self.update_employee(employee)

            elif user_input == "b":
                return


    def employee_sorting(self):
        print("\n" * 30)
        print("------ Sorting Methods ------")
        print("  1. Find all Employees")
        print("  2. Find all pilots")
        print("  3. Find all Attendants")
        print("  4. Employees not Working")
        print("  5. Employees Working")
        print("-----------------------------")
        print("\n" * 5)

        user_input = input("Input Command: ")

        if user_input == "1":
            return self.list_employees(EmployeeUI.ALL)
        
        elif user_input == "2":
            return self.list_employees(EmployeeUI.PILOTS)
        
        elif user_input == "3":
            return self.list_employees(EmployeeUI.ATTENDANTS)
        
        elif user_input == "4":
            pass
        
        elif user_input == "5":
            pass

        elif user_input == "b":
            return


    def create_employee(self):
        new_employee = Employee()
        key_list = new_employee.get_keys()
        header_list = new_employee.get_header()
        current_index = 0

        while True:
            print("\n" * 30)
            print("------ New Employee ------")
            self.HUI.display_info(new_employee, current_index)
            print("--------------------------")
            print("\n" * 5)

            user_input = input("Enter {}: ".format(header_list[current_index]))

            if current_index == 0 and (user_input == "" or not user_input.isalpha()):
                pass

            else:
                new_employee.info_dict[key_list[current_index]] = user_input
                current_index += 1
            
            if current_index == len(header_list):
                self.LL.add_employee(new_employee)
                return self.list_employees(EmployeeUI.ALL)
        
    
    def update_employee(self, employee):
        key_list = employee.get_keys()
        header_list = employee.get_header()
        current_index = 2

        while True:
            print("\n" * 30)
            print("------ Update Employee ------")
            self.HUI.display_info(employee, current_index)
            print("-----------------------------")
            print(" Leave Empty to keep Current")
            print("-----------------------------")
            print("\n" * 5)

            user_input = input("Enter {}: ".format(header_list[current_index]))

            if user_input != "":
                employee.info_dict[key_list[current_index]] = user_input
            
            current_index += 1

            if current_index == len(header_list):
                self.LL.save_employees()
                

