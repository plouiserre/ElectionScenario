from src.backend.infrastructure.models.candidate_record import CandidateRecord
from src.backend.infrastructure.models.district_record import DistrictRecord
from src.backend.infrastructure.models.election_record import ElectionRecord

def factory_candidate(last_name, first_name, sexe, parti_code, vote, vote_by_registered, vote_by_expressed):
    candidate = CandidateRecord()
    candidate.last_name = last_name
    candidate.first_name = first_name
    candidate.sexe = sexe
    candidate.parti_code = parti_code
    candidate.vote = vote
    candidate.vote_by_registered = vote_by_registered
    candidate.vote_by_expressed = vote_by_expressed
    return candidate

def factory_district(label, number, department_code, registered, voting, candidates):
    district = DistrictRecord()
    district.label = label
    district.number = number
    district.department_code = department_code
    district.registered = registered
    district.voting = voting
    district.candidates = candidates
    return district

def factory_election(year, districts): 
    election = ElectionRecord()
    election.year = year
    election.districts = districts
    return election