from src.backend.domain.models.factory import factory_congress_person
from tests.utils.data.generateDataDistricts import build_first_district, build_second_district, build_third_district, build_fourth_district, build_fifth_district, build_sixth_district, build_seventh_district


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