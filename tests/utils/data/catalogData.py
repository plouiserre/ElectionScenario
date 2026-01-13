from tests.utils.data.generateDataCongress import load_congress_very_stable, load_congress_stable, load_congress_quite_stable, load_congress_low_stable, load_congress_perfectly_representative, load_congress_good_representative, load_congress_quite_representative, load_congress_low_representative
from tests.utils.data.generateDataCongressPersons import load_all_candidates, load_candidates_from_name, load_congress_persons_by_departments
from tests.utils.data.generateDataDepartmentCongress import load_three_congress_departments
from tests.utils.data.generateDataDistricts import build_first_district, build_second_district, build_third_district, build_fourth_district, build_fifth_district, build_sixth_district, build_seventh_district, build_eleventh_district
from tests.utils.data.generateDataParties import load_all_parties, load_all_parties_with_candidates, load_all_parties_with_candidates_but_not_stability, load_all_parties_with_candidates_and_big_stability
from tests.utils.data.generateDataResults import load_json_districts_results, load_7_districts_results, load_20_perfect_districts_results, load_20_good_districts_results, load_20_quite_districts_results, load_20_low_districts_results, load_json_districts_three_departments_results, load_json_districts_departement_with_one_district_results, load_json_districts_department_with_three_districts_results, load_json_districts_department_with_twelve_districts_results, load_json_districts_three_departments_tmp_results, load_json_districts_three_departments_tmp_results_no_objects

__districts_keys = ["first_district", "second_district", "third_district", "fourth_district",
                    "fifth_district", "sixth_district", "seventh_district", "eleventh_district"]

def generate_datas(type_data, key):
    if type_data == "district":
        return __generate_district_datas(key)
    elif type_data == "candidate":
        return __generate_candidate_datas(key)
    elif type_data == "party" : 
        return __generate_party_datas(key)
    elif type_data == "congress":
        return __generate_congress_datas(key)
    elif type_data == "results_elections":
        return __generate_results_elections(key)
    elif type_data == "department_congress":
        return __generate_department_congress(key)
    return ""

def __generate_district_datas(key):
    if key == __districts_keys[0]:
        return build_first_district()
    elif key == __districts_keys[1]:
        return build_second_district()
    elif key == __districts_keys[2]:
        return build_third_district()
    elif key == __districts_keys[3]:
        return build_fourth_district()
    elif key == __districts_keys[4]:
        return build_fifth_district()
    elif key == __districts_keys[5]:
        return build_sixth_district()
    elif key == __districts_keys[6]:
        return build_seventh_district()
    else:
        return build_eleventh_district()   
    
def __generate_candidate_datas(key):
    if key == "groupby_district":
        return __load_all_candidates_by_district()
    elif "where_districtcode_" in key:
        return __load_all_candidates_from_specific_district(key)
    elif key == "by_department": 
        return load_congress_persons_by_departments()
    elif key == '': 
        return load_all_candidates()
    else :
        return load_candidates_from_name(key)
    
#TODO move the two method below
def __load_all_candidates_by_district():
    all_candidates = []
    all_candidates_by_districts = {}
    candidates = load_all_candidates()
    for candidate in candidates : 
        key = candidate.district.code
        if len(all_candidates_by_districts) > 0 and key in all_candidates_by_districts: 
            all_candidates_by_districts[key].append(candidate)
        else : 
            all_candidates_by_districts[key] = []
            all_candidates_by_districts[key].append(candidate)
    for key in all_candidates_by_districts: 
        candidates = all_candidates_by_districts[key]
        all_candidates.append(candidates)
    return all_candidates

def __load_all_candidates_from_specific_district(key):
    results = []
    key_element = str.split(key, "_")
    specific_district_code = key_element[2]
    all_candidates = load_all_candidates()
    for candidate in all_candidates : 
        if candidate.district.code == int(specific_district_code):
            results.append(candidate)
    return results

def __generate_party_datas(key):
    all_parties = load_all_parties()
    if key =="":
        return all_parties
    elif key == "with_candidates_2024":
        return load_all_parties_with_candidates()
    elif key == "low_stable_with_candidates_2024":
        return load_all_parties_with_candidates_but_not_stability()
    elif key =="high_stable_with_candidates_2024":
        return load_all_parties_with_candidates_and_big_stability()
    else: 
        return all_parties[key]
    
def __generate_congress_datas(key):
    if key == "very_stable":
        return load_congress_very_stable()
    elif key == "stable":
        return load_congress_stable()
    elif key =="quite_stable":
        return load_congress_quite_stable()
    elif key == "low_stable":
        return load_congress_low_stable()
    elif key == "perfectly_representative":
        return load_congress_perfectly_representative()
    elif key == "good_representative":
        return load_congress_good_representative()
    elif key == "quite_representative":
        return load_congress_quite_representative()
    elif key == "low_representative":
        return load_congress_low_representative()
    
def __generate_department_congress(key):
    return load_three_congress_departments()
    
def __generate_results_elections(key):
    if key =="perfect" :
        return load_20_perfect_districts_results()
    elif key =="good":
        return load_20_good_districts_results()
    elif key == "quite" : 
        return load_20_quite_districts_results()
    elif key == "default7":
        return load_7_districts_results()
    elif key == "json_results": 
        return load_json_districts_results()
    elif key == "three_departments":
        return load_json_districts_three_departments_results()
    elif key == "three_departments_tmp":
        return load_json_districts_three_departments_tmp_results()
    elif key =="three_departments_tmp_no_objects":
        return load_json_districts_three_departments_tmp_results_no_objects()
    elif key == "one_district":
        return load_json_districts_departement_with_one_district_results()
    elif key =="three_districts":
        return load_json_districts_department_with_three_districts_results()
    elif key == "twelve_districts":
        return load_json_districts_department_with_twelve_districts_results()
    else :
        return load_20_low_districts_results()