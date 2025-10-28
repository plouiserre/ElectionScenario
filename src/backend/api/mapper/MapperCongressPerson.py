from src.backend.api.mapper.MapperDistrict import to_mapper_district
from src.backend.api.response.CongressPersonResponse import CongressPersonResponse

def to_congress_person_response(congress_person_domain):
    response = CongressPersonResponse()
    response.district = to_mapper_district(congress_person_domain.district)
    response.first_name = congress_person_domain.first_name
    response.last_name = congress_person_domain.last_name
    response.vote = congress_person_domain.vote 
    response.vote_percentage = congress_person_domain.vote_percentage
    return response