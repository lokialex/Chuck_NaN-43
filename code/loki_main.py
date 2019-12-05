from logic_layer.LLAPI import LLAPI
from models.ModelAPI import ModelAPI
from ui_layer.UIBaseFunctions import UIBaseFunctions
from ui_layer.UIEmployees import UIEmployees

new_llapi = LLAPI()
new_modelapi = ModelAPI()
new_uibasefunctions = UIBaseFunctions()


new_ui_emp = UIEmployees(new_llapi, new_modelapi, new_uibasefunctions)
# new_ui_emp.display_employee_search_menu()
new_emp = new_ui_emp.get_employee_by_name("William Carillo")
# new_emp.set_ssn("1234567890")
# new_emp.set_email("hakon.stjani@nanair.is")
# print("")
# print(new_emp)


# new_ui_emp.display_all_employees()
