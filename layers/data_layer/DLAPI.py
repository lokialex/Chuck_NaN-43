from models import *

class DLAPI():
    def __init__(self):
        self.dl_employees = DLEmployees()
        self.dl_voyages = DLVoyages()
        self.dl_destinations = DLDestinations()
        self.dl_airplanes = DLAirplanes()

    def populate_all_employees(self):
        return self.dl_employees.pull_all_employees()


    def populate_all_voyages(self):
        return self.dl_voyages.pull_all_voyages()

    def populate_all_destinations(self):
        return self.dl_destinations.pull_all_destinations()

    def populate_all_airplanes(self):
        return self.dl_airplanes.pull_all_airplanes()