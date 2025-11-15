from src.backend.domain.models.factory import factory_congress_person
from tests.utils.data.catalogData import generate_datas


def load_all_candidates():
    all_candidates = [__load_all_candidates_from_five_hundred_second_district(), __load_all_candidates_from_fifteen_hundred_second_district(),
                      __load_all_candidates_from_twenty_fifth_hundred_second_district(), 
                      __load_all_candidates_from_thirty_fifth_hundred_second_district(), 
                      __load_all_candidates_from_fourty_fifth_hundred_second_district(), 
                      __load_all_candidates_from_fifty_fifth_hundred_second_district(), 
                      __load_all_candidates_from_sixty_hundred_second_district(), __load_all_candidates_from_seventy_hundred_second_district()]
    return all_candidates

def __load_all_candidates_from_five_hundred_second_district():
    first_candidate = factory_congress_person("GUIGNARD", "Boris", "MASCULIN", "DXG", 394, 1.02, generate_datas("district","first_district", ""))
    second_candidate = factory_congress_person("FINE", "Sébastien", "MASCULIN", "ENS", 10338, 26.70, generate_datas("district","first_district", ""))
    third_candidate = factory_congress_person("ROSSI", "Valérie", "FEMININ", "UG", 12661, 32.70, generate_datas("district","first_district", ""))
    fourth_candidate = factory_congress_person("MONDAIN", "Johann", "MASCULIN", "DIV", 2260, 5.70, generate_datas("district","first_district", ""))
    fifth_candidate = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, generate_datas("district","first_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    return candidates


def __load_all_candidates_from_fifteen_hundred_second_district():    
    first_candidate = factory_congress_person("GUIGNARD", "Boris", "MASCULIN", "DXG", 394, 1.02, generate_datas("district","first_district", ""))
    second_candidate = factory_congress_person("FINE", "Sébastien", "MASCULIN", "ENS", 10338, 26.70, generate_datas("district","first_district", ""))
    third_candidate = factory_congress_person("ROSSI", "Valérie", "FEMININ", "UG", 12661, 32.70, generate_datas("district","first_district", ""))
    fourth_candidate = factory_congress_person("MONDAIN", "Johann", "MASCULIN", "DIV", 2260, 5.70, generate_datas("district","first_district", ""))
    fifth_candidate = factory_congress_person("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 33.88, generate_datas("district","first_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    return candidates

def __load_all_candidates_from_twenty_fifth_hundred_second_district():
    first_candidate = factory_congress_person("CHEIKHI", "Mona", "FEMININ", "EXG", 298, 0.83, generate_datas("district","second_district", ""))
    second_candidate = factory_congress_person("PÉBAY", "Zoé", "FEMININ", "UG", 4919, 13.62, generate_datas("district","second_district", ""))
    third_candidate = factory_congress_person("LACROIX", "Gilles", "MASCULIN", "RN", 11923, 33.02, generate_datas("district","second_district", ""))
    fourth_candidate = factory_congress_person("VEYSSET-RAPAPORT", "Pascal", "MASCULIN", "REC", 220, 0.61, generate_datas("district","second_district", ""))
    fifth_candidate = factory_congress_person("TILMANT-TATISCHEFF", "Vladimir", "MASCULIN", "ENS", 3019, 8.36, generate_datas("district","second_district", ""))
    six_candidate = factory_congress_person("TOTY", "Louis", "MASCULIN", "DVD", 3348, 9.27, generate_datas("district","second_district", ""))
    seventh_candidate = factory_congress_person("BONY", "Jean-Yves", "MASCULIN", "LR", 12383, 34.29, generate_datas("district","second_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, six_candidate, seventh_candidate]
    return candidates

def __load_all_candidates_from_thirty_fifth_hundred_second_district():
    first_candidate = factory_congress_person("VOYNET", "Dominique", "FEMININ", "UG", 19160, 34.16, generate_datas("district","third_district", ""))
    second_candidate = factory_congress_person("VUITTON", "Brigitte", "FEMININ", "EXG", 788, 1.41, generate_datas("district","third_district", ""))
    third_candidate = factory_congress_person("FUSIS", "Eric", "MASCULIN", "RN", 16895, 30.12, generate_datas("district","third_district", ""))
    fourth_candidate = factory_congress_person("VUILLEMIN", "Benoît", "MASCULIN", "ENS", 15026, 26.79, generate_datas("district","third_district", ""))
    fifth_candidate = factory_congress_person("ROY", "Daniel", "MASCULIN", "LR", 4215, 7.52, generate_datas("district","third_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    return candidates

def __load_all_candidates_from_fourty_fifth_hundred_second_district():
    first_candidate = factory_congress_person("DEFRANCE", "Florence", "FEMININ", "EXG", 746, 0.99, generate_datas("district","fourth_district", ""))
    second_candidate = factory_congress_person("DECOURCELLE", "Christophe", "MASCULIN", "LR", 5218, 6.93, generate_datas("district","fourth_district", ""))
    third_candidate = factory_congress_person("MAILLART-MÉHAIGNERIE", "Laurence", "FEMININ", "ENS", 25792, 34.24, generate_datas("district","fourth_district", ""))
    fourth_candidate = factory_congress_person("VANHAECKE", "Bérénice", "FEMININ", "RN", 13130, 17.43, generate_datas("district","fourth_district", ""))
    fifth_candidate = factory_congress_person("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 40.31, generate_datas("district","fourth_district", ""))
    sixth_candidate = factory_congress_person("HANNE", "Olivier", "MASCULIN", "ECO", 71, 0.09, generate_datas("district","fourth_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
    return candidates

def __load_all_candidates_from_fifty_fifth_hundred_second_district():
    first_candidate = factory_congress_person("COLAS", "Cyril", "MASCULIN", "LR", 4527, 5.11, generate_datas("district","fifth_district", ""))
    second_candidate = factory_congress_person("JANVIER", "Caroline", "FEMININ", "ENS", 13263, 23.03, generate_datas("district","fifth_district", ""))
    third_candidate = factory_congress_person("MEGDOUD", "Farida", "FEMININ", "EXG", 388, 0.44, generate_datas("district","fifth_district", ""))
    fourth_candidate = factory_congress_person("CARRANI", "Bruno", "MASCULIN", "ECO", 1474, 2.56, generate_datas("district","fifth_district", ""))
    fifth_candidate = factory_congress_person("DUPLESSY", "Emmanuel", "MASCULIN", "UG", 16148, 28.03, generate_datas("district","fifth_district", ""))
    sixth_candidate = factory_congress_person("CHAILLOU", "Yann", "MASCULIN", "DVG", 1951, 3.39, generate_datas("district","fifth_district", ""))
    seventh_candidate = factory_congress_person("BABIN", "Elodie", "FEMININ", "RN", 18957, 32.91, generate_datas("district","fifth_district", ""))
    eighth_candidate = factory_congress_person("DUVILLARD", "Marie-Odile", "FEMININ", "REC", 716, 1.24, generate_datas("district","fifth_district", ""))
    nineth_candidate = factory_congress_person("AACHBOUN", "Ahmed", "MASCULIN", "DVG", 178, 0.31, generate_datas("district","fifth_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, seventh_candidate,
                  eighth_candidate, nineth_candidate]
    return candidates

def __load_all_candidates_from_sixty_hundred_second_district():
    first_candidate = factory_congress_person("GOULET", "Florence", "FEMININ", "RN", 19011, 50.63, generate_datas("district","sixth_district", ""))
    second_candidate = factory_congress_person("NORDEMANN", "Pierre", "MASCULIN", "EXG", 431, 1.15, generate_datas("district","sixth_district", ""))
    third_candidate = factory_congress_person("LAFLOTTE", "Johan", "MASCULIN", "UG", 5391, 14.36, generate_datas("district","sixth_district", ""))
    fourth_candidate = factory_congress_person("LAFUE", "Valentine", "FEMININ", "ECO", 742, 1.98, generate_datas("district","sixth_district", ""))
    fifth_candidate = factory_congress_person("DUMONT", "Jerome", "MASCULIN", "DVD", 11976, 31.89, generate_datas("district","sixth_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
    return candidates

def __load_all_candidates_from_seventy_hundred_second_district():
    first_candidate = factory_congress_person("JOLIVEAU", "Charline", "FEMININ", "EXG", 168, 0.30, generate_datas("district","seventh_district", ""))
    second_candidate = factory_congress_person("DE WITTE", "Melody", "FEMININ", "RN", 6206, 11.00, generate_datas("district","seventh_district", ""))
    third_candidate = factory_congress_person("SACASA", "Clara", "FEMININ", "EXG", 0, 0.00, generate_datas("district","seventh_district", ""))
    fourth_candidate = factory_congress_person("HERZOG DE COSSÉ BRISSAC", "Félicité", "FEMININ", "DVD", 3792, 6.72, generate_datas("district","seventh_district", ""))
    fifth_candidate = factory_congress_person("LE GENDRE", "Gilles", "MASCULIN", "DVC", 11071, 19.62, generate_datas("district","seventh_district", ""))
    sixth_candidate = factory_congress_person("EVANGELISTA", "Ornella", "FEMININ", "REC",  778, 1.38, generate_datas("district","seventh_district", ""))
    seventh_candidate = factory_congress_person("LAUSSUCQ", "Jean", "MASCULIN", "ENS", 13325, 23.62, generate_datas("district","seventh_district", ""))
    eighth_candidate = factory_congress_person("LORANS", "Cécile Marie", "FEMININ", "ECO", 512, 0.91, generate_datas("district","seventh_district", ""))
    nineth_candidate = factory_congress_person("MARSILY", "Romain", "MASCULIN", "DVD", 1229, 2.18, generate_datas("district","seventh_district", ""))
    tenth_candidate = factory_congress_person("MAURIANGE", "Frédéric","MASCULIN", "DVC", 430, 0.76, generate_datas("district","seventh_district", ""))
    eleventh_candidate = factory_congress_person("MAGNE", "Elise", "FEMININ", "DVG", 60, 0.11, generate_datas("district","seventh_district", ""))
    twelveth_candidate = factory_congress_person("ROSSET", "Marine", "FEMININ", "UG",18845, 33.40, generate_datas("district","seventh_district", ""))
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate,
                  seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate, eleventh_candidate,
                  twelveth_candidate]
    return candidates

