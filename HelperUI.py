from Employee import Employee

class HelperUI:
    PAGE_DELIMETER = 9
    ARROW = "  <---"

    def __init__(self):
        pass

    
    def list_screen(self, asset_list, title, instruction_list, current_page, num_pages):
        print("\n" * 30)
        print("------", title, "------")

        for i in range(HelperUI.PAGE_DELIMETER):
            try:
                print("  {}: {}".format(i + 1, asset_list[(current_page - 1) * HelperUI.PAGE_DELIMETER + i].get_summary()))
            except IndexError:
                print("")

        print("-" * (14 + len(title)))

        for instruction in instruction_list:
            print("  {}".format(instruction))
        print("-" * (14 + len(title)))

        print("prev(a) Page: {:>2}/{:<2} next(d)".format(current_page, num_pages))

        print("-" * (14 + len(title)))
        print("\n" * 5)



    def display_info(self, asset, current_index):
        key_list = asset.get_keys()
        header_list = asset.get_header()

        arrow_pos = [HelperUI.ARROW if current_index == pos else "" for pos in range(len(header_list))]

        for header, key, arrow in zip(header_list, key_list, arrow_pos):
            print("{:>13}: {}{}".format(header, asset.info_dict[key], arrow))





