from src.backend.domain.factory import factory_congress_person, factory_district

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
    candidate = factory_congress_person("GUIGNARD", "Boris", 394, 1.02, __build_first_district())
    return candidate

def __build_second_candidate_first_district():
    candidate = factory_congress_person("FINE", "MASCULIN", 10338, 26.70, __build_first_district())
    return candidate

def __build_third_candidate_first_district():
    candidate = factory_congress_person("ROSSI", "Valérie", 12661, 32.70, __build_first_district())
    return candidate

def __build_fourth_candidate_first_district():
    candidate = factory_congress_person("MONDAIN", "Johann", 2260, 5.70, __build_first_district())
    return candidate

def __build_fifth_candidate_first_district():
    candidate = factory_congress_person("ALBRAND", "Louis", 13115, 33.88, __build_first_district())
    return candidate

def __build_first_district():
    district = factory_district("2ème circonscription", 502, "Hautes-Alpes", 5)
    return district

def get_candidates_from_second_district_choosen():
    candidates = [__build_first_candidate_second_district(), __build_second_candidate_second_district(), 
                  __build_third_candidate_second_district(), __build_fourth_candidate_second_district(), 
                  __build_fifth_candidate_second_district(), __build_sixth_candidate_second_district(),
                  __build_seventh_candidate_second_district()]
    return candidates

def __build_first_candidate_second_district():
    candidate = factory_congress_person("CHEIKHI", "Mona", 298, 0.83, __build_second_district())
    return candidate

def __build_second_candidate_second_district():
    candidate = factory_congress_person("PÉBAY", "Zoé", 4919, 13.62, __build_second_district())
    return candidate

def __build_third_candidate_second_district():
    candidate = factory_congress_person("LACROIX", "Gilles", 11923, 33.02, __build_second_district())
    return candidate

def __build_fourth_candidate_second_district():
    candidate = factory_congress_person("VEYSSET-RAPAPORT", "Pascal", 220, 0.61, __build_second_district())
    return candidate

def __build_fifth_candidate_second_district():
    candidate = factory_congress_person("TILMANT-TATISCHEFF", "Vladimir", 3019, 8.36, __build_second_district())
    return candidate

def __build_sixth_candidate_second_district():
    candidate = factory_congress_person("TOTY", "Louis", 3348, 9.27, __build_second_district())
    return candidate

def __build_seventh_candidate_second_district():
    candidate = factory_congress_person("BONY", "Jean Yves", 12383, 34.29, __build_second_district())
    return candidate

def __build_second_district():
    district = factory_district("2ème circonscription", 1502, "Cantal", 15)
    return district

def get_candidates_from_third_district_choosen():
    candidates = [__build_first_candidate_third_district(), __build_second_candidate_third_district(), 
                  __build_third_candidate_third_district(), __build_fourth_candidate_third_district(), 
                  __build_fifth_candidate_third_district()]
    return candidates

def __build_first_candidate_third_district():
    candidate = factory_congress_person("VOYNET", "Dominique", 19160, 34.16, __build_third_district())
    return candidate

def __build_second_candidate_third_district():
    candidate = factory_congress_person("VUITTON", "Brigitte", 788, 1.41, __build_third_district())
    return candidate

def __build_third_candidate_third_district():
    candidate = factory_congress_person("FUSIS", "Eric", 16895, 30.12, __build_third_district())
    return candidate

def __build_fourth_candidate_third_district():
    candidate = factory_congress_person("VUILLEMIN", "Benoît", 15026, 26.79, __build_third_district())
    return candidate

def __build_fifth_candidate_third_district():
    candidate = factory_congress_person("ROY", "Daniel", 4215, 7.52, __build_third_district())
    return candidate

def __build_third_district():
    district = factory_district("2ème circonscription", 2502, "Doubs", 25)
    return district

def get_candidates_from_fourth_district_choosen():
    candidates = [__build_first_candidate_fourth_district(), __build_second_candidate_fourth_district(), 
                  __build_third_candidate_fourth_district(), __build_fourth_candidate_fourth_district(), 
                  __build_fifth_candidate_fourth_district(), __build_sixth_candidate_fourth_district()]
    return candidates

def __build_first_candidate_fourth_district():
    candidate = factory_congress_person("DEFRANCE", "Florence", 746, 0.99, __build_fourth_district())
    return candidate

def __build_second_candidate_fourth_district():
    candidate = factory_congress_person("DECOURCELLE", "Christophe", 5218, 6.93, __build_fourth_district())
    return candidate

def __build_third_candidate_fourth_district():
    candidate = factory_congress_person("MAILLART-MÉHAIGNERIE", "Laurence", 25792, 34.24, __build_fourth_district())
    return candidate

def __build_fourth_candidate_fourth_district():
    candidate = factory_congress_person("VANHAECKE", "Bérénice", 13130, 17.43, __build_fourth_district())
    return candidate

def __build_fifth_candidate_fourth_district():
    candidate = factory_congress_person("LAHAIS", "Tristan", 30361, 40.31, __build_fourth_district())
    return candidate

def __build_sixth_candidate_fourth_district():
    candidate = factory_congress_person("HANNE", "Olivier", 71, 0.09, __build_fourth_district())
    return candidate

def __build_fourth_district():
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
    candidate = factory_congress_person("COLAS", "Cyril", 4527, 5.11, __build_fifth_district())
    return candidate 
 
def __build_second_candidate_fifth_district():
    candidate = factory_congress_person("JANVIER", "Caroline", 13263, 23.03, __build_fifth_district())
    return candidate

def __build_third_candidate_fifth_district():
    candidate = factory_congress_person("MEGDOUD", "Farida", 388, 0.44, __build_fifth_district())
    return candidate

def __build_fourth_candidate_fifth_district():
    candidate = factory_congress_person("CARRANI", "Bruno", 1474, 2.56, __build_fifth_district())
    return candidate

def __build_fifth_candidate_fifth_district():
    candidate = factory_congress_person("DUPLESSY", "Emmanuel", 16148, 28.03, __build_fifth_district())
    return candidate

def __build_sixth_candidate_fifth_district():
    candidate = factory_congress_person("CHAILLOU", "Yann", 1951, 3.39, __build_fifth_district())
    return candidate

def __build_seventh_candidate_fifth_district():
    candidate = factory_congress_person("BABIN", "Elodie", 18957, 32.91, __build_fifth_district())
    return candidate

def __build_eighth_candidate_fifth_district():
    candidate = factory_congress_person("DUVILLARD", "Marie-Odile", 716, 1.24, __build_fifth_district())
    return candidate

def __build_nineth_candidate_fifth_district():
    candidate = factory_congress_person("AACHBOUN", "Ahmed", 178, 0.31, __build_fifth_district())
    return candidate 

def __build_fifth_district():
    district = factory_district("2ème circonscription", 4502, "Loiret", 45)
    return district

def get_candidates_from_sixth_district_choosen():
    candidates = [__build_first_candidate_sixth_district(), __build_second_candidate_sixth_district(), 
                  __build_third_candidate_sixth_district(), __build_fourth_candidate_sixth_district(), 
                  __build_fifth_candidate_sixth_district()]
    return candidates

def __build_first_candidate_sixth_district():
    candidate = factory_congress_person("GOULET", "Florence", 19011, 50.63, __build_sixth_district())
    return candidate

def __build_second_candidate_sixth_district():
    candidate = factory_congress_person("NORDEMANN", "Pierre", 431, 1.15, __build_sixth_district())
    return candidate

def __build_third_candidate_sixth_district():
    candidate = factory_congress_person("LAFLOTTE", "Johan", 5391, 14.36, __build_sixth_district())
    return candidate

def __build_fourth_candidate_sixth_district():
    candidate = factory_congress_person("LAFUE", "Valentine", 742, 1.98, __build_sixth_district())
    return candidate

def __build_fifth_candidate_sixth_district():
    candidate = factory_congress_person("DUMONT", "Jerome", 11976, 31.89, __build_sixth_district())
    return candidate

def __build_sixth_district():
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
    candidate = factory_congress_person("JOLIVEAU", "Charline", 168, 0.30, __build_seventh_district())
    return candidate

def __build_second_candidate_seventh_district():
    candidate = factory_congress_person("DE WITTE", "Melody", 6206, 11.00, __build_seventh_district())
    return candidate

def __build_third_candidate_seventh_district():
    candidate = factory_congress_person("SACASA", "Clara", 0, 0.00, __build_seventh_district())
    return candidate

def __build_fourth_candidate_seventh_district():
    candidate = factory_congress_person("HERZOG DE COSSÉ BRISSAC", "Félicité", 3792, 6.72, __build_seventh_district())
    return candidate

def __build_fifth_candidate_seventh_district():
    candidate = factory_congress_person("LE GENDRE", "Gilles", 11071, 19.62, __build_seventh_district())
    return candidate

def __build_sixth_candidate_seventh_district():
    candidate = factory_congress_person("EVANGELISTA", "Ornella", 778, 1.38, __build_seventh_district())
    return candidate

def __build_seventh_candidate_seventh_district():
    candidate = factory_congress_person("LAUSSUCQ", "Jean", 13325, 23.62, __build_seventh_district())
    return candidate

def __build_eighth_candidate_seventh_district():
    candidate = factory_congress_person("LORANS", "Cécile Marie", 512, 0.91, __build_seventh_district())
    return candidate

def __build_nineth_candidate_seventh_district():
    candidate = factory_congress_person("MARSILY", "Romain", 1229, 2.18, __build_seventh_district())
    return candidate

def __build_tenth_candidate_seventh_district():
    candidate = factory_congress_person("MAURIANGE", "Frédéric", 430, 0.76, __build_seventh_district())
    return candidate

def __build_eleventh_candidate_seventh_district():
    candidate = factory_congress_person("MAGNE", "Elise", 60, 0.11, __build_seventh_district())
    return candidate

def __build_twelveth_candidate_seventh_district():
    candidate = factory_congress_person("ROSSET", "Marine", 18845, 33.40, __build_seventh_district())
    return candidate

def __build_seventh_district():
    district = factory_district("2ème circonscription", 7502, "Paris", 75)
    return district