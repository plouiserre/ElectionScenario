from src.backend.domain.models.factory import factory_congress_person, factory_party
from tests.utils.data.generateDataDistricts import build_first_district, build_second_district, build_third_district, build_fourth_district, build_fifth_district, build_sixth_district, build_seventh_district

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