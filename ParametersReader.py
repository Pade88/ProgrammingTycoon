import json


class ParametersReader():
    def __init__(self, language_name):
        self.data = None
        with open(f"{language_name}_parameters.json") as input_data:
            self.data =  json.load(input_data)

    def get_data(self):
        return self.data

    def save_data(self, data):
        pass