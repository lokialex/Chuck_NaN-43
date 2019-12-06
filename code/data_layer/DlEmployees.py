import os
from os import path
class DLEmployees():
    SSN = 0
    NAME = 1
    ADDRESS = 2
    HOME_NUMBER = 3
    MOBILE_NUBER = 4
    EMAIL = 5
    TITLE = 6
    RANK = 7
    LICENSE = 8

    def __init__(self, modelAPI):
        
        self.__modelAPI = modelAPI

    def pull_all_employees(self):
        '''Opens a csv and returns a list of all employees (ssn, name, address, home number, mobile number, e-mail, rank, title)'''
        if path.exists('./repo/employees.csv') and path.exists('./repo/employees_temp.csv'):
            filestream = open("./repo/employees.csv", "r")
            os.remove("./repo/employees_temp.csv")
        elif  path.exists('./repo/employees.csv') and path.exists('./repo/employees_temp.csv') == False:
            filestream = open("./repo/employees.csv", "r")
        elif path.exists('./repo/employees.csv') == False and path.exists('./repo/employees_temp.csv'):
            filestream = open("./repo/employees_temp.csv", "r")
        else:
            print("employee data files not found")
            return

        self.all_crew_list = []
        for line in filestream:
            line_list = line.strip().split(",")
            new_emp = self.__modelAPI.get_model('Employee')
            
            new_emp.set_ssn(line_list[DLEmployees.SSN])
            new_emp.set_name(line_list[DLEmployees.NAME])
            new_emp.set_address(line_list[DLEmployees.ADDRESS])
            new_emp.set_home_num(line_list[DLEmployees.HOME_NUMBER])
            new_emp.set_mobile_num(line_list[DLEmployees.MOBILE_NUBER])
            new_emp.set_email(line_list[DLEmployees.EMAIL])
            new_emp.set_rank(line_list[DLEmployees.RANK])
            new_emp.set_title(line_list[DLEmployees.TITLE])
            new_emp.set_licence(line_list[DLEmployees.LICENSE])

            self.all_crew_list.append(new_emp)
        filestream.close()

        return self.all_crew_list[1:]

    def push_all_employees(self, emp_list):
        
        # employee_file.write(new_emp_str)
        HEADER = "id,ssn,name,address,homenumber,mobilenumber,email,role,rank,licence\n"
        filestream2 = open("./repo/employees_temp.csv", "a")
        filestream2.write(HEADER)
        for emp_info in emp_list:
            filestream2.write(emp_info.raw_info())
        filestream2.close()
        os.remove("./repo/employees.csv")
        os.rename("./repo/employees_temp.csv", "./repo/employees.csv")
        return
        
    def append_employee(self,employee):
        employee_stream = open('./repo/employees.csv', 'a')
        emp_str = employee.raw_info()
        employee_stream.write(emp_str)
        employee_stream.close()
        return        
