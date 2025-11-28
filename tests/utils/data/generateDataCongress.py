import json
from src.backend.domain.models.congress import Congress
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

def load_congress_very_stable():
    json_congress = "{\"congress\":{\"year\":2024,\"mode\":\"PROPORTIONALITYNATIONAL\",\"parties\":[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"elected_congress_persons\":185,\"congress_persons\":[{\"district\":{\"name\":\"2ème circonscription\",\"code\":\"9302\",\"department_name\":\"Seine-Saint-Denis\",\"department_code\":\"93\"},\"last_name\":\"PEU\",\"first_name\":\"Stéphane\",\"vote\":22055,\"vote_percentage\":71.8},{\"district\":{\"name\":\"6ème circonscription\",\"code\":\"9306\",\"department_name\":\"Seine-Saint-Denis\",\"department_code\":\"93\"},\"last_name\":\"LACHAUD\",\"first_name\":\"Bastien\",\"vote\":25777,\"vote_percentage\":71.68},{\"district\":{\"name\":\"4ème circonscription\",\"code\":\"1304\",\"department_name\":\"Bouches-du-Rhône\",\"department_code\":\"13\"},\"last_name\":\"BOMPARD\",\"first_name\":\"Manuel\",\"vote\":26712,\"vote_percentage\":67.49},{\"district\":{\"name\":\"1ère circonscription\",\"code\":\"9301\",\"department_name\":\"Seine-Saint-Denis\",\"department_code\":\"93\"},\"last_name\":\"COQUEREL\",\"first_name\":\"Éric\",\"vote\":27298,\"vote_percentage\":65.28}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected_congress_persons\":192,\"congress_persons\":[{\"district\":{\"name\":\"10ème circonscription\",\"code\":\"6210\",\"department_name\":\"Pas-de-Calais\",\"department_code\":\"62\"},\"last_name\":\"FRAPPÉ\",\"first_name\":\"Thierry\",\"vote\":32530,\"vote_percentage\":60.61},{\"district\":{\"name\":\"12ème circonscription\",\"code\":\"6212\",\"department_name\":\"Pas-de-Calais\",\"department_code\":\"62\"},\"last_name\":\"BILDE\",\"first_name\":\"Bruno\",\"vote\":33944,\"vote_percentage\":59.24}]},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\",\"elected_congress_persons\":139,\"congress_persons\":[{\"district\":{\"name\":\"1ère circonscription\",\"code\":\"98601\",\"department_name\":\"Wallis et Futuna\",\"department_code\":\"986\"},\"last_name\":\"SEO\",\"first_name\":\"Mikaele\",\"vote\":4281,\"vote_percentage\":62.25}]}],\"stability_majority\":\"\"}}"
    congress_data = json.loads(json_congress)
    congress = __transform_to_congress(congress_data)
    return congress


def __transform_to_congress(congress_data):
    congress_obj = congress_data["congress"]
    congress = Congress()
    congress.year = congress_obj["year"]
    congress.mode = congress_obj["mode"]
    congress.parties = []
    for party_obj in congress_obj["parties"]: 
        party = __transform_to_party(party_obj)
        congress.parties.append(party)
    return congress


def __transform_to_party(party_obj):
    party = Party()
    party.code = party_obj["code"]
    party.name = party_obj["name"]
    party.congress_persons = []
    for congress_person_obj in party_obj["congress_persons"]:
        congress_person = __transform_to_congress_person(congress_person_obj)
        party.congress_persons.append(congress_person)
        party.elected_congress_persons += 1
    return party

def __transform_to_congress_person(congress_person_obj): 
    congress_person = CongressPerson()
    congress_person.first_name = congress_person_obj["first_name"]
    congress_person.last_name = congress_person_obj["last_name"]
    congress_person.vote = congress_person_obj["vote"]
    congress_person.vote_percentage = congress_person_obj["vote_percentage"]
    congress_person.district = District()
    congress_person.district.code = congress_person_obj["district"]["code"]
    congress_person.district.name = congress_person_obj["district"]["name"]
    congress_person.district.department_code = congress_person_obj["district"]["department_code"]
    congress_person.district.department_name = congress_person_obj["district"]["department_name"]
    return congress_person