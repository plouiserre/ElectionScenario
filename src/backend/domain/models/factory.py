from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.congress_datas import CongressDatas
from src.backend.domain.models.department import Department
from src.backend.domain.models.elections import Elections
from src.backend.domain.models.ProportionalDepartemental.mode_design import ModeDesign

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

def factory_congress_datas(year, mode, parties, departmental_assemblies):
    congress_datas = CongressDatas()
    congress_datas.year = year
    congress_datas.mode = mode
    congress_datas.parties = parties
    congress_datas.departmental_assemblies = departmental_assemblies
    return congress_datas

def factory_dpt(name, code):
    dpt = Department()
    dpt.name = name
    dpt.code = code
    return dpt

def factory_mode_design(type, minimal_vote): 
    mode_design = ModeDesign()
    mode_design.type = type
    mode_design.minimal_vote = minimal_vote
    return mode_design
