from src.backend.infrastructure.models.factory_record import factory_candidate_record, factory_district_record, factory_election_record, factory_party_record

def construct_election_2022():
    districts = [__construct_district_502(), __construct_district_1502(), __construct_district_2502(), 
                     __construct_district_3502(), __construct_district_4502(), __construct_district_5502(), 
                     __construct_district_6502(), __construct_district_7502()]
    election = factory_election_record(__construct_parties(), districts)
    return election        
    
def __construct_district_502():
    first_candidate = factory_candidate_record("GUIGNARD", "Boris", "MASCULIN", "DXG", 179, 0.33, 0.63)
    second_candidate = factory_candidate_record("MOUNAL", "Capucine", "FEMININ", "NUP", 8365, 15.41, 29.22)
    third_candidate = factory_candidate_record("ROUX", "Rémi", "MASCULIN", "DVG", 1077, 1.98, 3.76)
    fourth_candidate = factory_candidate_record("PASSEREAU", "Yann", "MASCULIN", "ECO", 305, 0.56, 1.07)
    fifth_candidate = factory_candidate_record("GIRAUD", "Joel", "MASCULIN", "ENS", 10889, 20.06, 38.04)
    sixth_candidate = factory_candidate_record("CHAUVET", "Carole", "FEMININ", "LR", 1549, 2.85, 5.41)
    seventh_candidate = factory_candidate_record("BESSONNIER", "Sandrine",  "FEMININ", "DSV", 383, 0.71, 1.34)
    eighth_candidate = factory_candidate_record("PELISSIER", "Margot", "FEMININ", "REC", 883, 1.63, 3.08)
    nineth_candidate =factory_candidate_record("ALBRAND", "Louis", "MASCULIN", "RN", 4996, 9.21, 17.45)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate]
    district = factory_district_record("2ème circonscription", 2, 5, 54274, 25057, candidates)
    return district

def __construct_district_1502() : 
    first_candidate = factory_candidate_record("CHEIKHI", "Mona", "FEMININ", "DXG", 285, 0.54, 1.03)
    second_candidate = factory_candidate_record("MORILLE", "Mélody", "FEMININ", "NUP", 4534, 8.58, 16.33)
    third_candidate = factory_candidate_record("DELMOURE", "Jean-René", "MASCULIN", "ECO", 7, 0.01, 0.03)
    fourth_candidate = factory_candidate_record("GUIBERT", "Martine", "FEMININ", "ENS", 4848, 9.17, 17.46)
    fifth_candidate = factory_candidate_record("BONY", "Jean-Yves", "MASCULIN", "LR", 10472, 19.81, 37.71)
    sixth_candidate = factory_candidate_record("TOTY", "Louis", "MASCULIN", "DVD", 2967, 5.61, 10.68)
    seventh_candidate = factory_candidate_record("CHEYROL", "Antoine", "MASCULIN", "REC", 796, 1.51, 2.87)
    eighth_candidate = factory_candidate_record("LACROIX", "Gilles", "MASCULIN", "RN", 3861, 7.3, 13.9)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate]
    district = factory_district_record("2ème circonscription", 2, 15, 52867, 24448, candidates)
    return district

def __construct_district_2502():
    first_candidate = factory_candidate_record("VUITTON", "Brigitte", "FEMININ", "DXG", 779, 0.98, 1.93)
    second_candidate = factory_candidate_record("RAVACLEY", "Stéphane", "MASCULIN", "NUP", 13112, 16.56, 32.51)
    third_candidate = factory_candidate_record("THOMASSIN", "Geoffrey", "MASCULIN", "DIV", 216, 0.27, 0.54)
    fourth_candidate = factory_candidate_record("MEYER", "Claudine", "FEMININ", "REG", 0, 0.0, 0.0)
    fifth_candidate = factory_candidate_record("ALAUZET", "Eric", "MASCULIN", "ENS", 12647, 15.98, 31.36)
    sixth_candidate = factory_candidate_record("KAOULAL", "Chafia", "FEMININ", "LR", 4354, 5.5, 10.8)
    seventh_candidate = factory_candidate_record("PRENEL", "Jim",  "MASCULIN", "DSV", 692, 0.87, 1.72)
    eighth_candidate = factory_candidate_record("CARRAU", "Barbara", "FEMININ", "REC", 1472, 1.84, 3.65)
    nineth_candidate =factory_candidate_record("FUSIS", "Eric", "MASCULIN", "RN", 7055, 8.91, 17.49)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate]
    district = factory_district_record("2ème circonscription", 2, 25, 79162, 37688, candidates)
    return district

def __construct_district_3502():
    first_candidate = factory_candidate_record("DEFRANCE", "Florence", "FEMININ", "DXG", 619, 0.63, 1.13)
    second_candidate = factory_candidate_record("LAHAIS", "Tristan", "MASCULIN", "NUP", 21596, 21.98, 39.51)
    third_candidate = factory_candidate_record("MARION", "Victor", "MASCULIN", "ECO", 676, 0.69, 1.24)
    fourth_candidate = factory_candidate_record("BEN LAHCEN", "Sofia", "FEMININ", "DIV", 84, 0.09, 0.15)
    fifth_candidate = factory_candidate_record("LAHOGUE", "Mathilde", "FEMININ", "REG", 1154, 1.17, 2.11)
    sixth_candidate = factory_candidate_record("EGRON", "Maël", "MASCULIN", "REG", 375, 0.38, 0.69)
    seventh_candidate = factory_candidate_record("MAILLART-MÉHAIGNERIE", "Laurence",  "FEMININ", "ENS", 22630, 23.03, 41.41)
    eighth_candidate = factory_candidate_record("JAMBU", "Marc-Antoine", "MASCULIN", "DSV", 718, 0.73, 1.31)
    nineth_candidate =factory_candidate_record("CHAROTE", "Jean-Pierre", "MASCULIN", "REC", 2204, 2.24, 4.03)
    tenth_candidate = factory_candidate_record("CADIOU", "Stéphanie", "FEMININ", "RN", 4598, 4.68, 8.41)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate]
    district = factory_district_record("2ème circonscription", 2, 35, 98259, 42410, candidates)
    return district

def __construct_district_4502():
    first_candidate = factory_candidate_record("MEGDOUD", "Farida", "FEMININ", "DXG", 496, 0.57, 1.21)
    second_candidate = factory_candidate_record("DUPLESSY", "Emmanuel", "MASCULIN", "NUP", 10338, 11.84, 25.12)
    third_candidate = factory_candidate_record("CHAILLOU", "Yann", "MASCULIN", "DVG", 1720, 1.97, 4.18)
    fourth_candidate = factory_candidate_record("BOYER", "Anaïs", "FEMININ", "ECO", 737, 0.84, 1.79)
    fifth_candidate = factory_candidate_record("BERTRAN", "Sarah", "FEMININ", "DIV", 868, 0.99, 2.11)
    sixth_candidate = factory_candidate_record("EGRON", "Maël", "MASCULIN", "REG", 375, 0.38, 0.69)
    seventh_candidate = factory_candidate_record("JANVIER", "Caroline",  "FEMININ", "ENS", 11978, 13.72, 29.1)
    eighth_candidate = factory_candidate_record("HOUSSARD", "Alexandre", "MASCULIN", "LR", 4811, 5.51, 11.69)
    nineth_candidate =factory_candidate_record("MALLET", "Jean-Paul", "MASCULIN", "REC", 2043, 2.34, 4.96)
    tenth_candidate = factory_candidate_record("BABIN", "Élodie", "FEMININ", "RN", 7911, 9.06, 19.22)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate]
    district = factory_district_record("2ème circonscription", 2, 45, 87280, 45283, candidates)
    return district

def __construct_district_5502():
    first_candidate = factory_candidate_record("NORDEMANN", "Pierre", "MASCULIN", "DXG", 247, 0.41, 0.93)
    second_candidate = factory_candidate_record("LAFLOTTE", "Johan", "MASCULIN", "NUP", 4318, 7.25, 16.23)
    third_candidate = factory_candidate_record("HAROS", "Pascal", "MASCULIN", "DVG", 1822, 3.06, 6.85)
    fourth_candidate = factory_candidate_record("DHYVERT", "Yves", "MASCULIN", "ECO", 778, 1.31, 2.92)
    fifth_candidate = factory_candidate_record("TESTI", "Michel", "MASCULIN", "ECO", 368, 0.62, 1.38)
    sixth_candidate = factory_candidate_record("BOIS", "Anne", "FEMININ", "ENS", 5101, 8.57, 19.17)
    seventh_candidate = factory_candidate_record("GALLIC", "Martin",  "MASCULIN", "DVC", 658, 1.11, 2.47)
    eighth_candidate = factory_candidate_record("DURET", "Jean-Luc", "MASCULIN", "DVC", 1, 0.0, 0.0)
    nineth_candidate =factory_candidate_record("ADDENET", "Jean-Marie", "MASCULIN", "LR", 3588, 6.03, 13.49)
    tenth_candidate = factory_candidate_record("BEDEL", "Nicolas", "MASCULIN", "DSV", 353, 0.59, 1.33)
    eleventh_candidate = factory_candidate_record("MENNESON", "Michel", "MASCULIN", "REC", 676, 1.14, 2.54)
    twelth_candidate = factory_candidate_record("GOULET", "Florence", "FEMININ", "RN", 8693, 14.61, 32.68)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate, eleventh_candidate,
                  twelth_candidate]
    district = factory_district_record("2ème circonscription", 2, 55, 59520, 32306, candidates)
    return district

def __construct_district_6502():
    first_candidate = factory_candidate_record("MEUNIER", "François", "MASCULIN", "DXG", 438, 0.49, 0.96)
    second_candidate = factory_candidate_record("CRAMPE", "Jérome", "MASCULIN", "RDG", 6555, 7.3, 14.32)
    third_candidate = factory_candidate_record("KORN", "Grégory", "MASCULIN", "NUP", 10504, 11.7, 22.95)
    fourth_candidate = factory_candidate_record("CASTÉRA", "Yves", "MASCULIN", "DVG", 896, 1.0, 1.96)
    fifth_candidate = factory_candidate_record("RIGOLLET", "Antoine", "MASCULIN", "ECO", 598, 0.67, 1.31)
    sixth_candidate = factory_candidate_record("DABAT", "Jean-Marc", "MASCULIN", "DIV", 1973, 2.2, 4.31)
    seventh_candidate = factory_candidate_record("BEAUDRY", "Delphine",  "FEMININ", "REG", 465, 0.52, 1.02)
    eighth_candidate = factory_candidate_record("MOURNET", "Benoit", "MASCULIN", "ENS", 10870, 12.11, 23.75)
    nineth_candidate =factory_candidate_record("DUTREY", "Véronique", "FEMININ", "LR", 2770, 3.09, 6.05)
    tenth_candidate = factory_candidate_record("BARBE", "Aline", "FEMININ", "DSV", 547, 0.61, 1.2)
    eleventh_candidate = factory_candidate_record("ALVES DA CUNHA", "Claude", "MASCULIN", "REC", 1667, 1.86, 3.64)
    twelth_candidate = factory_candidate_record("DUMANOIR", "Serge", "MASCULIN", "RN", 8483, 9.45, 18.54)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate, eleventh_candidate,
                  twelth_candidate]
    district = factory_district_record("2ème circonscription", 2, 65, 89775, 42742, candidates)
    return district

def __construct_district_7502():
    first_candidate = factory_candidate_record("JOLIVEAU", "Charline", "FEMININ", "DXG", 146, 0.2, 0.33)
    second_candidate = factory_candidate_record("FRANTZ", "Adrien", "MASCULIN", "DXG", 102, 0.14, 0.23)
    third_candidate = factory_candidate_record("ROSSET", "Marine", "FEMININ", "NUP", 11890, 15.9, 27.27)
    fourth_candidate = factory_candidate_record("CASTÉRA", "Yves", "MASCULIN", "DVG", 896, 1.0, 1.96)
    fifth_candidate = factory_candidate_record("DREYFUSS", "Karine", "FEMININ", "ECO", 682, 0.91, 1.56)
    sixth_candidate = factory_candidate_record("ASSAYAG", "Daniel", "MASCULIN", "DIV", 248, 0.33, 0.57)
    seventh_candidate = factory_candidate_record("DE VILLEPIN", "Quitterie",  "FEMININ", "DIV", 2362, 3.16, 5.42)
    eighth_candidate = factory_candidate_record("MAGNE", "Elise", "FEMININ", "DIV", 550, 0.74, 1.26)
    nineth_candidate =factory_candidate_record("DUTREY", "Véronique", "FEMININ", "LR", 2770, 3.09, 6.05)
    tenth_candidate = factory_candidate_record("LE GENDRE", "Gilles", "MASCULIN", "ENS", 15547, 20.79, 35.66)
    eleventh_candidate = factory_candidate_record("LECOQ", "Jean-Pierre", "MASCULIN", "LR", 7948, 10.63, 18.23)
    twelth_candidate = factory_candidate_record("GILBERT", "Isabelle", "FEMININ", "REC", 2827, 3.78, 6.48)
    thirteenth_candidate = factory_candidate_record("ROUGÉ", "André", "MASCULIN", "RN", 1294, 1.73, 2.97)
    candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                  seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate, eleventh_candidate,
                  twelth_candidate, thirteenth_candidate]
    district = factory_district_record("2ème circonscription", 2, 75, 74767, 30690, candidates)
    return district

def __construct_parties(): 
    parties = []
    parties.append(factory_party_record('Divers extrême gauche','DXG'))
    parties.append(factory_party_record('Parti radical de gauche','RDG'))
    parties.append(factory_party_record('Nouvelle union populaire écologique et sociale','NUP'))
    parties.append(factory_party_record('Divers gauche','DVG'))
    parties.append(factory_party_record('Ecologistes','ECO'))
    parties.append(factory_party_record('Divers','DIV'))
    parties.append(factory_party_record('Régionaliste','REG'))
    parties.append(factory_party_record('Ensemble ! (Majorité présidentielle)','ENS'))
    parties.append(factory_party_record('Divers centre','DVC'))
    parties.append(factory_party_record('Union des Démocrates et des Indépendants','UDI'))
    parties.append(factory_party_record('Les Républicains','LR'))
    parties.append(factory_party_record('Divers droite','DVD'))
    parties.append(factory_party_record('Droite souverainiste','DSV'))
    parties.append(factory_party_record('Reconquête !','REC'))
    parties.append(factory_party_record('Rassemblement National','RN'))
    parties.append(factory_party_record( 'Divers extrême droite','DXD'))
    return parties