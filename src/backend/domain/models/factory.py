#tmp
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.congress import Congress
from src.backend.domain.models.district import District
from src.backend.domain.models.elections import Elections
from src.backend.domain.models.party import Party

def factory_district(name, code, department_name, department_code):
    district = District()
    district.name = name
    district.code = code
    district.department_name = department_name
    district.department_code = department_code
    return district

def factory_congress_person(last_name, first_name, sexe, parti_code, vote, vote_percentage, district):
    congress_person = CongressPerson()
    congress_person.last_name = last_name
    congress_person.first_name = first_name
    congress_person.sexe = sexe
    congress_person.parti_code = parti_code
    congress_person.vote = vote
    congress_person.vote_percentage = vote_percentage
    congress_person.district = district
    return congress_person

def factory_elections(candidates, parties):
    elections = Elections()
    elections.all_candidates = candidates
    elections.all_parties = parties 
    return elections

def factory_party(name, code, congress_persons): 
    party = Party()
    party.name = name
    party.code = code
    party.congress_persons = congress_persons
    return party

def factory_congress(year, mode, parties):
    congress = Congress()
    congress.year = year
    congress.mode = mode
    congress.parties = parties
    return congress