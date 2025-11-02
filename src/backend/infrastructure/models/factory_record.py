from src.backend.infrastructure.models.candidate_record import CandidateRecord
from src.backend.infrastructure.models.department_record import DepartmentRecord
from src.backend.infrastructure.models.district_record import DistrictRecord
from src.backend.infrastructure.models.election_record import ElectionRecord
from src.backend.infrastructure.models.elections_results_record import ElectionsResultsRecord
from src.backend.infrastructure.models.party_record import PartyRecord

def factory_candidate_record(last_name, first_name, sexe, parti_code, vote, vote_by_registered, vote_by_expressed):
    candidate = CandidateRecord()
    candidate.last_name = last_name
    candidate.first_name = first_name
    candidate.sexe = sexe
    candidate.parti_code = parti_code
    candidate.vote = vote
    candidate.vote_by_registered = vote_by_registered
    candidate.vote_by_expressed = vote_by_expressed
    return candidate

def factory_district_record(label, number, department_code, registered, voting, candidates):
    district = DistrictRecord()
    district.label = label
    district.number = number
    district.department_code = department_code
    district.registered = registered
    district.voting = voting
    district.candidates = candidates
    return district

def factory_election_record(year, districts): 
    election = ElectionRecord()
    election.year = year
    election.districts = districts
    return election

def factory_department_record(name, code):
    department = DepartmentRecord()
    department.name = name
    department.code = code
    return department

def factory_elections_result_record(elections, departments, parties):
    elections_result = ElectionsResultsRecord()
    elections_result.elections = elections
    elections_result.departments = departments
    elections_result.parties = parties
    return elections_result

def factory_party_record(name, code):
    party = PartyRecord()
    party.name = name
    party.code = code
    return party