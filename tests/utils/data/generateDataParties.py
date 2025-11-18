import json
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.party import Party

def load_all_parties():
    json_parties = "{\"2022\":[{\"name\":\"Divers extrême gauche\",\"code\":\"DXG\"},{\"name\":\"Parti radical de gauche\",\"code\":\"RDG\"},{\"name\":\"Nouvelle union populaire écologique et sociale\",\"code\":\"NUP\"},{\"name\":\"Divers gauche\",\"code\":\"DVG\"},{\"name\":\"Ecologistes\",\"code\":\"ECO\"},{\"name\":\"Divers\",\"code\":\"DIV\"},{\"name\":\"Régionaliste\",\"code\":\"REG\"},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\"},{\"name\":\"Divers centre\",\"code\":\"DVC\"},{\"name\":\"Union des Démocrates et des Indépendants\",\"code\":\"UDI\"},{\"name\":\"Les Républicains\",\"code\":\"LR\"},{\"name\":\"Divers droite\",\"code\":\"DVD\"},{\"name\":\"Droite souverainiste\",\"code\":\"DSV\"},{\"name\":\"Reconquête !\",\"code\":\"REC\"},{\"name\":\"Rassemblement National\",\"code\":\"RN\"},{\"name\":\"Divers extrême droite\",\"code\":\"DXD\"}],\"2024\":[{\"name\":\"Extrême gauche\",\"code\":\"EXG\"},{\"name\":\"Parti communiste français\",\"code\":\"COM\"},{\"name\":\"La France insoumise\",\"code\":\"FI\"},{\"name\":\"Parti socialiste\",\"code\":\"SOC\"},{\"name\":\"Parti radical de gauche\",\"code\":\"RDG\"},{\"name\":\"Les Ecologistes\",\"code\":\"VEC\"},{\"name\":\"Divers gauche\",\"code\":\"DVG\"},{\"name\":\"Union de la gauche\",\"code\":\"UG\"},{\"name\":\"Ecologistes\",\"code\":\"ECO\"},{\"name\":\"Régionaliste\",\"code\":\"REG\"},{\"name\":\"Divers\",\"code\":\"DIV\"},{\"name\":\"Renaissance\",\"code\":\"REN\"},{\"name\":\"Modem\",\"code\":\"MDM\"},{\"name\":\"Horizons\",\"code\":\"HOR\"},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\"},{\"name\":\"Divers centre\",\"code\":\"DVC\"},{\"name\":\"Union des Démocrates et Indépendants\",\"code\":\"UDI\"},{\"name\":\"Les Républicains\",\"code\":\"LR\"},{\"name\":\"Divers droite\",\"code\":\"DVD\"},{\"name\":\"Droite souverainiste\",\"code\":\"DSV\"},{\"name\":\"Rassemblement National\",\"code\":\"RN\"},{\"name\":\"Reconquête !\",\"code\":\"REC\"},{\"name\":\"Union de l'extrême droite\",\"code\":\"UXD\"},{\"name\":\"Extrême droite\",\"code\":\"EXD\"}]}"
    parties_obj = json.loads(json_parties)
    parties = __transform_to_parties_array(parties_obj)
    return parties 


def __transform_to_parties_array(parties_obj):
    all_parties = {}
    for year in parties_obj:
        all_parties[year] = []
        all_parties_this_year = parties_obj[year]
        for party_obj in all_parties_this_year:
            party = Party()
            party.code = party_obj["code"]
            party.name = party_obj["name"]
            all_parties[year].append(party)
    return all_parties

def load_all_parties_with_candidates():
    json_parties_with_candidates = "[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"elected persons\":3,\"congressPersons\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":2502,\"department_name\":\"Doubs\",\"department_code\":25}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}},{\"last_name\":\"ROSSET\",\"first_name\":\"Marine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":18845,\"vote_percentage\":33.4,\"district\":{\"name\":\"2ème circonscription\",\"code\":7502,\"department_name\":\"Paris\",\"department_code\":75}},{\"last_name\":\"AUTAIN\",\"first_name\":\"Clémentine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":22209,\"vote_percentage\":62.65,\"district\":{\"name\":\"11ème circonscription\",\"code\":9311,\"department_name\":\"Seine-Saint-Denis\",\"department_code\":93}}]},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"elected persons\":1,\"congressPersons\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":1502,\"department_name\":\"Cantal\",\"department_code\":15}}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected persons\":3,\"congressPersons\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"BABIN\",\"first_name\":\"Elodie\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":4502,\"department_name\":\"Loiret\",\"department_code\":45}},{\"last_name\":\"GOULET\",\"first_name\":\"Florence\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":19011,\"vote_percentage\":50.63,\"district\":{\"name\":\"2ème circonscription\",\"code\":5502,\"department_name\":\"Meuse\",\"department_code\":55}}]}]"
    parties_obj_with_candidates = json.loads(json_parties_with_candidates)
    parties = __transform_to_parties_with_candidates(parties_obj_with_candidates)
    return parties

def load_all_parties_with_candidates_and_big_stability():
    json_parties_with_candidates = "[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"elected persons\":4,\"congressPersons\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":2502,\"department_name\":\"Doubs\",\"department_code\":25}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}},{\"last_name\":\"ROSSET\",\"first_name\":\"Marine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":18845,\"vote_percentage\":33.4,\"district\":{\"name\":\"2ème circonscription\",\"code\":7502,\"department_name\":\"Paris\",\"department_code\":75}},{\"last_name\":\"AUTAIN\",\"first_name\":\"Clémentine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":22209,\"vote_percentage\":62.65,\"district\":{\"name\":\"11ème circonscription\",\"code\":9311,\"department_name\":\"Seine-Saint-Denis\",\"department_code\":93}}]},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"elected persons\":1,\"congressPersons\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":1502,\"department_name\":\"Cantal\",\"department_code\":15}}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected persons\":3,\"congressPersons\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"BABIN\",\"first_name\":\"Elodie\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":4502,\"department_name\":\"Loiret\",\"department_code\":45}},{\"last_name\":\"GOULET\",\"first_name\":\"Florence\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":19011,\"vote_percentage\":50.63,\"district\":{\"name\":\"2ème circonscription\",\"code\":5502,\"department_name\":\"Meuse\",\"department_code\":55}}]}]"
    parties_obj_with_candidates = json.loads(json_parties_with_candidates)
    parties = __transform_to_parties_with_candidates(parties_obj_with_candidates)
    return parties

def load_all_parties_with_candidates_but_not_stability():
    json_parties_with_candidates = "[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"elected persons\":2,\"congressPersons\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":2502,\"department_name\":\"Doubs\",\"department_code\":25}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}}]},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"elected persons\":1,\"congressPersons\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":1502,\"department_name\":\"Cantal\",\"department_code\":15}}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected persons\":2,\"congressPersons\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"BABIN\",\"first_name\":\"Elodie\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":4502,\"department_name\":\"Loiret\",\"department_code\":45}}]},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\",\"elected persons\":2,\"congressPersons\":[{\"last_name\":\"FINE\",\"first_name\":\"Sébastien\",\"sexe\":\"MASCULIN\",\"parti_code\":\"ENS\",\"vote\":10338,\"vote_percentage\":26.7,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"MAILLART-MÉHAIGNERIE\",\"first_name\":\"Laurence\",\"sexe\":\"FEMININ\",\"parti_code\":\"ENS\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}}]}]"
    parties_obj_with_candidates = json.loads(json_parties_with_candidates)
    parties = __transform_to_parties_with_candidates(parties_obj_with_candidates)
    return parties

def __transform_to_parties_with_candidates(parties_obj):
    all_parties = []
    for party_obj in parties_obj:        
        party = Party()
        party.code = party_obj["code"]
        party.name = party_obj["name"]
        party.elected_congress_persons = party_obj["elected persons"]
        party.congress_persons = []
        for candidate_obj in party_obj["congressPersons"]:
            congress_person = CongressPerson()
            congress_person.last_name = candidate_obj["last_name"]
            congress_person.first_name = candidate_obj["first_name"]
            congress_person.sexe = candidate_obj["sexe"]
            congress_person.parti_code = candidate_obj["parti_code"]
            congress_person.vote = candidate_obj["vote"]
            congress_person.vote_percentage = candidate_obj["vote_percentage"]
            congress_person.district.code = candidate_obj["district"]["code"]
            congress_person.district.name = candidate_obj["district"]["name"]
            congress_person.district.department_code = candidate_obj["district"]["department_code"]
            congress_person.district.department_name = candidate_obj["district"]["department_name"]
            party.congress_persons.append(congress_person)
        all_parties.append(party)
    return all_parties