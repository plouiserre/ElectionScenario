from src.backend.domain.factory import factory_congress_person, factory_district

def get_candidates_from_one_district():
    candidates = [__build_first_candidate(), __build_second_candidate(), __build_third_candidate(), __build_fourth_candidate(), 
                  __build_fifth_candidate(), __build_sixth_candidate(), __build_seventh_candidate(), __build_eighth_candidate(), 
                  __build_nineth_candidate(), __build_tenth_candidate(), __build_eleventh_candidate(), __build_twelveth_candidate()]
    return candidates

def __build_first_candidate():
    candidate = factory_congress_person("JOLIVEAU", "Charline", 168, 0.30, __build_first_district())
    return candidate

def __build_second_candidate():
    candidate = factory_congress_person("DE WITTE", "Melody", 6206, 11.00, __build_first_district())
    return candidate

def __build_third_candidate():
    candidate = factory_congress_person("SACASA", "Clara", 0, 0.00, __build_first_district())
    return candidate

def __build_fourth_candidate():
    candidate = factory_congress_person("HERZOG DE COSSÉ BRISSAC", "Félicité", 3792, 6.72, __build_first_district())
    return candidate

def __build_fifth_candidate():
    candidate = factory_congress_person("LE GENDRE", "Gilles", 11071, 19.62, __build_first_district())
    return candidate

def __build_sixth_candidate():
    candidate = factory_congress_person("EVANGELISTA", "Ornella", 778, 1.38, __build_first_district())
    return candidate

def __build_seventh_candidate():
    candidate = factory_congress_person("LAUSSUCQ", "Jean", 13325, 23.62, __build_first_district())
    return candidate

def __build_eighth_candidate():
    candidate = factory_congress_person("LORANS", "Cécile Marie", 512, 0.91, __build_first_district())
    return candidate

def __build_nineth_candidate():
    candidate = factory_congress_person("MARSILY", "Romain", 1229, 2.18, __build_first_district())
    return candidate

def __build_tenth_candidate():
    candidate = factory_congress_person("MAURIANGE", "Frédéric", 430, 0.76, __build_first_district())
    return candidate

def __build_eleventh_candidate():
    candidate = factory_congress_person("MAGNE", "Elise", 60, 0.11, __build_first_district())
    return candidate

def __build_twelveth_candidate():
    candidate = factory_congress_person("ROSSET", "Marine", 18845, 33.40, __build_first_district())
    return candidate

def __build_first_district():
    district = factory_district("2ème circonscription", 7502, "Paris", 75)
    return district