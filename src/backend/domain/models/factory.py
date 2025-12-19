from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.congress_datas import CongressDatas
from src.backend.domain.models.elections import Elections

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

def factory_elections(candidates, parties, departments):
    elections = Elections()
    elections.all_candidates = candidates
    elections.all_parties = parties 
    elections.all_departments = departments
    return elections

def factory_congress_datas(year, mode, parties):
    congress_datas = CongressDatas()
    congress_datas.year = year
    congress_datas.mode = mode
    congress_datas.parties = parties
    return congress_datas