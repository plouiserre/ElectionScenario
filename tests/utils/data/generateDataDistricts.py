import json
from src.backend.domain.models.district import District

def build_first_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":502, \"department_name\" : \"Hautes-Alpes\", \"department_code\" : 5}"
    district = __construct_district_from_json(json_district)
    return district

def build_second_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}"
    district = __construct_district_from_json(json_district)
    return district

def build_third_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":2502, \"department_name\" : \"Doubs\", \"department_code\" : 25}"
    district = __construct_district_from_json(json_district)
    return district

def build_fourth_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}"
    district = __construct_district_from_json(json_district)
    return district

def build_fifth_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}"
    district = __construct_district_from_json(json_district)
    return district

def build_sixth_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":5502, \"department_name\" : \"Meuse\", \"department_code\" : 55}"
    district = __construct_district_from_json(json_district)
    return district

def build_seventh_district():
    json_district = "{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}"
    district = __construct_district_from_json(json_district)
    return district

def build_eleventh_district():
    json_district = "{\"name\":\"11ème circonscription\", \"code\":9311, \"department_name\" : \"Seine-Saint-Denis\", \"department_code\" : 93}"
    district = __construct_district_from_json(json_district)
    return district

def __construct_district_from_json(json_data):
    json_2 = json.loads(json_data)    
    district = District()
    district.code = json_2["code"]
    district.department_code = json_2["department_code"]
    district.department_name = json_2["department_name"]
    district.name = json_2["name"]
    return district