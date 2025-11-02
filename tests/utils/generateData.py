from src.backend.domain.models.factory import factory_congress_person, factory_district, factory_party
from src.backend.infrastructure.models.factory_record import factory_candidate_record, factory_department_record, factory_district_record, factory_election_record, factory_elections_result_record


def get_candidates_from_all_districts():
    all_candidates_from_all_districts =[get_candidates_from_first_district_choosen(), get_candidates_from_second_district_choosen(),
                                        get_candidates_from_third_district_choosen(), get_candidates_from_fourth_district_choosen(),
                                        get_candidates_from_fifth_district_choosen(), get_candidates_from_sixth_district_choosen(),
                                        get_candidates_from_seventh_district_choosen()]
    return all_candidates_from_all_districts

def get_candidates_from_first_district_choosen():
    candidates = [__build_first_candidate_first_district(), __build_second_candidate_first_district(), 
                  __build_third_candidate_first_district(), __build_fourth_candidate_first_district(), 
                  __build_fifth_candidate_first_district()]
    return candidates

def __build_first_candidate_first_district():
    candidate = factory_congress_person("GUIGNARD", "Boris", "MASCULIN", "DXG", 394, 1.02, build_first_district())
    return candidate

def __build_second_candidate_first_district():
    candidate = factory_congress_person("FINE", "Sébastien", "MASCULIN", "ENS", 10338, 26.70, build_first_district())
    return candidate

def __build_third_candidate_first_district():
    candidate = factory_congress_person("ROSSI", "Valérie", "FEMININ", "UG", 12661, 32.70, build_first_district())
    return candidate

def __build_fourth_candidate_first_district():
    candidate = factory_congress_person("MONDAIN", "Johann", "MASCULIN", "DIV", 2260, 5.70, build_first_district())
    return candidate

def __build_fifth_candidate_first_district():
    candidate = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, build_first_district())
    return candidate

def build_first_district():
    district = factory_district("2ème circonscription", 502, "Hautes-Alpes", 5)
    return district

def get_candidates_from_second_district_choosen():
    candidates = [__build_first_candidate_second_district(), __build_second_candidate_second_district(), 
                  __build_third_candidate_second_district(), __build_fourth_candidate_second_district(), 
                  __build_fifth_candidate_second_district(), __build_sixth_candidate_second_district(),
                  __build_seventh_candidate_second_district()]
    return candidates

def __build_first_candidate_second_district():
    candidate = factory_congress_person("CHEIKHI", "Mona", "FEMININ", "EXG", 298, 0.83, build_second_district())
    return candidate

def __build_second_candidate_second_district():
    candidate = factory_congress_person("PÉBAY", "Zoé", "FEMININ", "UG", 4919, 13.62, build_second_district())
    return candidate

def __build_third_candidate_second_district():
    candidate = factory_congress_person("LACROIX", "Gilles", "MASCULIN", "RN", 11923, 33.02, build_second_district())
    return candidate

def __build_fourth_candidate_second_district():
    candidate = factory_congress_person("VEYSSET-RAPAPORT", "Pascal", "MASCULIN", "REC", 220, 0.61, build_second_district())
    return candidate

def __build_fifth_candidate_second_district():
    candidate = factory_congress_person("TILMANT-TATISCHEFF", "Vladimir", "MASCULIN", "ENS", 3019, 8.36, build_second_district())
    return candidate

def __build_sixth_candidate_second_district():
    candidate = factory_congress_person("TOTY", "Louis", "MASCULIN", "DVD", 3348, 9.27, build_second_district())
    return candidate

def __build_seventh_candidate_second_district():
    candidate = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, build_second_district())
    return candidate

def build_second_district():
    district = factory_district("2ème circonscription", 1502, "Cantal", 15)
    return district

def get_candidates_from_third_district_choosen():
    candidates = [__build_first_candidate_third_district(), __build_second_candidate_third_district(), 
                  __build_third_candidate_third_district(), __build_fourth_candidate_third_district(), 
                  __build_fifth_candidate_third_district()]
    return candidates

def __build_first_candidate_third_district():
    candidate = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, build_third_district())
    return candidate

def __build_second_candidate_third_district():
    candidate = factory_congress_person("VUITTON", "Brigitte", "FEMININ", "EXG", 788, 1.41, build_third_district())
    return candidate

def __build_third_candidate_third_district():
    candidate = factory_congress_person("FUSIS", "Eric", "MASCULIN", "RN", 16895, 30.12, build_third_district())
    return candidate

def __build_fourth_candidate_third_district():
    candidate = factory_congress_person("VUILLEMIN", "Benoît", "MASCULIN", "ENS", 15026, 26.79, build_third_district())
    return candidate

def __build_fifth_candidate_third_district():
    candidate = factory_congress_person("ROY", "Daniel", "MASCULIN", "LR", 4215, 7.52, build_third_district())
    return candidate

def build_third_district():
    district = factory_district("2ème circonscription", 2502, "Doubs", 25)
    return district

def get_candidates_from_fourth_district_choosen():
    candidates = [__build_first_candidate_fourth_district(), __build_second_candidate_fourth_district(), 
                  __build_third_candidate_fourth_district(), __build_fourth_candidate_fourth_district(), 
                  __build_fifth_candidate_fourth_district(), __build_sixth_candidate_fourth_district()]
    return candidates

def __build_first_candidate_fourth_district():
    candidate = factory_congress_person("DEFRANCE", "Florence", "FEMININ", "EXG", 746, 0.99, build_fourth_district())
    return candidate

def __build_second_candidate_fourth_district():
    candidate = factory_congress_person("DECOURCELLE", "Christophe", "MASCULIN", "LR", 5218, 6.93, build_fourth_district())
    return candidate

def __build_third_candidate_fourth_district():
    candidate = factory_congress_person("MAILLART-MÉHAIGNERIE", "Laurence", "FEMININ", "ENS", 25792, 34.24, build_fourth_district())
    return candidate

def __build_fourth_candidate_fourth_district():
    candidate = factory_congress_person("VANHAECKE", "Bérénice", "FEMININ", "RN", 13130, 17.43, build_fourth_district())
    return candidate

def __build_fifth_candidate_fourth_district():
    candidate = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, build_fourth_district())
    return candidate

def __build_sixth_candidate_fourth_district():
    candidate = factory_congress_person("HANNE", "Olivier", "MASCULIN", "ECO", 71, 0.09, build_fourth_district())
    return candidate

def build_fourth_district():
    district = factory_district("2ème circonscription", 3502, "Ille-et-Vilaine", 35)
    return district

def get_candidates_from_fifth_district_choosen():
    candidates = [__build_first_candidate_fifth_district(), __build_second_candidate_fifth_district(), 
                  __build_third_candidate_fifth_district(), __build_fourth_candidate_fifth_district(), 
                  __build_fifth_candidate_fifth_district(), __build_sixth_candidate_fifth_district(), 
                  __build_seventh_candidate_fifth_district(), __build_eighth_candidate_fifth_district(), 
                  __build_nineth_candidate_fifth_district()]
    return candidates

def __build_first_candidate_fifth_district():
    candidate = factory_congress_person("COLAS", "Cyril", "MASCULIN", "LR", 4527, 5.11, build_fifth_district())
    return candidate 
 
def __build_second_candidate_fifth_district():
    candidate = factory_congress_person("JANVIER", "Caroline", "FEMININ", "ENS", 13263, 23.03, build_fifth_district())
    return candidate

def __build_third_candidate_fifth_district():
    candidate = factory_congress_person("MEGDOUD", "Farida", "FEMININ", "EXG", 388, 0.44, build_fifth_district())
    return candidate

def __build_fourth_candidate_fifth_district():
    candidate = factory_congress_person("CARRANI", "Bruno", "MASCULIN", "ECO", 1474, 2.56, build_fifth_district())
    return candidate

def __build_fifth_candidate_fifth_district():
    candidate = factory_congress_person("DUPLESSY", "Emmanuel", "MASCULIN", "UG", 16148, 28.03, build_fifth_district())
    return candidate

def __build_sixth_candidate_fifth_district():
    candidate = factory_congress_person("CHAILLOU", "Yann", "MASCULIN", "DVG", 1951, 3.39, build_fifth_district())
    return candidate

def __build_seventh_candidate_fifth_district():
    candidate = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, build_fifth_district())
    return candidate

def __build_eighth_candidate_fifth_district():
    candidate = factory_congress_person("DUVILLARD", "Marie-Odile", "FEMININ", "REC", 716, 1.24, build_fifth_district())
    return candidate

def __build_nineth_candidate_fifth_district():
    candidate = factory_congress_person("AACHBOUN", "Ahmed", "MASCULIN", "DVG", 178, 0.31, build_fifth_district())
    return candidate 

def build_fifth_district():
    district = factory_district("2ème circonscription", 4502, "Loiret", 45)
    return district

def get_candidates_from_sixth_district_choosen():
    candidates = [__build_first_candidate_sixth_district(), __build_second_candidate_sixth_district(), 
                  __build_third_candidate_sixth_district(), __build_fourth_candidate_sixth_district(), 
                  __build_fifth_candidate_sixth_district()]
    return candidates

def __build_first_candidate_sixth_district():
    candidate = factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, build_sixth_district())
    return candidate

def __build_second_candidate_sixth_district():
    candidate = factory_congress_person("NORDEMANN", "Pierre", "MASCULIN", "EXG", 431, 1.15, build_sixth_district())
    return candidate

def __build_third_candidate_sixth_district():
    candidate = factory_congress_person("LAFLOTTE", "Johan", "MASCULIN", "UG", 5391, 14.36, build_sixth_district())
    return candidate

def __build_fourth_candidate_sixth_district():
    candidate = factory_congress_person("LAFUE", "Valentine", "FEMININ", "ECO", 742, 1.98, build_sixth_district())
    return candidate

def __build_fifth_candidate_sixth_district():
    candidate = factory_congress_person("DUMONT", "Jerome", "MASCULIN", "DVD", 11976, 31.89, build_sixth_district())
    return candidate

def build_sixth_district():
    district = factory_district("2ème circonscription", 5502, "Meuse", 55)
    return district


def get_candidates_from_seventh_district_choosen():
    candidates = [__build_first_candidate_seventh_district(), __build_second_candidate_seventh_district(), 
                  __build_third_candidate_seventh_district(), __build_fourth_candidate_seventh_district(), 
                  __build_fifth_candidate_seventh_district(), __build_sixth_candidate_seventh_district(), 
                  __build_seventh_candidate_seventh_district(), __build_eighth_candidate_seventh_district(), 
                  __build_nineth_candidate_seventh_district(), __build_tenth_candidate_seventh_district(), 
                  __build_eleventh_candidate_seventh_district(), __build_twelveth_candidate_seventh_district()]
    return candidates

def __build_first_candidate_seventh_district():
    candidate = factory_congress_person("JOLIVEAU", "Charline", "FEMININ", "EXG", 168, 0.30, build_seventh_district())
    return candidate

def __build_second_candidate_seventh_district():
    candidate = factory_congress_person("DE WITTE", "Melody", "FEMININ", "RN", 6206, 11.00, build_seventh_district())
    return candidate

def __build_third_candidate_seventh_district():
    candidate = factory_congress_person("SACASA", "Clara", "FEMININ", "EXG", 0, 0.00, build_seventh_district())
    return candidate

def __build_fourth_candidate_seventh_district():
    candidate = factory_congress_person("HERZOG DE COSSÉ BRISSAC", "Félicité", "FEMININ", "DVD", 3792, 6.72, build_seventh_district())
    return candidate

def __build_fifth_candidate_seventh_district():
    candidate = factory_congress_person("LE GENDRE", "Gilles", "MASCULIN", "DVC", 11071, 19.62, build_seventh_district())
    return candidate

def __build_sixth_candidate_seventh_district():
    candidate = factory_congress_person("EVANGELISTA", "Ornella", "FEMININ", "REC",  778, 1.38, build_seventh_district())
    return candidate

def __build_seventh_candidate_seventh_district():
    candidate = factory_congress_person("LAUSSUCQ", "Jean", "MASCULIN", "ENS", 13325, 23.62, build_seventh_district())
    return candidate

def __build_eighth_candidate_seventh_district():
    candidate = factory_congress_person("LORANS", "Cécile Marie", "FEMININ", "ECO", 512, 0.91, build_seventh_district())
    return candidate

def __build_nineth_candidate_seventh_district():
    candidate = factory_congress_person("MARSILY", "Romain", "MASCULIN", "DVD", 1229, 2.18, build_seventh_district())
    return candidate

def __build_tenth_candidate_seventh_district():
    candidate = factory_congress_person("MAURIANGE", "Frédéric","MASCULIN", "DVC", 430, 0.76, build_seventh_district())
    return candidate

def __build_eleventh_candidate_seventh_district():
    candidate = factory_congress_person("MAGNE", "Elise", "FEMININ", "DVG", 60, 0.11, build_seventh_district())
    return candidate

def __build_twelveth_candidate_seventh_district():
    candidate = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, build_seventh_district())
    return candidate

def build_seventh_district():
    district = factory_district("2ème circonscription", 7502, "Paris", 75)
    return district


def get_all_parties_without_elected_persons_2024():
    parties = []
    parties.append(factory_party('Extrême gauche', 'EXG', 0, []))
    parties.append(factory_party('Parti communiste français', 'COM', 0, []))
    parties.append(factory_party('La France insoumise','FI',  0, []))
    parties.append(factory_party('Parti socialiste','SOC',  0, []))
    parties.append(factory_party('Parti radical de gauche','RDG',  0, []))
    parties.append(factory_party('Les Ecologistes','VEC',  0, []))
    parties.append(factory_party('Divers gauche','DVG',  0, []))
    parties.append(factory_party('Union de la gauche','UG', 0, []))
    parties.append(factory_party('Ecologistes','ECO',  0, []))
    parties.append(factory_party('Régionaliste','REG', 0, []))
    parties.append(factory_party('Divers','DIV', 0, []))
    parties.append(factory_party('Renaissance','REN', 0, []))
    parties.append(factory_party('Modem', 'MDM', 0, []))
    parties.append(factory_party('Horizons', 'HOR', 0, []))
    parties.append(factory_party('Ensemble ! (Majorité présidentielle)', 'ENS', 0, []))
    parties.append(factory_party('Divers centre', 'DVC', 0, []))
    parties.append(factory_party('Union des Démocrates et Indépendants', 'UDI', 0, []))
    parties.append(factory_party('Les Républicains', 'LR', 0, []))
    parties.append(factory_party('Divers droite', 'DVD', 0, []))
    parties.append(factory_party('Droite souverainiste', 'DSV', 0, []))
    parties.append(factory_party('Rassemblement National', 'RN', 0, []))
    parties.append(factory_party('Reconquête !', 'REC', 0, []))
    parties.append(factory_party('Union de l\'extrême droite', 'UXD', 0, []))
    parties.append(factory_party('Extrême droite', 'EXD', 0, []))
    return parties

def get_parties_with_elected_persons_2024(first_percentage, second_percentage, third_percentage):
    parties = []
    _first_elected_person_ug = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, build_third_district())
    _second_elected_person_ug = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, build_fourth_district())
    _third_elected_person_ug = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, build_seventh_district())
    parties.append(factory_party('Union de la gauche','UG', first_percentage, [_first_elected_person_ug, _second_elected_person_ug, _third_elected_person_ug]))
    first_elected_person_lr = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, build_second_district())
    parties.append(factory_party('Les Républicains', 'LR', second_percentage, [first_elected_person_lr]))
    first_elected_person_rn = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, build_first_district())
    second_elected_person_rn = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, build_fifth_district())
    third_elected_person_rn =factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, build_sixth_district())
    parties.append(factory_party('Rassemblement National', 'RN', third_percentage, [first_elected_person_rn, second_elected_person_rn, third_elected_person_rn]))
    return parties

def get_results_elections_2024():
    results = factory_elections_result_record([__construct_election()])
    return results        
    
def __construct_election(): 
    districts = [__construct_district_502(), __construct_district_1502(), __construct_district_2502(), 
                    __construct_district_3502(), __construct_district_4502(), __construct_district_5502(), 
                    __construct_district_6502(), __construct_district_7502()]
    election = factory_election_record(2024, districts)
    return election        

def __construct_district_502():
    first_candidate = factory_candidate_record("GUIGNARD", "Boris", "MASCULIN", "EXG", 394, 0.72, 1.02)
    second_candidate = factory_candidate_record("FINE", "Sébastien", "MASCULIN", "ENS", 10338, 18.96, 26.70)
    third_candidate = factory_candidate_record("ROSSI", "Valérie", "FEMININ", "UG", 12661, 23.22, 32.7)
    fourth_candidate = factory_candidate_record("MONDAIN", "Johann", "MASCULIN", "DIV", 2206, 4.05, 5.70)
    fifth_candidate = factory_candidate_record("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 24.06, 33.88)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    district = factory_district_record("2ème circonscription", 502, 5, 54517, 39716, candidates)
    return district

def __construct_district_1502():
    first_candidate = factory_candidate_record("CHEIKHI", "Mona", "FEMININ", "EXG", 298, 0.57, 0.83)
    second_candidate = factory_candidate_record("PÉBAY", "Zoé", "FEMININ", "UG", 4919, 9.40, 13.62)
    third_candidate = factory_candidate_record("LACROIX", "Gilles", "MASCULIN", "RN", 11923, 22.79, 33.02)
    fourth_candidate = factory_candidate_record("VEYSSET-RAPAPORT", "Pascal", "MASCULIN", "REC", 220, 0.42, 0.61)
    fifth_candidate = factory_candidate_record("TILMANT-TATISCHEFF", "Vladimir", "MASCULIN", "ENS", 3019, 5.77, 8.36)
    sixth_candidate = factory_candidate_record("TOTY", "Louis", "MASCULIN", "DVD", 3348, 6.4, 9.27)
    seventh_candidate = factory_candidate_record("BONY", "Jean Yves", "MASCULIN", "DVD", 12383, 23.67, 34.29)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, 
                    sixth_candidate, seventh_candidate]
    district = factory_district_record("2ème circonscription", 1502, 15, 52310, 37078, candidates)
    return district

def __construct_district_2502():
    first_candidate = factory_candidate_record("VOYNET", "Dominique", "FEMININ", "UG", 19160, 24.29, 34.16)
    second_candidate = factory_candidate_record("VUITTON", "Brigitte", "FEMININ", "EXG", 788, 1.00, 1.41)
    third_candidate = factory_candidate_record("FUSIS", "Eric", "MASCULIN", "RN", 16895, 21.42, 30.12)
    fourth_candidate = factory_candidate_record("VUILLEMIN", "Benoît", "MASCULIN", "ENS", 15026, 19.05, 26.79)
    fifth_candidate = factory_candidate_record("ROY", "Daniel", "MASCULIN", "LR", 4215, 5.34, 7.52)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    district = factory_district_record("2ème circonscription", 2502, 25, 78875, 57350, candidates)
    return district

def __construct_district_3502():
    first_candidate = factory_candidate_record("DEFRANCE", "Florence", "FEMININ", "EXG", 746, 0.75, 0.99)
    second_candidate = factory_candidate_record("DECOURCELLE", "Christophe", "MASCULIN", "LR", 5218, 5.22, 6.93)
    third_candidate = factory_candidate_record("MAILLART-MÉHAIGNERIE", "Laurence", "FEMININ", "ENS", 25792, 25.82, 34.24)
    fourth_candidate = factory_candidate_record("VUILLEVANHAECKEMIN", "Bérénice", "FEMININ", "RN", 13130, 13.14, 17.43)
    fifth_candidate = factory_candidate_record("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 30.39, 40.31)
    sixth_candidate = factory_candidate_record("HANNE", "Olivier", "MASCULIN", "ECO", 71, 0.07, 0.09)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
    district = factory_district_record("2ème circonscription", 3502, 35, 99900, 76790, candidates)
    return district  

def __construct_district_4502():
    first_candidate = factory_candidate_record("COLAS", "Cyril", "MASCULIN", "LR", 4527, 5.11, 7.86)
    second_candidate = factory_candidate_record("JANVIER", "Caroline", "FEMININ", "ENS", 13263, 14.97, 23.03)
    third_candidate = factory_candidate_record("MEGDOUD", "Farida", "FEMININ", "EXG", 388, 0.44, 0.67)
    fourth_candidate = factory_candidate_record("CARRANI", "Bruno", "MASCULIN", "ECO", 1474, 1.66, 2.56)
    fifth_candidate = factory_candidate_record("DUPLESSY", "Emmanuel", "MASCULIN", "UG", 16148, 18.23, 28.03)
    sixth_candidate = factory_candidate_record("CHAILLOU", "Yann", "MASCULIN", "DVG", 1951, 2.20, 3.39)
    seventh_candidate = factory_candidate_record("BABIN", "Elodie", "FEMININ", "RN", 18957, 21.4, 32.91)
    eighth_candidate = factory_candidate_record("DUVILLARD", "Marie-Odile", "FEMININ", "REC", 716, 0.81, 1.24)
    nineth_candidate = factory_candidate_record("AACHBOUN", "Ahmed", "MASCULIN", "DVG", 178, 0.2, 0.31)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                    seventh_candidate, eighth_candidate, nineth_candidate]
    district = factory_district_record("2ème circonscription", 4502, 45, 88601, 58836, candidates)
    return district

def __construct_district_5502():
    first_candidate = factory_candidate_record("GOULET", "Florence", "FEMININ", "RN", 19011, 32.10, 50.63)
    second_candidate = factory_candidate_record("NORDEMANN", "Pierre", "MASCULIN", "ENS", 13263, 14.97, 23.03)
    third_candidate = factory_candidate_record("MEGDOUD", "Farida", "FEMININ", "EXG", 431, 0.73, 1.15)
    fourth_candidate = factory_candidate_record("LAFLOTTE", "Johan", "MASCULIN", "UG", 5391, 9.10, 14.36)
    fifth_candidate = factory_candidate_record("LAFUE", "Valentine", "FEMININ", "ECO", 742, 1.25, 1.98)
    sixth_candidate = factory_candidate_record("DUMONT", "Jerome", "MASCULIN", "DVD", 11976, 20.22, 31.89)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
    district = factory_district_record("2ème circonscription", 5502, 55, 59230, 38599, candidates)               
    return district  

def __construct_district_6502():
    first_candidate = factory_candidate_record("MEUNIER", "François", "MASCULIN", "EXG", 692, 0.78, 1.14)
    second_candidate = factory_candidate_record("BÉHAGUE", "Jacques", "MASCULIN", "LR", 3184, 3.60, 5.24)
    third_candidate = factory_candidate_record("DABAT", "Jean-Marc", "MASCULIN", "REG", 1486, 1.68, 2.45)
    fourth_candidate = factory_candidate_record("MOURNET", "Benoit", "MASCULIN", "ENS", 15121, 17.09, 24.91)
    fifth_candidate = factory_candidate_record("FÉGNÉ", "Denis", "MASCULIN", "UG", 17055, 19.27, 28.09)
    sixth_candidate = factory_candidate_record("EL MARSNI", "Ali", "MASCULIN", "DIV", 0, 0.00, 0.0)
    seventh_candidate = factory_candidate_record("MONTEIL", "Olivier", "MASCULIN", "RN", 22436, 25.35, 36.96)
    eighth_candidate = factory_candidate_record("ALVES DA CUNHA", "Claude", "MASCULIN", "REC", 735, 0.83, 1.21)        
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                    seventh_candidate, eighth_candidate]
    district = factory_district_record("2ème circonscription", 6502, 65, 88496, 62793, candidates)               
    return district

def __construct_district_7502():
    first_candidate = factory_candidate_record("JOLIVEAU", "Charline", "FEMININ", "EXG", 168, 0.23, 0.30)
    second_candidate = factory_candidate_record("DE WITTE", "Melody", "FEMININ", "RN", 6206, 8.32, 11.00)
    third_candidate = factory_candidate_record("SACASA", "Clara", "FEMININ", "EXG", 0, 0.00, 0.00)
    fourth_candidate = factory_candidate_record("HERZOG DE COSSÉ BRISSAC", "Félicité", "FEMININ", "DVD", 3792, 5.08, 6.72)
    fifth_candidate = factory_candidate_record("LE GENDRE", "Gilles", "MASCULIN", "DVC", 11071, 14.84, 19.62)
    sixth_candidate = factory_candidate_record("EVANGELISTA", "Ornella", "FEMININ", "REC", 778, 1.04, 1.38)
    seventh_candidate = factory_candidate_record("LAUSSUCQ", "Jean", "MASCULIN", "RENSN", 13325, 17.87, 23.62)
    eighth_candidate = factory_candidate_record("LORANS", "Cécile Marie", "FEMININ", "ECO", 512, 0.68, 0.91)     
    nineth_candidate = factory_candidate_record("MARSILY", "Romain", "MASCULIN", "DVD", 1229, 1.65, 2.18)
    tenth_candidate = factory_candidate_record("MAURIANGE", "Frédéric", "MASCULIN", "DVC", 430, 0.58, 0.76)
    eleventh_candidate = factory_candidate_record("MAGNE", "Elise", "FEMININ", "DVG", 60, 0.08, 0.11)
    twelth_candidate = factory_candidate_record("ROSSET", "Marine", "FEMININ", "UG", 18845, 25.27, 33.4)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                    seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate, eleventh_candidate, 
                    twelth_candidate]
    district = factory_district_record("2ème circonscription", 7502, 75, 74579, 56908, candidates)               
    return district