from api.mapper.MapperParty import to_mapper_party_response
from api.response.CongressResponse import CongressResponse

def to_mapper_congress_response(congress_domain):
    response = CongressResponse()
    response.year = congress_domain.year
    response.mode = congress_domain.mode 
    for party_domain in congress_domain.parties : 
        party_response = to_mapper_party_response(party_domain)
        response.parties.append(party_response)
    return response