from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

def mapper_candidates_to_domain_person(results_election):
    all_candidates = []
    for election in results_election.elections:
        for district in election.districts: 
            for candidate in district.candidates:
                candidate_domain = __mapper_candidate_to_congress_person(candidate, district, results_election.departments)
                all_candidates.append(candidate_domain)
    return all_candidates


def __mapper_candidate_to_congress_person(candidate, district, departments):
    congress_person = CongressPerson()
    congress_person.first_name = candidate.first_name
    congress_person.last_name = candidate.last_name
    congress_person.parti_code = candidate.parti_code
    congress_person.sexe = candidate.sexe
    congress_person.vote = candidate.vote
    congress_person.vote_percentage = candidate.vote_by_expressed 
    congress_person.district = __mapper_district_infra_to_district_domain(district, departments)
    return congress_person

def __mapper_district_infra_to_district_domain(district, departments):
    district_domain = District()
    district_domain.code = district.number
    district_domain.name = district.label
    district_domain.department_code = district.department_code
    for department in departments : 
        if department.code == district.department_code :
            district_domain.department_name = department.name
            break
    return district_domain

def mapper_parties_to_domain(results):
    all_parties = []
    for party in results.parties: 
        party_domain = __mapper_party_to_domain(party)
        all_parties.append(party_domain)
    return all_parties

def __mapper_party_to_domain(party):
    party_domain = Party()
    party_domain.code = party.code
    party_domain.name = party.name
    return party_domain