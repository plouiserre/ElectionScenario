from src.backend.infrastructure.models.factory_record import factory_candidate_record, factory_district_record, factory_election_record, factory_party_record

def construct_election_2024(): 
        districts = [__construct_district_502(), __construct_district_1502(), __construct_district_2502(), 
                     __construct_district_3502(), __construct_district_4502(), __construct_district_5502(), 
                     __construct_district_6502(), __construct_district_7502()]
        election = factory_election_record(__construct_parties(), districts)
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
    seventh_candidate = factory_candidate_record("LAUSSUCQ", "Jean", "MASCULIN", "ENS", 13325, 17.87, 23.62)
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

def __construct_parties():
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