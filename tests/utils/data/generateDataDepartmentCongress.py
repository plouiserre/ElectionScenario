import json
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.department_congress import DepartmentCongress
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

def load_three_congress_departments():
    congress_departments = []
    json_data = "{\"congress_departments\":[{\"department_code\":33,\"department_name\":\"Gironde\",\"parties\":[{\"code\":\"UG\",\"elected_congress_persons\":4,\"family\":\"2\",\"name\":\"Union de la gauche\",\"congress_persons\":[{\"first_name\":\"Loïc\",\"last_name\":\"PRUD'HOMME\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":30664,\"vote_percentage\":\"49.83%\",\"district\":{\"code\":\"3303\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"3ème circonscription\"}},{\"first_name\":\"Nicolas\",\"last_name\":\"THIERRY\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":26547,\"vote_percentage\":\"49.45%\",\"district\":{\"code\":\"3302\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"2ème circonscription\"}},{\"first_name\":\"Alain\",\"last_name\":\"DAVID\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":27092,\"vote_percentage\":\"42.36%\",\"district\":{\"code\":\"3304\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"4ème circonscription\"}},{\"first_name\":\"Sébastien\",\"last_name\":\"SAINT-PASTEUR\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":21913,\"vote_percentage\":\"38.50%\",\"district\":{\"code\":\"3307\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"7ème circonscription\"}}]},{\"code\":\"RN\",\"elected_congress_persons\":4,\"family\":\"5\",\"name\":\"Rassemblement National\",\"congress_persons\":[{\"first_name\":\"Edwige\",\"last_name\":\"DIAZ\",\"parti_code\":\"RN\",\"sexe\":\"FEMININ\",\"vote\":34590,\"vote_percentage\":\"53.33%\",\"district\":{\"code\":\"3311\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"11ème circonscription\"}},{\"first_name\":\"Sandrine\",\"last_name\":\"CHADOURNE\",\"parti_code\":\"RN\",\"sexe\":\"FEMININ\",\"vote\":26547,\"vote_percentage\":\"43.80%\",\"district\":{\"code\":\"3310\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"10ème circonscription\"}},{\"first_name\":\"Grégoire\",\"last_name\":\"DE FOURNAS\",\"parti_code\":\"RN\",\"sexe\":\"MASCULIN\",\"vote\":35457,\"vote_percentage\":\"42.32%\",\"district\":{\"code\":\"3305\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"5ème circonscription\"}},{\"first_name\":\"François-Xavier\",\"last_name\":\"MARQUES\",\"parti_code\":\"RN\",\"sexe\":\"MASCULIN\",\"vote\":27868,\"vote_percentage\":\"38.54%\",\"district\":{\"code\":\"3309\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"9ème circonscription\"}}]},{\"code\":\"ENS\",\"elected_congress_persons\":4,\"family\":\"3\",\"name\":\"Ensemble ! (Majorité présidentielle)\",\"congress_persons\":[{\"first_name\":\"Thomas\",\"last_name\":\"CAZENAVE\",\"parti_code\":\"ENS\",\"sexe\":\"MASCULIN\",\"vote\":28564,\"vote_percentage\":\"38.31%\",\"district\":{\"code\":\"3301\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"1ère circonscription\"}},{\"first_name\":\"Bérangère\",\"last_name\":\"COUILLARD\",\"parti_code\":\"ENS\",\"sexe\":\"FEMININ\",\"vote\":18854,\"vote_percentage\":\"33.12%\",\"district\":{\"code\":\"3307\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"7ème circonscription\"}},{\"first_name\":\"Eric\",\"last_name\":\"POUILLAT\",\"parti_code\":\"ENS\",\"sexe\":\"MASCULIN\",\"vote\":25636,\"vote_percentage\":\"32.78%\",\"district\":{\"code\":\"3306\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"6ème circonscription\"}},{\"first_name\":\"Sophie\",\"last_name\":\"PANONACLE\",\"parti_code\":\"ENS\",\"sexe\":\"FEMININ\",\"vote\":26881,\"vote_percentage\":\"31.71%\",\"district\":{\"code\":\"3308\",\"department_code\":\"33\",\"department_name\":\"\",\"name\":\"8ème circonscription\"}}]}]},{\"department_code\":3,\"department_name\":\"Allier\",\"parties\":[{\"code\":\"RN\",\"elected_congress_persons\":1,\"family\":\"5\",\"name\":\"Rassemblement National\",\"congress_persons\":[{\"first_name\":\"Anne-Marie\",\"last_name\":\"THES\",\"parti_code\":\"RN\",\"sexe\":\"FEMININ\",\"vote\":22816,\"vote_percentage\":\"38.61%\",\"district\":{\"code\":\"301\",\"department_code\":\"3\",\"department_name\":\"\",\"name\":\"1ère circonscription\"}}]},{\"code\":\"UG\",\"elected_congress_persons\":1,\"family\":\"2\",\"name\":\"Union de la gauche\",\"congress_persons\":[{\"first_name\":\"Yannick\",\"last_name\":\"MONNET\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":17043,\"vote_percentage\":\"28.84%\",\"district\":{\"code\":\"301\",\"department_code\":\"3\",\"department_name\":\"\",\"name\":\"1ère circonscription\"}}]},{\"code\":\"LR\",\"elected_congress_persons\":1,\"family\":\"4\",\"name\":\"Les Républicains\",\"congress_persons\":[{\"first_name\":\"Nicolas\",\"last_name\":\"RAY\",\"parti_code\":\"LR\",\"sexe\":\"MASCULIN\",\"vote\":21464,\"vote_percentage\":\"40.05%\",\"district\":{\"code\":\"303\",\"department_code\":\"3\",\"department_name\":\"\",\"name\":\"3ème circonscription\"}}]}]},{\"department_code\":15,\"department_name\":\"Cantal\",\"parties\":[{\"code\":\"DVD\",\"elected_congress_persons\":1,\"family\":\"4\",\"name\":\"Divers Droite\",\"congress_persons\":[{\"first_name\":\"Vincent\",\"last_name\":\"DESCOEUR\",\"parti_code\":\"DVD\",\"sexe\":\"MASCULIN\",\"vote\":16615,\"vote_percentage\":\"37.66%\",\"district\":{\"code\":\"1501\",\"department_code\":\"15\",\"department_name\":\"\",\"name\":\"1ère circonscription\"}}]}]}]}"
    json_departments_congress = json.loads(json_data)    
    congress_departments = __build_congress_departments(json_departments_congress)
    return congress_departments

def __build_congress_departments(json_departments_congress):
    congress_departments = []
    congress_departments_json = json_departments_congress["congress_departments"]
    for congress_department_json in congress_departments_json :         
        parties = __build_parties(congress_department_json["parties"])
        department_congress = DepartmentCongress()
        department_congress.department_code = congress_department_json["department_code"]
        department_congress.department_name = congress_department_json["department_name"]
        department_congress.parties = parties
        congress_departments.append(department_congress)
    return congress_departments

def __build_parties(parties_json):
    parties = []
    for party_json in parties_json :
        party = Party()
        party.code = party_json["code"]
        party.elected_congress_persons = party_json["elected_congress_persons"]
        party.family = party_json["family"]
        party.name = party_json["name"]
        party.congress_persons = __build_congress_persons(party_json["congress_persons"])
        parties.append(party)
    return parties

def __build_congress_persons(congress_persons_json):
    congress_persons = []
    for congress_person_json in congress_persons_json:
        congress_person = CongressPerson()
        congress_person.first_name = congress_person_json["first_name"]
        congress_person.last_name = congress_person_json["last_name"]
        congress_person.parti_code = congress_person_json["parti_code"]
        congress_person.sexe = congress_person_json["sexe"]
        congress_person.vote = congress_person_json["vote"]
        congress_person.vote_percentage = congress_person_json["vote_percentage"]
        congress_person.district = __build_district(congress_person_json["district"])
        congress_persons.append(congress_person)
    return congress_persons

def __build_district(district_json):
    district = District()
    district.code = district_json["code"]
    district.department_code = district_json["department_code"]
    district.department_name = district_json["department_name"]
    district.name = district_json["name"]
    return district