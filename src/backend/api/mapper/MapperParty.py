from src.backend.api.mapper.MapperCongressPerson import to_congress_person_response
from src.backend.api.response.PartyResponse import PartyResponse

def to_mapper_party_response(party_domain):
    response = PartyResponse()
    response.code = party_domain.code
    response.elected_congress_persons = party_domain.elected_congress_persons
    response.name = party_domain.name
    for congress_person in party_domain.congress_persons:
        congress_person_response = to_congress_person_response(congress_person)
        response.congress_persons.append(congress_person_response)
    return response