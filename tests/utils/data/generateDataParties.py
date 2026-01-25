import json
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.party import Party

def load_all_parties():
    json_parties = "{\"2022\":[{\"name\":\"Divers extrême gauche\",\"code\":\"DXG\",\"family\":1},{\"name\":\"Parti radical de gauche\",\"code\":\"RDG\",\"family\":2},{\"name\":\"Nouvelle union populaire écologique et sociale\",\"code\":\"NUP\",\"family\":2},{\"name\":\"Divers gauche\",\"code\":\"DVG\",\"family\":2},{\"name\":\"Ecologistes\",\"code\":\"ECO\",\"family\":10},{\"name\":\"Divers\",\"code\":\"DIV\",\"family\":10},{\"name\":\"Régionaliste\",\"code\":\"REG\",\"family\":10},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\",\"family\":3},{\"name\":\"Divers centre\",\"code\":\"DVC\",\"family\":3},{\"name\":\"Union des Démocrates et des Indépendants\",\"code\":\"UDI\",\"family\":4},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"family\":4},{\"name\":\"Divers droite\",\"code\":\"DVD\",\"family\":4},{\"name\":\"Droite souverainiste\",\"code\":\"DSV\",\"family\":4},{\"name\":\"Reconquête !\",\"code\":\"REC\",\"family\":5},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"family\":5},{\"name\":\"Divers extrême droite\",\"code\":\"DXD\",\"family\":5}],\"2024\":[{\"name\":\"Extrême gauche\",\"code\":\"EXG\",\"family\":1},{\"name\":\"Parti communiste français\",\"code\":\"COM\",\"family\":2},{\"name\":\"La France insoumise\",\"code\":\"FI\",\"family\":2},{\"name\":\"Parti socialiste\",\"code\":\"SOC\",\"family\":2},{\"name\":\"Parti radical de gauche\",\"code\":\"RDG\",\"family\":2},{\"name\":\"Les Ecologistes\",\"code\":\"VEC\",\"family\":2},{\"name\":\"Divers gauche\",\"code\":\"DVG\",\"family\":2},{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"family\":2},{\"name\":\"Ecologistes\",\"code\":\"ECO\",\"family\":10},{\"name\":\"Régionaliste\",\"code\":\"REG\",\"family\":10},{\"name\":\"Divers\",\"code\":\"DIV\",\"family\":10},{\"name\":\"Renaissance\",\"code\":\"REN\",\"family\":3},{\"name\":\"Modem\",\"code\":\"MDM\",\"family\":3},{\"name\":\"Horizons\",\"code\":\"HOR\",\"family\":3},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\",\"family\":3},{\"name\":\"Divers centre\",\"code\":\"DVC\",\"family\":3},{\"name\":\"Union des Démocrates et Indépendants\",\"code\":\"UDI\",\"family\":4},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"family\":4},{\"name\":\"Divers droite\",\"code\":\"DVD\",\"family\":4},{\"name\":\"Droite souverainiste\",\"code\":\"DSV\",\"family\":4},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"family\":5},{\"name\":\"Reconquête !\",\"code\":\"REC\",\"family\":5},{\"name\":\"Union de l'extrême droite\",\"code\":\"UXD\",\"family\":5},{\"name\":\"Extrême droite\",\"code\":\"EXD\",\"family\":5}]}"
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
            party.family = party_obj["family"]
            all_parties[year].append(party)
    return all_parties

def load_all_parties_with_candidates():
    json_parties_with_candidates = "[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"family\":2,\"elected persons\":3,\"congressPersons\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":2502,\"department_name\":\"Doubs\",\"department_code\":25}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}},{\"last_name\":\"ROSSET\",\"first_name\":\"Marine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":18845,\"vote_percentage\":33.4,\"district\":{\"name\":\"2ème circonscription\",\"code\":7502,\"department_name\":\"Paris\",\"department_code\":75}}]},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"elected persons\":1,\"family\":4,\"congressPersons\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":1502,\"department_name\":\"Cantal\",\"department_code\":15}}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected persons\":3,\"family\":5,\"congressPersons\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"BABIN\",\"first_name\":\"Elodie\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":4502,\"department_name\":\"Loiret\",\"department_code\":45}},{\"last_name\":\"GOULET\",\"first_name\":\"Florence\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":19011,\"vote_percentage\":50.63,\"district\":{\"name\":\"2ème circonscription\",\"code\":5502,\"department_name\":\"Meuse\",\"department_code\":55}}]}]"
    parties_obj_with_candidates = json.loads(json_parties_with_candidates)
    parties = __transform_to_parties_with_candidates(parties_obj_with_candidates)
    return parties

def load_all_parties_with_candidates_and_big_stability():
    json_parties_with_candidates = "[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"elected persons\":4,\"family\":2,\"congressPersons\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":2502,\"department_name\":\"Doubs\",\"department_code\":25}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}},{\"last_name\":\"ROSSET\",\"first_name\":\"Marine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":18845,\"vote_percentage\":33.4,\"district\":{\"name\":\"2ème circonscription\",\"code\":7502,\"department_name\":\"Paris\",\"department_code\":75}},{\"last_name\":\"AUTAIN\",\"first_name\":\"Clémentine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":22209,\"vote_percentage\":62.65,\"district\":{\"name\":\"11ème circonscription\",\"code\":9311,\"department_name\":\"Seine-Saint-Denis\",\"department_code\":93}}]},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"family\":4,\"elected persons\":1,\"congressPersons\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":1502,\"department_name\":\"Cantal\",\"department_code\":15}}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected persons\":2,\"family\":5,\"congressPersons\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"GOULET\",\"first_name\":\"Florence\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":19011,\"vote_percentage\":50.63,\"district\":{\"name\":\"2ème circonscription\",\"code\":5502,\"department_name\":\"Meuse\",\"department_code\":55}}]}]"
    parties_obj_with_candidates = json.loads(json_parties_with_candidates)
    parties = __transform_to_parties_with_candidates(parties_obj_with_candidates)
    return parties

def load_all_parties_with_candidates_but_not_stability():
    json_parties_with_candidates = "[{\"name\":\"Union de la gauche\",\"code\":\"UG\",\"elected persons\":2,\"family\":2,\"congressPersons\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":2502,\"department_name\":\"Doubs\",\"department_code\":25}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}}]},{\"name\":\"Les Républicains\",\"code\":\"LR\",\"elected persons\":1,\"family\":4,\"congressPersons\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":1502,\"department_name\":\"Cantal\",\"department_code\":15}}]},{\"name\":\"Rassemblement National\",\"code\":\"RN\",\"elected persons\":2,\"family\":5,\"congressPersons\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"BABIN\",\"first_name\":\"Elodie\",\"sexe\":\"FEMININ\",\"parti_code\":\"RN\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":4502,\"department_name\":\"Loiret\",\"department_code\":45}}]},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\",\"elected persons\":2,\"family\":3,\"congressPersons\":[{\"last_name\":\"FINE\",\"first_name\":\"Sébastien\",\"sexe\":\"MASCULIN\",\"parti_code\":\"ENS\",\"vote\":10338,\"vote_percentage\":26.7,\"district\":{\"name\":\"2ème circonscription\",\"code\":502,\"department_name\":\"Hautes-Alpes\",\"department_code\":5}},{\"last_name\":\"MAILLART-MÉHAIGNERIE\",\"first_name\":\"Laurence\",\"sexe\":\"FEMININ\",\"parti_code\":\"ENS\",\"vote\":18957,\"vote_percentage\":32.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":3502,\"department_name\":\"Ille-et-Vilaine\",\"department_code\":35}}]}]"
    parties_obj_with_candidates = json.loads(json_parties_with_candidates)
    parties = __transform_to_parties_with_candidates(parties_obj_with_candidates)
    return parties

def __transform_to_parties_with_candidates(parties_obj):
    all_parties = []
    for party_obj in parties_obj:        
        party = Party()
        party.code = party_obj["code"]
        party.name = party_obj["name"]
        party.family = int(party_obj["family"])
        party.elected_congress_persons = party_obj["elected persons"]
        party.congress_persons = []
        for candidate_obj in party_obj["congressPersons"]:
            congress_person = __get_congress_person_from_json(candidate_obj)
            party.congress_persons.append(congress_person)
        all_parties.append(party)
    return all_parties

def load_parties_info(): 
    json_parties_info = "{\"parties_info\":{\"5\":[{\"last_name\":\"ALBRAND\",\"first_name\":\"Louis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":13115,\"vote_percentage\":33.88,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"502\",\"department_name\":\"Hautes-Alpes\",\"department_code\":\"5\"}}],\"15\":[{\"last_name\":\"BONY\",\"first_name\":\"Jean-Yves\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":12383,\"vote_percentage\":34.29,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"1502\",\"department_name\":\"Cantal\",\"department_code\":\"15\"}}],\"25\":[{\"last_name\":\"VOYNET\",\"first_name\":\"Dominique\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":19160,\"vote_percentage\":34.16,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"2502\",\"department_name\":\"Doubs\",\"department_code\":\"25\"}}],\"35\":[{\"last_name\":\"DECOURCELLE\",\"first_name\":\"Christophe\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":5218,\"vote_percentage\":6.93,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"3502\",\"department_name\":\"Ille-et-Vilaine\",\"department_code\":\"35\"}},{\"last_name\":\"LAHAIS\",\"first_name\":\"Tristan\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":30361,\"vote_percentage\":40.31,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"3502\",\"department_name\":\"Ille-et-Vilaine\",\"department_code\":\"35\"}}],\"65\":[{\"last_name\":\"MONTEIL\",\"first_name\":\"Olivier\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":22436,\"vote_percentage\":36.96,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"6502\",\"department_name\":\"Hautes-Pyrénées\",\"department_code\":\"65\"}}],\"75\":[{\"last_name\":\"ROSSET\",\"first_name\":\"Marine\",\"sexe\":\"FEMININ\",\"parti_code\":\"UG\",\"vote\":18845,\"vote_percentage\":33.4,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"7502\",\"department_name\":\"Paris\",\"department_code\":\"75\"}},{\"last_name\":\"LE GENDRE\",\"first_name\":\"Gilles\",\"sexe\":\"MASCULIN\",\"parti_code\":\"DVC\",\"vote\":11071,\"vote_percentage\":19.62,\"district\":{\"name\":\"2ème circonscription\",\"code\":\"7502\",\"department_name\":\"Paris\",\"department_code\":\"75\"}}]}}"
    parties_info_json_obj = json.loads(json_parties_info)
    parties_info_obj = {}
    for key in parties_info_json_obj["parties_info"] : 
        congress_persons_obj = parties_info_json_obj["parties_info"][key]
        parties_info_obj[key] = []
        for congress_person_obj in congress_persons_obj:
            congress_person = __get_congress_person_from_json(congress_person_obj)            
            parties_info_obj[key].append(congress_person)
    return parties_info_obj

def __get_congress_person_from_json(congress_person_obj): 
            congress_person = CongressPerson()
            congress_person.last_name = congress_person_obj["last_name"]
            congress_person.first_name = congress_person_obj["first_name"]
            congress_person.sexe = congress_person_obj["sexe"]
            congress_person.parti_code = congress_person_obj["parti_code"]
            congress_person.vote = congress_person_obj["vote"]
            congress_person.vote_percentage = congress_person_obj["vote_percentage"]
            congress_person.district.code = congress_person_obj["district"]["code"]
            congress_person.district.name = congress_person_obj["district"]["name"]
            congress_person.district.department_code = congress_person_obj["district"]["department_code"]
            congress_person.district.department_name = congress_person_obj["district"]["department_name"]
            return congress_person