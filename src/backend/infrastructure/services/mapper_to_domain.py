from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.factory import factory_elections
from src.backend.domain.models.party import Party

def mapper_all_elections_results(results_elections):
    all_elections_results = {}
    all_candidates = __mapper_candidates_to_domain_person(results_elections)
    all_parties = __mapper_parties_to_domain(results_elections)
    for year in all_parties : 
        all_candidates_this_year = all_candidates[year]
        all_parties_this_year = all_parties[year]
        elections = factory_elections(all_candidates_this_year, all_parties_this_year)
        all_elections_results[year] = elections
    return all_elections_results
    

def __mapper_candidates_to_domain_person(results_elections):
    all_candidates_all_years = {}
    for year in results_elections:
        results = results_elections[year]
        all_candidates_all_years[year]= []
        for district in results.election.districts: 
            candidates_domain = []
            for candidate in district.candidates:
                candidate_domain = __mapper_candidate_to_congress_person(candidate, district, results.departments)
                candidates_domain.append(candidate_domain)
            all_candidates_all_years[year].append(candidates_domain)
    return all_candidates_all_years


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

def __mapper_parties_to_domain(results_elections):
    all_parties_all_years = {}
    for year in results_elections: 
        results = results_elections[year]
        all_parties_all_years[year] = []
        for party in results.election.parties:
            party_domain = __mapper_party_to_domain(party)
            all_parties_all_years[year].append(party_domain)
    return all_parties_all_years

def __mapper_party_to_domain(party):
    party_domain = Party()
    party_domain.code = party.code
    party_domain.name = party.name
    return party_domain