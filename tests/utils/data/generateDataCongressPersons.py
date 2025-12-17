import json
from src.backend.domain.models.congressPerson import CongressPerson
from src.backend.domain.models.district import District
from src.backend.domain.models.party import Party

def load_all_candidates():
    all_candidates = []
    all_candidates.extend(__load_all_candidates_from_five_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_fifteenth_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_twenty_fifth_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_thirty_fifth_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_fourty_fifth_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_fifty_fifth_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_sixty_fifth_hundred_second_district())
    all_candidates.extend(__load_all_candidates_from_seventy_fifth_hundred_second_district())
    return all_candidates


def __load_all_candidates_from_five_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"GUIGNARD\", \"first_name\" : \"Boris\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"EXG\", \"vote\": 394, \"vote_percentage\": 1.02, \"district\":{\"name\":\"2ème circonscription\", \"code\":502, \"department_name\" : \"Hautes-Alpes\", \"department_code\" : 5}} ,{\"last_name\" : \"FINE\", \"first_name\" : \"Sébastien\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"ENS\", \"vote\": 10338, \"vote_percentage\": 26.70, \"district\":{\"name\":\"2ème circonscription\", \"code\":502, \"department_name\" : \"Hautes-Alpes\", \"department_code\" : 5}}, {\"last_name\" : \"ROSSI\", \"first_name\" : \"Valérie\", \"sexe\" : \"FEMININ\", \"parti_code\": \"UG\", \"vote\": 12661, \"vote_percentage\": 32.70, \"district\":{\"name\":\"2ème circonscription\", \"code\":502, \"department_name\" : \"Hautes-Alpes\", \"department_code\" : 5}} , {\"last_name\" : \"MONDAIN\", \"first_name\" : \"Johann\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DIV\", \"vote\": 2260, \"vote_percentage\": 5.70, \"district\":{\"name\":\"2ème circonscription\", \"code\":502, \"department_name\" : \"Hautes-Alpes\", \"department_code\" : 5}}, {\"last_name\" : \"ALBRAND\", \"first_name\" : \"Louis\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"RN\", \"vote\": 13115, \"vote_percentage\": 33.88, \"district\":{\"name\":\"2ème circonscription\", \"code\":502, \"department_name\" : \"Hautes-Alpes\", \"department_code\" : 5}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates

def __load_all_candidates_from_fifteenth_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"CHEIKHI\", \"first_name\" : \"Mona\", \"sexe\" : \"FEMININ\", \"parti_code\": \"EXG\", \"vote\": 298, \"vote_percentage\": 0.83, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}, {\"last_name\" : \"PÉBAY\", \"first_name\" : \"Zoé\", \"sexe\" : \"FEMININ\", \"parti_code\": \"UG\", \"vote\": 4919, \"vote_percentage\": 13.62, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}, {\"last_name\" : \"LACROIX\", \"first_name\" : \"Gilles\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"RN\", \"vote\": 11923, \"vote_percentage\": 33.02, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}, {\"last_name\" : \"VEYSSET-RAPAPORT\", \"first_name\" : \"Pascal\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"REC\", \"vote\": 220, \"vote_percentage\": 0.61, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}, {\"last_name\" : \"TILMANT-TATISCHEFF\", \"first_name\" : \"Vladimir\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"ENS\", \"vote\": 3019, \"vote_percentage\": 8.36, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}, {\"last_name\" : \"TOTY\", \"first_name\" : \"Louis\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVD\", \"vote\": 3348, \"vote_percentage\": 9.27, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}, {\"last_name\" : \"BONY\", \"first_name\" : \"Jean-Yves\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"LR\", \"vote\": 12383, \"vote_percentage\": 34.29, \"district\":{\"name\":\"2ème circonscription\", \"code\":1502, \"department_name\" : \"Cantal\", \"department_code\" : 15}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates

def __load_all_candidates_from_twenty_fifth_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"VOYNET\", \"first_name\" : \"Dominique\", \"sexe\" : \"FEMININ\", \"parti_code\": \"UG\", \"vote\": 19160, \"vote_percentage\": 34.16, \"district\":{\"name\":\"2ème circonscription\", \"code\":2502, \"department_name\" : \"Doubs\", \"department_code\" : 25}}, {\"last_name\" : \"VUITTON\", \"first_name\" : \"Brigitte\", \"sexe\" : \"FEMININ\", \"parti_code\": \"EXG\", \"vote\": 788, \"vote_percentage\": 1.41, \"district\":{\"name\":\"2ème circonscription\", \"code\":2502, \"department_name\" : \"Doubs\", \"department_code\" : 25}}, {\"last_name\" : \"FUSIS\", \"first_name\" : \"Eric\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"RN\", \"vote\": 16895, \"vote_percentage\": 30.12, \"district\":{\"name\":\"2ème circonscription\", \"code\":2502, \"department_name\" : \"Doubs\", \"department_code\" : 25}}, {\"last_name\" : \"VUILLEMIN\", \"first_name\" : \"Benoît\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"ENS\", \"vote\": 15026, \"vote_percentage\": 26.79, \"district\":{\"name\":\"2ème circonscription\", \"code\":2502, \"department_name\" : \"Doubs\", \"department_code\" : 25}}, {\"last_name\" : \"ROY\", \"first_name\" : \"Daniel\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"LR\", \"vote\": 4215, \"vote_percentage\": 7.52, \"district\":{\"name\":\"2ème circonscription\", \"code\":2502, \"department_name\" : \"Doubs\", \"department_code\" : 25}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates


def __load_all_candidates_from_thirty_fifth_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"DEFRANCE\", \"first_name\" : \"Florence\", \"sexe\" : \"FEMININ\", \"parti_code\": \"EXG\", \"vote\": 746, \"vote_percentage\": 0.99, \"district\":{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}}, {\"last_name\" : \"DECOURCELLE\", \"first_name\" : \"Christophe\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"LR\", \"vote\": 5218, \"vote_percentage\": 6.93, \"district\":{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}}, {\"last_name\" : \"MAILLART-MÉHAIGNERIE\", \"first_name\" : \"Laurence\", \"sexe\" : \"FEMININ\", \"parti_code\": \"ENS\", \"vote\": 25792, \"vote_percentage\": 34.24, \"district\":{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}}, {\"last_name\" : \"VANHAECKE\", \"first_name\" : \"Bérénice\", \"sexe\" : \"FEMININ\", \"parti_code\": \"RN\", \"vote\": 13130, \"vote_percentage\": 17.43, \"district\":{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}}, {\"last_name\" : \"LAHAIS\", \"first_name\" : \"Tristan\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"UG\", \"vote\": 30361, \"vote_percentage\": 40.31, \"district\":{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}}, {\"last_name\" : \"HANNE\", \"first_name\" : \"Olivier\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"ECO\", \"vote\": 71, \"vote_percentage\": 0.09, \"district\":{\"name\":\"2ème circonscription\", \"code\":3502, \"department_name\" : \"Ille-et-Vilaine\", \"department_code\" : 35}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates
    
def __load_all_candidates_from_fourty_fifth_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"COLAS\", \"first_name\" : \"Cyril\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"LR\", \"vote\": 4527, \"vote_percentage\": 5.11, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"JANVIER\", \"first_name\" : \"Caroline\", \"sexe\" : \"FEMININ\", \"parti_code\": \"ENS\", \"vote\": 13263, \"vote_percentage\": 23.03, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"MEGDOUD\", \"first_name\" : \"Farida\", \"sexe\" : \"FEMININ\", \"parti_code\": \"EXG\", \"vote\": 388, \"vote_percentage\": 0.44, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"CARRANI\", \"first_name\" : \"Bruno\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"ECO\", \"vote\": 1474, \"vote_percentage\": 2.56, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"DUPLESSY\", \"first_name\" : \"Emmanuel\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"UG\", \"vote\": 16148, \"vote_percentage\": 28.03, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"CHAILLOU\", \"first_name\" : \"Yann\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVG\", \"vote\": 1951, \"vote_percentage\": 3.39, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"BABIN\", \"first_name\" : \"Elodie\", \"sexe\" : \"FEMININ\", \"parti_code\": \"RN\", \"vote\": 18957, \"vote_percentage\": 32.91, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"DUVILLARD\", \"first_name\" : \"Marie-Odile\", \"sexe\" : \"FEMININ\", \"parti_code\": \"REC\", \"vote\": 716, \"vote_percentage\": 1.24, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}, {\"last_name\" : \"AACHBOUN\", \"first_name\" : \"Ahmed\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVG\", \"vote\": 178, \"vote_percentage\": 0.31, \"district\":{\"name\":\"2ème circonscription\", \"code\":4502, \"department_name\" : \"Loiret\", \"department_code\" : 45}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates

def __load_all_candidates_from_fifty_fifth_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"GOULET\", \"first_name\" : \"Florence\", \"sexe\" : \"FEMININ\", \"parti_code\": \"RN\", \"vote\": 19011, \"vote_percentage\": 50.63, \"district\":{\"name\":\"2ème circonscription\", \"code\":5502, \"department_name\" : \"Meuse\", \"department_code\" : 55}}, {\"last_name\" : \"GOULET\", \"first_name\" : \"Pierre\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"EXG\", \"vote\": 431, \"vote_percentage\": 1.15, \"district\":{\"name\":\"2ème circonscription\", \"code\":5502, \"department_name\" : \"Meuse\", \"department_code\" : 55}}, {\"last_name\" : \"LAFLOTTE\", \"first_name\" : \"Johan\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"UG\", \"vote\": 5391, \"vote_percentage\": 14.36, \"district\":{\"name\":\"2ème circonscription\", \"code\":5502, \"department_name\" : \"Meuse\", \"department_code\" : 55}}, {\"last_name\" : \"LAFUE\", \"first_name\" : \"Valentine\", \"sexe\" : \"FEMININ\", \"parti_code\": \"ECO\", \"vote\": 742, \"vote_percentage\": 1.98, \"district\":{\"name\":\"2ème circonscription\", \"code\":5502, \"department_name\" : \"Meuse\", \"department_code\" : 55}}, {\"last_name\" : \"DUMONT\", \"first_name\" : \"Jerome\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVD\", \"vote\": 11976, \"vote_percentage\": 31.89, \"district\":{\"name\":\"2ème circonscription\", \"code\":5502, \"department_name\" : \"Meuse\", \"department_code\" : 55}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates

def __load_all_candidates_from_sixty_fifth_hundred_second_district():
    json_candidates = "[{\"last_name\":\"MEUNIER\",\"first_name\":\"François\",\"sexe\":\"MASCULIN\",\"parti_code\":\"EXG\",\"vote\":692,\"vote_percentage\":1.14,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"BÉHAGUE\",\"first_name\":\"Jacques\",\"sexe\":\"MASCULIN\",\"parti_code\":\"LR\",\"vote\":3184,\"vote_percentage\":5.24,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"DABAT\",\"first_name\":\"Jean-Marc\",\"sexe\":\"MASCULIN\",\"parti_code\":\"REG\",\"vote\":1486,\"vote_percentage\":2.45,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"MOURNET\",\"first_name\":\"Benoit\",\"sexe\":\"MASCULIN\",\"parti_code\":\"ENS\",\"vote\":15121,\"vote_percentage\":24.91,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"FÉGNÉ\",\"first_name\":\"Denis\",\"sexe\":\"MASCULIN\",\"parti_code\":\"UG\",\"vote\":17055,\"vote_percentage\":28.09,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"EL MARSNI\",\"first_name\":\"Ali\",\"sexe\":\"MASCULIN\",\"parti_code\":\"DIV\",\"vote\":0,\"vote_percentage\":0,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"MONTEIL\",\"first_name\":\"Olivier\",\"sexe\":\"MASCULIN\",\"parti_code\":\"RN\",\"vote\":22436,\"vote_percentage\":36.96,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}},{\"last_name\":\"ALVES DA CUNHA\",\"first_name\":\"Claude\",\"sexe\":\"MASCULIN\",\"parti_code\":\"REC\",\"vote\":735,\"vote_percentage\":36.96,\"district\":{\"name\":\"2ème circonscription\",\"code\":6502,\"department_name\":\"Hautes-Pyrénées\",\"department_code\":65}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates

def __load_all_candidates_from_seventy_fifth_hundred_second_district():
    json_candidates = "[{\"last_name\" : \"JOLIVEAU\", \"first_name\" : \"Charline\", \"sexe\" : \"FEMININ\", \"parti_code\": \"EXG\", \"vote\": 168, \"vote_percentage\": 0.30, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"DE WITTE\", \"first_name\" : \"Melody\", \"sexe\" : \"FEMININ\", \"parti_code\": \"RN\", \"vote\": 6206, \"vote_percentage\": 11.00, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"SACASA\", \"first_name\" : \"Clara\", \"sexe\" : \"FEMININ\", \"parti_code\": \"EXG\", \"vote\": 0, \"vote_percentage\": 0.00, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"HERZOG DE COSSÉ BRISSAC\", \"first_name\" : \"Félicité\", \"sexe\" : \"FEMININ\", \"parti_code\": \"DVD\", \"vote\": 3792, \"vote_percentage\": 6.72, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"LE GENDRE\", \"first_name\" : \"Gilles\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVC\", \"vote\": 11071, \"vote_percentage\": 19.62, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"EVANGELISTA\", \"first_name\" : \"Ornella\", \"sexe\" : \"FEMININ\", \"parti_code\": \"REC\", \"vote\": 778, \"vote_percentage\": 1.38, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"LAUSSUCQ\", \"first_name\" : \"Jean\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"ENS\", \"vote\": 13325, \"vote_percentage\": 23.62, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"LORANS\", \"first_name\" : \"Cécile Marie\", \"sexe\" : \"FEMININ\", \"parti_code\": \"ECO\", \"vote\": 512, \"vote_percentage\": 0.91, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"MARSILY\", \"first_name\" : \"Romain\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVD\", \"vote\": 1229, \"vote_percentage\": 2.18, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"MAURIANGE\", \"first_name\" : \"Frédéric\", \"sexe\" : \"MASCULIN\", \"parti_code\": \"DVC\", \"vote\": 430, \"vote_percentage\": 0.76, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"MAGNE\", \"first_name\" : \"Elise\", \"sexe\" : \"FEMININ\", \"parti_code\": \"DVG\", \"vote\": 60, \"vote_percentage\": 0.11, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}, {\"last_name\" : \"ROSSET\", \"first_name\" : \"Marine\", \"sexe\" : \"FEMININ\", \"parti_code\": \"UG\", \"vote\": 18845, \"vote_percentage\": 33.40, \"district\":{\"name\":\"2ème circonscription\", \"code\":7502, \"department_name\" : \"Paris\", \"department_code\" : 75}}]"
    candidates_obj = json.loads(json_candidates)
    candidates = __transform_to_candidates_array(candidates_obj)
    return candidates

def load_congress_persons_by_departments():
    results = {}
    json_congress_persons_by_departments = "{\"3\":[{\"code\":\"RN\",\"name\":\"Rassemblement National\",\"elected_congress_persons\":2,\"family\":5,\"congress_persons\":[{\"first_name\":\"Anne-Marie\",\"last_name\":\"THÈS\",\"parti_code\":\"RN\",\"sexe\":\"FEMININ\",\"vote\":22816,\"vote_percentage\":38.61,\"district\":{\"name\":\"1ère circonscription\",\"code\":\"301\",\"department_code\":\"3\",\"department_name\":\"Allier\"}},{\"first_name\":\"Rémy\",\"last_name\":\"QUENEY\",\"parti_code\":\"RN\",\"sexe\":\"MASCULIN\",\"vote\":20270,\"vote_percentage\":37.82,\"district\":{\"name\":\"3ème circonscription\",\"code\":\"303\",\"department_code\":\"3\",\"department_name\":\"Allier\"}}]},{\"code\":\"UG\",\"name\":\"Union de la gauche\",\"elected_congress_persons\":1,\"family\":2,\"congress_persons\":[{\"first_name\":\"Yannick\",\"last_name\":\"MONNET\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":17043,\"vote_percentage\":28.84,\"district\":{\"name\":\"1ère circonscription\",\"code\":\"301\",\"department_code\":\"3\",\"department_name\":\"Allier\"}}]}],\"15\":[{\"code\":\"UXD\",\"name\":\"Union de l'extrême droite\",\"elected_congress_persons\":1,\"family\":5,\"congress_persons\":[{\"first_name\":\"Bartolomé\",\"last_name\":\"LENOIR\",\"parti_code\":\"UXD\",\"sexe\":\"MASCULIN\",\"vote\":20403,\"vote_percentage\":33.35,\"district\":{\"name\":\"1ère circonscription\",\"code\":\"1501\",\"department_code\":\"15\",\"department_name\":\"Cantal\"}}]}],\"33\":[{\"code\":\"UG\",\"name\":\"Union de la gauche\",\"elected_congress_persons\":4,\"family\":2,\"congress_persons\":[{\"first_name\":\"Loïc\",\"last_name\":\"PRUD'HOMME\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":30664,\"vote_percentage\":49.83,\"district\":{\"name\":\"3ème circonscription\",\"code\":\"3303\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Marie\",\"last_name\":\"RECALDE\",\"parti_code\":\"UG\",\"sexe\":\"FEMININ\",\"vote\":27564,\"vote_percentage\":35.24,\"district\":{\"name\":\"6ème circonscription\",\"code\":\"3306\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Alain\",\"last_name\":\"DAVID\",\"parti_code\":\"UG\",\"sexe\":\"MASCULIN\",\"vote\":27092,\"vote_percentage\":42.36,\"district\":{\"name\":\"4ème circonscription\",\"code\":\"3304\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Pascale\",\"last_name\":\"GOT\",\"parti_code\":\"UG\",\"sexe\":\"FEMININ\",\"vote\":26631,\"vote_percentage\":31.79,\"district\":{\"name\":\"5ème circonscription\",\"code\":\"3305\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}}]},{\"code\":\"RN\",\"name\":\"Rassemblement National\",\"elected_congress_persons\":4,\"family\":5,\"congress_persons\":[{\"first_name\":\"Grégoire\",\"last_name\":\"DE FOURNAS\",\"parti_code\":\"RN\",\"sexe\":\"MASCULIN\",\"vote\":35457,\"vote_percentage\":42.32,\"district\":{\"name\":\"5ème circonscription\",\"code\":\"3305\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Edwige\",\"last_name\":\"DIAZ\",\"parti_code\":\"RN\",\"sexe\":\"FEMININ\",\"vote\":34590,\"vote_percentage\":53.33,\"district\":{\"name\":\"11ème circonscription\",\"code\":\"3311\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Laurent\",\"last_name\":\"LAMARA\",\"parti_code\":\"RN\",\"sexe\":\"MASCULIN\",\"vote\":31248,\"vote_percentage\":36.86,\"district\":{\"name\":\"8ème circonscription\",\"code\":\"3308\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"François-Xavier\",\"last_name\":\"MARQUES\",\"parti_code\":\"RN\",\"sexe\":\"MASCULIN\",\"vote\":27868,\"vote_percentage\":38.54,\"district\":{\"name\":\"9ème circonscription\",\"code\":\"3309\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}}]},{\"code\":\"ENS\",\"name\":\"Ensemble ! (Majorité présidentielle)\",\"elected_congress_persons\":4,\"family\":3,\"congress_persons\":[{\"first_name\":\"Thomas\",\"last_name\":\"CAZENAVE\",\"parti_code\":\"ENS\",\"sexe\":\"MASCULIN\",\"vote\":28564,\"vote_percentage\":38.31,\"district\":{\"name\":\"1ère circonscription\",\"code\":\"3301\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Sophie\",\"last_name\":\"PANONACLE\",\"parti_code\":\"ENS\",\"sexe\":\"FEMININ\",\"vote\":26881,\"vote_percentage\":31.71,\"district\":{\"name\":\"8ème circonscription\",\"code\":\"3308\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Eric\",\"last_name\":\"POULLIAT\",\"parti_code\":\"ENS\",\"sexe\":\"MASCULIN\",\"vote\":25636,\"vote_percentage\":32.78,\"district\":{\"name\":\"6ème circonscription\",\"code\":\"3306\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}},{\"first_name\":\"Sophie\",\"last_name\":\"METTE\",\"parti_code\":\"ENS\",\"sexe\":\"FEMININ\",\"vote\":21714,\"vote_percentage\":30.03,\"district\":{\"name\":\"9ème circonscription\",\"code\":\"3309\",\"department_code\":\"33\",\"department_name\":\"Gironde\"}}]}]}"
    parties_obj = json.loads(json_congress_persons_by_departments)
    for key in parties_obj : 
        parties_department = parties_obj[key]
        parties = __transform_to_parties_array(parties_department)
        results[key] = parties
    return results

#TODO improve 
def __transform_to_parties_array(parties_obj):
    all_parties = []
    for party_obj in parties_obj:
            party = Party()
            party.code = party_obj["code"]
            party.name = party_obj["name"]
            party.family = party_obj["family"]
            party.congress_persons = __transform_to_candidates_array(party_obj["congress_persons"])
            all_parties.append(party)
    return all_parties

def __transform_to_candidates_array_second_form(candidates_obj):
    all_candidates = []
    for candidate_obj in candidates_obj:
        candidate = CongressPerson()
        candidate.first_name = candidate_obj["first_name"]
        candidate.last_name = candidate_obj["last_name"]
        candidate.sexe = candidate_obj["sexe"]
        candidate.parti_code = candidate_obj["party_code"]
        candidate.vote = candidate_obj["vote"]
        candidate.vote_percentage = candidate_obj["vote_percentage"]
        all_candidates.append(candidate)
    return all_candidates

def __transform_to_candidates_array(candidates_obj):
    all_candidates = []
    for candidate_obj in candidates_obj:
        candidate = CongressPerson()
        candidate.first_name = candidate_obj["first_name"]
        candidate.last_name = candidate_obj["last_name"]
        candidate.sexe = candidate_obj["sexe"]
        candidate.parti_code = candidate_obj["parti_code"]
        candidate.vote = candidate_obj["vote"]
        candidate.vote_percentage = candidate_obj["vote_percentage"]
        candidate.district = __transform_district_json_to_district_obj(candidate_obj["district"])
        all_candidates.append(candidate)
    return all_candidates

#TODO centralise
def __transform_district_json_to_district_obj(district_obj):
    district = District()
    district.code = district_obj["code"]
    district.department_code = district_obj["department_code"]
    district.department_name = district_obj["department_name"]
    district.name = district_obj["name"]
    return district


def load_candidates_from_name(last_names):
    candidates_search  =[]
    all_candidates = load_all_candidates()
    for candidate in all_candidates : 
        for last_name in last_names : 
            if candidate.last_name == last_name: 
                candidates_search.append(candidate)
            else :
                continue
    return candidates_search