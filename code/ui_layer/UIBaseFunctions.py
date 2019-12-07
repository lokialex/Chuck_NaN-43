class UIBaseFunctions():
    UI_DIVIDER_INT = 124
    DEVIATION_INT = 2
    LINE_LEN = 88
    WALL = "|"
    T_LEN = 18
    TRUE_LEN = LINE_LEN + 2 * T_LEN
    distinguisher = "{}\n{}\n\n".format("_"*TRUE_LEN, "_"*TRUE_LEN)

    def print_nan_airlines(self):
        print(self.distinguisher)
        print(self.T_LEN*" " + "███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗")
        print(self.T_LEN*" " + "████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝")
        print(self.T_LEN*" " + "██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗")
        print(self.T_LEN*" " + "██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗██║     ██║██║╚██╗██║██╔══╝  ╚════██║")
        print(self.T_LEN*" " + "██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║███████╗██║██║ ╚████║███████╗███████║")
        print(self.T_LEN*" " + "╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")
        print(self.distinguisher, end="")

    def __init__(self):
        pass

    def back(self):
        return 9

    def home(self):
        return 0

    def exit_program(self):
        exit()

    def get_user_selection(self, collection, key_word = "selection"):
        while True:
            try:
                selection = int(input("Enter {}: ".format(key_word)))
                if selection in collection:
                    return selection
                elif len(collection) >= selection:
                    return selection
                else:
                    print("Invalid {}".format(key_word))
            except ValueError:
                print("Invalid input")

    def check_return_value(self, return_value):
        if return_value == 0:
            return 0
        if return_value == 9:
            return 9
        return return_value

    def display_menu(self, menu_str, nav_dict, model_list=None, return_menu_str="9. Return 0. Home"):
        while True:
            print("-" * self.UI_DIVIDER_INT)
            print("|{}{}{}|".format(menu_str, " "*(self.UI_DIVIDER_INT - len(menu_str) -
                                                   len(return_menu_str) - self.DEVIATION_INT), return_menu_str))
            print("-" * self.UI_DIVIDER_INT)
            return_value = self.get_user_selection(nav_dict)
            if model_list == None:
                return_value = nav_dict[return_value]()
                return_value = self.check_return_value(return_value)
                if return_value == 0:
                    return 0
                if return_value == 9:
                    return
                if return_value != None:
                    return return_value

    def print_model_list(self, model_list, modelAPI, header_flag):

        print("-" * self.UI_DIVIDER_INT)
        print(modelAPI.get_model_header_format(model_list[0], header_flag))
        print(modelAPI.get_model_list_info(model_list, header_flag))
        print("-" * self.UI_DIVIDER_INT)
        return self.check_return_value(model_list)

    def print_model(self, model):
        print("-" * self.UI_DIVIDER_INT)
        print(model)
        print("-" * self.UI_DIVIDER_INT)
        return_value = model.display_edit_menu()
        return self.check_return_value(model)

    def select_from_model_list(self, model_list):
        return_value = self.get_user_selection(model_list, "index")
        return_value = self.print_model(model_list[return_value])


    