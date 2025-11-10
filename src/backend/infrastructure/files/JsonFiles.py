import os
import json 

class JsonFiles:
    def __init__(self):
        pass

    def get_elections_data(self):
        elections_results = {}
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(base_dir, "data.json")
        with open(file, "r", encoding="utf-8") as f:
            elections_results = json.load(f)
            #elections_results = json.loads(data_json)
        return elections_results["elections_results"]