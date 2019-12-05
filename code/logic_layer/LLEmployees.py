class LLEmployees:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI

    def validate_employee(self):
        pass

    def get_all_employees(self):
        ''' pulls and returns a list of employee instances '''
        employee_list = self.__dl_api.populate_all_employees()
        employee_dict = {}
        index = 1
        for index, employee in enumerate(employee_list):
            employee_dict[index] = employee
        return employee_dict

    def get_ssn_dict(self):
        employee_dict = self.get_all_employees
        ssn_dict = {}
        for index, employee in employee_dict.items():
            ssn_dict[employee.get_ssn()] = index
        return ssn_dict

    def get_employee_by_ssn(self, ssn):
        ''' pulls a list of employee instances and returns a instance of employee by employee_ID '''
        ssn_dict = self.get_ssn_dict
        employee_id = ssn_dict[ssn]
        employee_dict = self.get_all_employees
        employee = employee_dict[employee_id]
        return employee

    def list_all_employees_by_date(self):
        pass

    def filter_all_employees_by_availability(self):
        pass

    def filter_all_employees_by_title(self, title):
        ''' Takes list of all employees and returns list of employees filtered by title from input '''
        filter_list = []
        employee_list = self.__dl_api.populate_all_employees()
        for employee in employee_list:
            if employee.get_title() == title:
                filter_list.append(employee)
        return filter_list

    def filter_pilots_by_airplane_type(self, airplane_type):
        pass

    def sort_pilots_by_airplane_type(self):
        pass

    def create_work_scedule(self):
        pass
