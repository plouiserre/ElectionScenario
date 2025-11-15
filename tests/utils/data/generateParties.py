from src.backend.domain.models.factory import factory_congress_person, factory_party
from src.backend.infrastructure.models.factory_record import factory_party_record
from tests.utils.data.catalogData import generate_datas

def get_all_parties_without_elected_persons_2024():
    parties = []
    parties.append(factory_party('Extrême gauche', 'EXG', []))
    parties.append(factory_party('Parti communiste français', 'COM', []))
    parties.append(factory_party('La France insoumise','FI',  []))
    parties.append(factory_party('Parti socialiste','SOC',  []))
    parties.append(factory_party('Parti radical de gauche','RDG',  []))
    parties.append(factory_party('Les Ecologistes','VEC',  []))
    parties.append(factory_party('Divers gauche','DVG',  []))
    parties.append(factory_party('Union de la gauche','UG', []))
    parties.append(factory_party('Ecologistes','ECO',  []))
    parties.append(factory_party('Régionaliste','REG', []))
    parties.append(factory_party('Divers','DIV', []))
    parties.append(factory_party('Renaissance','REN', []))
    parties.append(factory_party('Modem', 'MDM', []))
    parties.append(factory_party('Horizons', 'HOR', []))
    parties.append(factory_party('Ensemble ! (Majorité présidentielle)', 'ENS', []))
    parties.append(factory_party('Divers centre', 'DVC', []))
    parties.append(factory_party('Union des Démocrates et Indépendants', 'UDI', []))
    parties.append(factory_party('Les Républicains', 'LR', []))
    parties.append(factory_party('Divers droite', 'DVD', []))
    parties.append(factory_party('Droite souverainiste', 'DSV', []))
    parties.append(factory_party('Rassemblement National', 'RN', []))
    parties.append(factory_party('Reconquête !', 'REC', []))
    parties.append(factory_party('Union de l\'extrême droite', 'UXD', []))
    parties.append(factory_party('Extrême droite', 'EXD', []))
    return parties

def get_parties_with_elected_persons_2024():
    parties = []
    _first_elected_person_ug = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, generate_datas("district","third_district",""))
    _second_elected_person_ug = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, generate_datas("district","fourth_district",""))
    _third_elected_person_ug = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, generate_datas("district","seventh_district",""))
    parties.append(factory_party('Union de la gauche','UG', [_first_elected_person_ug, _second_elected_person_ug, _third_elected_person_ug]))
    first_elected_person_lr = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, generate_datas("district","second_district",""))
    parties.append(factory_party('Les Républicains', 'LR', [first_elected_person_lr]))
    first_elected_person_rn = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, generate_datas("district","first_district",""))
    second_elected_person_rn = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, generate_datas("district","fifth_district",""))
    third_elected_person_rn =factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, generate_datas("district","sixth_district",""))
    parties.append(factory_party('Rassemblement National', 'RN', [first_elected_person_rn, second_elected_person_rn, third_elected_person_rn]))
    return parties

def generate_parties_record():
        parties = []
        parties.append(factory_party_record('Extrême gauche', 'EXG'))
        parties.append(factory_party_record('Parti communiste français', 'COM'))
        parties.append(factory_party_record('La France insoumise','FI'))
        parties.append(factory_party_record('Parti socialiste','SOC'))
        parties.append(factory_party_record('Parti radical de gauche','RDG'))
        parties.append(factory_party_record('Les Ecologistes','VEC'))
        parties.append(factory_party_record('Divers gauche','DVG'))
        parties.append(factory_party_record('Union de la gauche','UG'))
        parties.append(factory_party_record('Ecologistes','ECO'))
        parties.append(factory_party_record('Régionaliste','REG'))
        parties.append(factory_party_record('Divers','DIV'))
        parties.append(factory_party_record('Renaissance','REN'))
        parties.append(factory_party_record('Modem', 'MDM'))
        parties.append(factory_party_record('Horizons', 'HOR'))
        parties.append(factory_party_record('Ensemble ! (Majorité présidentielle)', 'ENS'))
        parties.append(factory_party_record('Divers centre', 'DVC'))
        parties.append(factory_party_record('Union des Démocrates et Indépendants', 'UDI'))
        parties.append(factory_party_record('Les Républicains', 'LR'))
        parties.append(factory_party_record('Divers droite', 'DVD'))
        parties.append(factory_party_record('Droite souverainiste', 'DSV'))
        parties.append(factory_party_record('Rassemblement National', 'RN'))
        parties.append(factory_party_record('Reconquête !', 'REC'))
        parties.append(factory_party_record('Union de l\'extrême droite', 'UXD'))
        parties.append(factory_party_record('Extrême droite', 'EXD'))
        return parties