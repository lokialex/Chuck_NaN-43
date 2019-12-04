from data_layer.DLAPI import DLAPI
from models.Airplane import Airplane
from models.Destination import Destination
from models.Voyage import Voyage
from models.Employee import Employee
from models.FlightAttendant import FlightAttendant
from models.Pilot import Pilot


class LLEmployees:
    def __init__(self):
        self.dl_api = DLAPI()

    def validate_employee(self):
        pass

    def get_employee_by_ssn(self, ssn):
        ''' pulls a list of employee instances and returns a instance of employee by employee_ID '''

        employee_list = self.dl_api.populate_all_employees()
        for employee in employee_list:
            if employee.get_employee_by_ssn() == ssn:
                return employee

    def get_all_employees(self):
        ''' pulls and returns a list of employee instances '''
        return self.dl_api.populate_all_employees()

    def filter_all_employees_by_date(self):
        pass

    def filter_all_employees_by_ssn(self):
        # employee_list = self.get_all_employees()
        # for employee in employee_list[1:]:
        pass

    def filter_all_employees_by_title(self, title):
        '''takes list of all employees and returns list of employees filtered by title from input'''
        filter_list = []
        employee_list = self.dl_api.populate_all_employees()
        for employee in employee_list:
            if employee.get_title() == title:
                filter_list.append(employee)
        return filter_list

    def filter_pilots_by_airplane_type(self, airplane_type):
        pass

    def sort_pilots_bu_airplane_type(self):
        pass

    def create_work_scedule(self):
        pass
