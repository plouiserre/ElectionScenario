from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.factory import factory_elections
from src.backend.domain.models.party import Party

def mapper_all_elections_results(data_results_elections):
    all_elections_results = {}
    all_candidates = __mapper_candidates_to_domain_person(data_results_elections)
    all_parties = __mapper_parties_to_domain(data_results_elections)
    for year in all_parties : 
        all_candidates_this_year = all_candidates[year]
        all_parties_this_year = all_parties[year]
        elections = factory_elections(all_candidates_this_year, all_parties_this_year)
        all_elections_results[year] = elections
    return all_elections_results
    

def __mapper_candidates_to_domain_person(data_results_elections):
    results_elections = data_results_elections["elections"]
    all_candidates_all_years = {}
    for results in results_elections:
        year = results["year"]
        all_candidates_all_years[year]= []
        for district in results["districts"]: 
            candidates_domain = []
            for candidate in district["candidates"]:
                candidate_domain = __mapper_candidate_to_congress_person(candidate, district, data_results_elections["departments"])
                candidates_domain.append(candidate_domain)
            all_candidates_all_years[year].append(candidates_domain)
    return all_candidates_all_years


def __mapper_candidate_to_congress_person(candidate, district, departments):
    congress_person = CongressPerson()
    congress_person.first_name = candidate["firstName"]
    congress_person.last_name = candidate["lastName"]
    congress_person.parti_code = candidate["partiCode"]
    congress_person.sexe = candidate["sexe"]
    congress_person.vote = candidate["vote"]
    congress_person.vote_percentage = __manage_vote_percentage(candidate)
    congress_person.district = __mapper_district_infra_to_district_domain(district, departments)
    return congress_person

def __manage_vote_percentage(candidate):
    vote_percentage_with_sign = candidate["voteByExpressed"]
    vote_percentage_str = vote_percentage_with_sign.replace("%", "")
    vote_percentage = float(vote_percentage_str)
    return vote_percentage

def __mapper_district_infra_to_district_domain(district, departments):
    district_domain = District()    
    district_domain.code = __manage_corsica_district_data_with_number(district, "number") 
    district_domain.name = district["label"]
    district_domain.department_code = __manage_corsica_district_data_with_number(district, "department code")
    for department in departments : 
        department_code = __adapt_department_code(district, department)
        if department_code == district["department code"] :
            district_domain.department_name = department["name"]
            break
    return district_domain

def __manage_corsica_district_data_with_number(district, key):
    district_code = 0
    if("2A" in district[key]):
        district_number_updated = district[key].replace("2A", "20")
        district_code = int(district_number_updated)
    elif("2B" in district[key]):
        district_number_updated = district[key].replace("2B", "20")
        district_code = int(district_number_updated)
    else :
        district_code = int(district[key])
    return district_code


def __adapt_department_code(district, department):
    if  len(department["code"]) == 1 and len(district["department code"]) == 2 :
        return "0"+department["code"] 
    else :
        return department["code"]
        

def __mapper_parties_to_domain(data_results_elections):
    all_parties = data_results_elections["parties"]
    all_parties_all_years = {}
    for year in all_parties:
        parties =  all_parties[year]
        key_year = int(year)
        all_parties_all_years[key_year] = []
        for party in parties:
            party_domain = __mapper_party_to_domain(party)
            all_parties_all_years[key_year].append(party_domain)
    return all_parties_all_years

def __mapper_party_to_domain(party):
    party_domain = Party()
    party_domain.code = party["code"]
    party_domain.name = party["name"]
    return party_domain