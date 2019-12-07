class LLDestinations:
    DESTINATION_EDIT_CONTACT_NAME_FLAG = 0
    def __init__(self, DLAPI, modelAPI):
        self.__dl_api = DLAPI
        self.__modelAPI = modelAPI
        self.__all_destination_list = []


    def pull_all_destinations(self):
        ''' Gets a list of destination instances and returns it '''
        return self.__dl_api.pull_all_destinations()

    def push_all_destinations(self, all_destination_list):
        ''' Takes a list of destination instances and sends it to the DL ''' 
        self.__dl_api.overwrite_all_destinations(all_destination_list)

    def validate_destination(self, destination):
        ''' Gets destination instance and returns a boolean '''
        return self.__modelAPI.validate_model(destination)

    def edit_destination(self, destination, input_tpl):
        ''' Gets an instance and a tuple that holds a input flag and input string,
            calls a set function depending on flag and returns a boolean '''

        set_contact_info_dict = {0:destination.set_contact_name, 1:destination.set_contact_number}
        success_check = set_contact_info_dict[input_tpl[0]](input_tpl[1])
        if success_check:
            self.push_all_destinations(self.__all_destination_list)
        return success_check

    def get_one_destination(self, airport):
        ''' Gets input from UI layer and returns an instance '''
        self.__all_destination_list = self.get_all_destinations()

        for destination in self.__all_destination_list:
            if destination.get_airport() == airport:
                return destination


