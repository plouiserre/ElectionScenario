from src.backend.domain.models.factory import factory_congress_person, factory_party
from src.backend.infrastructure.models.factory_record import factory_party_record
from tests.utils.data.catalog.catalogData import generate_datas

def get_parties_with_elected_persons_2024():
    parties = []
    _first_elected_person_ug = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, generate_datas("district","third_district"))
    _second_elected_person_ug = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, generate_datas("district","fourth_district"))
    _third_elected_person_ug = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, generate_datas("district","seventh_district"))
    parties.append(factory_party('Union de la gauche','UG', [_first_elected_person_ug, _second_elected_person_ug, _third_elected_person_ug]))
    first_elected_person_lr = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, generate_datas("district","second_district"))
    parties.append(factory_party('Les Républicains', 'LR', [first_elected_person_lr]))
    first_elected_person_rn = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, generate_datas("district","first_district"))
    second_elected_person_rn = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, generate_datas("district","fifth_district"))
    third_elected_person_rn =factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, generate_datas("district","sixth_district"))
    parties.append(factory_party('Rassemblement National', 'RN', [first_elected_person_rn, second_elected_person_rn, third_elected_person_rn]))
    return parties