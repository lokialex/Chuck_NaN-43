from datetime import datetime
from datetime import timedelta
class LLVoyages:
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_voyage_list = []

    def get_all_voyage_list(self):
        self.__all_voyage_list = self.__dl_api.pull_all_voyages()
        self.check_status(self.__all_voyage_list)
        self.check_staffed(self.__all_voyage_list)
        return self.__all_voyage_list

    def overwrite_all_voyages(self, voyage_list):
        return self.__dl_api.overwrite_all_voyages(voyage_list)

    def filter_all_empty_voyages(self):
        '''Takes a list of all voyage instances and returns a list of filtered voyage instances'''
        self.get_all_voyage_list() 
        empty_voyage_list = []

        for voyage in self.__all_voyage_list:
            if voyage.get_airplane_insignia() == ".":
                empty_voyage_list.append(voyage)

        return empty_voyage_list

    def filter_all_voyages_by_period(self, start_date, end_date):
        '''Takes a list of all voyage instances and returns a list of voyages filteres by period'''

        start = self.get_iso_format_date_time(start_date)
        end = self.get_iso_format_date_time(end_date)

        self.get_all_voyage_list() 
        period_voyage_list = []

        for voyage in self.__all_voyage_list:
            if start <= self.get_iso_format_date_time(voyage.get_return_flight_arrival_date()) and self.get_iso_format_date_time(voyage.get_departing_flight_departure_date()) <= end:
                period_voyage_list.append(voyage)
        return period_voyage_list
        
    def filter_all_voyages_by_airport(self, airport):

        self.__all_voyage_list = self.get_all_voyage_list()
        airport_voyage_list = []

        for voyage in self.__all_voyage_list:
            if voyage.get_return_flight_departing_from() == airport:
                airport_voyage_list.append(voyage)

        return airport_voyage_list

    def create_voyage(self, destination, start_date, start_time = "00:00:00"):

        self.get_all_voyage_list()

        try:
            fixed_date = datetime.strptime(start_date, '%d-%m-%Y')
            fixed_time = datetime.strptime(start_time, '%H:%M:%S').time()
        except ValueError:
            return False

        fixed_date_time = datetime.combine(fixed_date, fixed_time)
        new_voyage = self.__modelAPI.get_model("Voyage")

        new_voyage.set_return_flight_departing_from(destination.get_airport())
        new_voyage.set_departing_flight_departure_date(fixed_date_time.isoformat())
        new_voyage.set_airplane_insignia(".")
        new_voyage.set_captain_ssn(".")
        new_voyage.set_copilot_ssn(".")
        new_voyage.set_fsm_ssn(".")
        new_voyage.set_fa_ssns([".", "."])

        dep_flight_num, ret_flight_num = self.generate_flight_numbers() 
        new_voyage.set_flight_numbers(dep_flight_num, ret_flight_num)

        departing_flight_arrival_date, return_flight_departure_date, return_flight_arrival_date \
            = self.calculate_flight_times(fixed_date_time, destination.get_airport())
        
        departing_flight_arrival_date_str, return_flight_departure_date_str, return_flight_arrival_date_str \
            = str(departing_flight_arrival_date), str(return_flight_departure_date), str(return_flight_arrival_date)
        
        new_voyage.set_flight_times(departing_flight_arrival_date_str, \
            return_flight_departure_date_str, return_flight_arrival_date_str)

        start_date = fixed_date_time.isoformat()
        end_date = new_voyage.get_return_flight_arrival_date()

        for voyage in self.__all_voyage_list:
            other_start_date = voyage.get_departing_flight_departure_date()
            other_end_date = voyage.get_return_flight_arrival_date()
            
            if other_start_date == start_date or other_start_date == end_date or\
                other_end_date == start_date or other_end_date == end_date:
                return False

        if self.__modelAPI.validate_model(new_voyage):
            return self.__dl_api.append_voyage(new_voyage)

        return False

    def duplicate_voyage(self, voyage, start_date, start_time = "00:00:00"):
        '''Copies a voyage to another date'''

        destination = voyage.get_destination()
        return self.create_voyage(destination, start_date, start_time)

    def repeat_voyage(self, voyage, repeat_interval, end_date):
        date = self.get_iso_format_date_time(voyage.get_departing_flight_departing_date())
        end_date = self.get_iso_format_date_time(end_date)
        while date <= end_date:
            date =+ repeat_interval
            success = self.duplicate_voyage(voyage, date)
        return success

    def populate_voyage(self):
        pass

    def generate_flight_numbers(self):
        self.__all_voyage_list = self.get_all_voyage_list()
        existing_numbers = []
        for voyage in self.__all_voyage_list:
            existing_numbers.append(int(voyage.get_departing_flight_num().replace("NA","")))
            existing_numbers.append(int(voyage.get_return_flight_num().replace("NA","")))

        departing_number_int = max(existing_numbers)+ 1
        arriving_number_int = max(existing_numbers) + 2
        arriving_number_str = str(arriving_number_int)
        departing_number_str = str(departing_number_int)

        while len(departing_number_str) < 4:
            departing_number_str = "0" + departing_number_str
        while len(arriving_number_str) < 4:
            arriving_number_str = "0" + arriving_number_str
        return "NA" + departing_number_str, "NA" + arriving_number_str

    def calculate_flight_times(self,date,airport):
        self.__all_voyage_list = self.get_all_voyage_list()
        destinations_list = self.__dl_api.pull_all_destinations()
        destinations_dict = dict()
        
        for destination in destinations_list:
            destinations_dict[destination.get_airport()] = int(destination.get_flight_time())
        
        flight_time = destinations_dict[airport]
        departing_flight_arrival_date = date + timedelta(hours =flight_time)
        return_flight_departure_date = departing_flight_arrival_date + timedelta(hours = 1)
        return_flight_arrival_date = return_flight_departure_date + timedelta(hours = flight_time)
        return departing_flight_arrival_date.isoformat(), return_flight_departure_date.isoformat(), return_flight_arrival_date.isoformat()
         
    def filter_available_employees(self, rank, voyage):

        start_date = voyage.get_departing_flight_departure_date()
        end_date = voyage.get_return_flight_arrival_date()
        voyages_in_date_range_list = self.filter_all_voyages_by_period(start_date, end_date)

        all_employee_list = self.__dl_api.pull_all_employees()

        filter_rank_list = [(employee) for employee in all_employee_list if employee.get_rank() == rank]

        available_employee_list = []

        for other_voyage in voyages_in_date_range_list:   
            voyage_ssn = other_voyage.get_voyage_employee_ssn(rank)
            for employee in filter_rank_list:
                if employee not in available_employee_list:
                    employee_ssn = employee.get_ssn()
                    if type(voyage_ssn).__name__ == "list":
                        if employee_ssn not in voyage_ssn:
                            available_employee_list.append(employee)
                            
                    else:
                        if employee_ssn != voyage_ssn:
                            available_employee_list.append(employee)

        final_employee_list = available_employee_list    
        
        if rank == "Captain" or rank == "Copilot":
            final_employee_list = []
            for airplane in self.__dl_api.pull_all_airplanes():
                if airplane.get_insignia() == voyage.get_airplane_insignia():
                    selected_airplane = airplane
                    break

            airplane_type = "NA" + selected_airplane.get_make() + selected_airplane.get_model()

            for employee in available_employee_list: 
                if employee.get_licence() == airplane_type:
                    final_employee_list.append(employee)

        return final_employee_list
            

    def check_status(self, voyage_list):
        current_date = datetime.today()
        for voyage in voyage_list:
            departing_flight_departure_date = self.get_iso_format_date_time(voyage.get_departing_flight_departure_date())
            departing_flight_arrival_date = self.get_iso_format_date_time(voyage.get_departing_flight_arrival_date())
            return_flight_departure_date = self.get_iso_format_date_time(voyage.get_return_flight_departure_date())
            return_flight_arrival_date = self.get_iso_format_date_time(voyage.get_return_flight_arrival_date())

            if current_date <= departing_flight_departure_date:
                voyage.set_status("Not started")
            elif departing_flight_departure_date <= current_date <= departing_flight_arrival_date:
                voyage.set_status("Flying to {}".format(voyage.get_return_flight_departing_from()))
            elif departing_flight_arrival_date <= current_date <= return_flight_departure_date:
                voyage.set_status("Currently in {}".format(voyage.get_return_flight_departing_from()))
            elif return_flight_departure_date <= current_date <= return_flight_arrival_date:
                voyage.set_status("Flying to {}".format(voyage.get_departing_flight_departing_from()))
            else:
                voyage.set_status("Voyage completed")
    
    def check_staffed(self, voyage_list):
        for voyage in voyage_list:
            if voyage.get_airplane_insignia() != "." and voyage.get_captain_ssn() != "." and voyage.get_copilot_ssn() != "." and voyage.get_fsm_ssn() != "." and voyage.get_fa_ssns() != ".:.":
                voyage.set_staffed("Staffed")
            else:
                voyage.set_staffed("Not staffed")

    def get_iso_format_date_time(self, date=''):

        if date.find("T") == -1:
            new_date = datetime.strptime(date,'%Y-%m-%d')
        else:
            new_date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
        return new_date