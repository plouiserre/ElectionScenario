from api.response.CongressResponse import CongressResponse
from api.response.CongressPersonResponse import CongressPersonResponse
from api.response.DistrictResponse import DistrictResponse
from api.response.PartyResponse import PartyResponse

#tmp delete when it is not use anymore
def factory_district_response(name, code,department_code, department_name):
    response = DistrictResponse()
    response.name = name
    response.code = code
    response.department_code = department_code
    response.department_name = department_name
    return response

def factory_congress_person(last_name, first_name, district):
    response = CongressPersonResponse()
    response.last_name = last_name
    response.first_name = first_name
    response.district = district
    return response

def factory_party(name, code, congressmans):
    response = PartyResponse()
    response.name = name
    response.code = code
    response.congressmans = congressmans
    return response

def factory_congress(year, mode, parties):
    response = CongressResponse()
    response.mode = mode
    response.year = year
    response.parties = parties
    return response