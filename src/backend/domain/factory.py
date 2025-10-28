#tmp
from src.backend.domain.congressPerson import CongressPerson
from src.backend.domain.congress import Congress
from src.backend.domain.district import District
from src.backend.domain.party import Party

def factory_district(name, code, department_name, department_code):
    district = District()
    district.name = name
    district.code = code
    district.department_name = department_name
    district.department_code = department_code
    return district

def factory_congress_person(last_name, first_name, vote, vote_percentage, district):
    congress_person = CongressPerson()
    congress_person.last_name = last_name
    congress_person.first_name = first_name
    congress_person.vote = vote
    congress_person.vote_percentage = vote_percentage
    congress_person.district = district
    return congress_person

def factory_party(name, code, percentage, congress_persons): 
    party = Party()
    party.name = name
    party.code = code
    party.percentage = percentage
    party.congress_persons = congress_persons
    return party

def factory_congress(year, mode, parties):
    congress = Congress()
    congress.year = year
    congress.mode = mode
    congress.parties = parties
    return congress