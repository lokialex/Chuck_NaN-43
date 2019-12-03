from validation.validator import Validator

models_validation = Validator()


class Destination():
    def __init__(self, country='', airport='', flight_time='', distance='', contact_name='', contact_num=0):
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__contact_name = contact_name
        self.__contact_num = contact_num

    def __str__(self):
        return "Country: {:>2}\nAirport: {:>2}\nFlight time: {:>2}\nDistance: {:>2}\nContact name: {:>2}\nContact number: {:>2}".format(self.__country, self.__airport, self.__flight_time, self.__distance, self.__contact_name, self.__contact_num)

    def get_country(self):
        return self.__country

    def set_country(self, new_country):
        if models_validation.validate_destination_country:
            self.__country = new_country
        else:
            pass

    def get_airport(self):
        return self.__airport

    def set_airport(self, new_airport):
        if models_validation.validate_destination_airport:
            self.__airport = new_airport
        else:
            pass

    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, new_flight_time):
        if models_validation.validate_destination_flight_time:
            self.__flight_time = new_flight_time
        else:
            pass

    def get_distance(self):
        return self.__distance

    def set_distance(self, new_distance):
        if models_validation.validate_destination_distance:
            self.__distance = new_distance
        else:
            pass

    def get_contact_name(self):
        return self.__contact_name

    def set_contact_name(self, new_contact_name):
        if models_validation.validate_destination_contact_name:
            self.__contact_name = new_contact_name
        else:
            pass

    def get_contact_num(self):
        return self.__contact_num

    def set_contact_num(self, new_contact_num):
        if models_validation.validate_destination_contact_num:
            self.__contact_num = new_contact_num
        else:
            pass
