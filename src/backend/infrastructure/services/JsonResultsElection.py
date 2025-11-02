from src.backend.domain.ports.outside.ResultsElectionsPort import ResultsElectionsPort
from src.backend.infrastructure.models.factory_record import factory_candidate, factory_district, factory_election, factory_elections_result

class JsonResultsElection(ResultsElectionsPort):
    def __init__(self):
        super().__init__()

    def get_results(self):
        results = None
        #json = "{\"elections_results\":{\"elecions\":[{\"year\":2024,\"districts\":[{\"label\":\"2ème circonscription\",\"number\":\"502\",\"department code\":\"5\",\"registered\":54517,\"voting\":39716,\"candidates\":[{\"lastName\":\"GUIGNARD\",\"firstName\":\"Boris\",\"sexe\":\"MASCULIN\",\"partiCode\":\"EXG\",\"vote\":394,\"voteByRegistered\":\"0.72%\",\"voteByExpressed\":\"1.02%\"},{\"lastName\":\"FINE\",\"firstName\":\"Sébastien\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ENS\",\"vote\":10338,\"voteByRegistered\":\"18.96%\",\"voteByExpressed\":\"26.70%\"},{\"lastName\":\"ROSSI\",\"firstName\":\"Valérie\",\"sexe\":\"FEMININ\",\"partiCode\":\"UG\",\"vote\":12661,\"voteByRegistered\":\"23.22%\",\"voteByExpressed\":\"32.70%\"},{\"lastName\":\"MONDAIN\",\"firstName\":\"Johann\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DIV\",\"vote\":2206,\"voteByRegistered\":\"4.05%\",\"voteByExpressed\":\"5.70%\"},{\"lastName\":\"ALBRAND\",\"firstName\":\"Louis\",\"sexe\":\"MASCULIN\",\"partiCode\":\"RN\",\"vote\":13115,\"voteByRegistered\":\"24.06%\",\"voteByExpressed\":\"33.88%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"1502\",\"department code\":\"15\",\"registered\":52310,\"voting\":37078,\"candidates\":[{\"lastName\":\"CHEIKHI\",\"firstName\":\"Mona\",\"sexe\":\"FEMININ\",\"partiCode\":\"EXG\",\"vote\":298,\"voteByRegistered\":\"0.57%\",\"voteByExpressed\":\"0.83%\"},{\"lastName\":\"PÉBAY\",\"firstName\":\"Zoé\",\"sexe\":\"FEMININ\",\"partiCode\":\"UG\",\"vote\":4919,\"voteByRegistered\":\"9.40%\",\"voteByExpressed\":\"13.62%\"},{\"lastName\":\"LACROIX\",\"firstName\":\"Gilles\",\"sexe\":\"MASCULIN\",\"partiCode\":\"RN\",\"vote\":11923,\"voteByRegistered\":\"22.79%\",\"voteByExpressed\":\"33.02%\"},{\"lastName\":\"VEYSSET-RAPAPORT\",\"firstName\":\"Pascal\",\"sexe\":\"MASCULIN\",\"partiCode\":\"REC\",\"vote\":220,\"voteByRegistered\":\"0.42%\",\"voteByExpressed\":\"0.61%\"},{\"lastName\":\"TILMANT-TATISCHEFF\",\"firstName\":\"Vladimir\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ENS\",\"vote\":3019,\"voteByRegistered\":\"5.77%\",\"voteByExpressed\":\"8.36%\"},{\"lastName\":\"TOTY\",\"firstName\":\"Louis\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVD\",\"vote\":3348,\"voteByRegistered\":\"6.40%\",\"voteByExpressed\":\"9.27%\"},{\"lastName\":\"BONY\",\"firstName\":\"Jean Yves\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVD\",\"vote\":12383,\"voteByRegistered\":\"23.67%\",\"voteByExpressed\":\"34.29%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"2502\",\"department code\":\"25\",\"registered\":78875,\"voting\":57350,\"candidates\":[{\"lastName\":\"VOYNET\",\"firstName\":\"Dominique\",\"sexe\":\"FEMININ\",\"partiCode\":\"UG\",\"vote\":19160,\"voteByRegistered\":\"24.29%\",\"voteByExpressed\":\"34.16%\"},{\"lastName\":\"VUITTON\",\"firstName\":\"Brigitte\",\"sexe\":\"FEMININ\",\"partiCode\":\"EXG\",\"vote\":788,\"voteByRegistered\":\"1.00%\",\"voteByExpressed\":\"1.41%\"},{\"lastName\":\"FUSIS\",\"firstName\":\"Eric\",\"sexe\":\"MASCULIN\",\"partiCode\":\"RN\",\"vote\":16895,\"voteByRegistered\":\"21.42%\",\"voteByExpressed\":\"30.12%\"},{\"lastName\":\"VUILLEMIN\",\"firstName\":\"Benoît\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ENS\",\"vote\":15026,\"voteByRegistered\":\"19.05%\",\"voteByExpressed\":\"26.79%\"},{\"lastName\":\"ROY\",\"firstName\":\"Daniel\",\"sexe\":\"MASCULIN\",\"partiCode\":\"LR\",\"vote\":4215,\"voteByRegistered\":\"5.34%\",\"voteByExpressed\":\"7.52%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"3502\",\"department code\":\"35\",\"registered\":99900,\"voting\":76790,\"candidates\":[{\"lastName\":\"DEFRANCE\",\"firstName\":\"Florence\",\"sexe\":\"FEMININ\",\"partiCode\":\"EXG\",\"vote\":746,\"voteByRegistered\":\"0.75%\",\"voteByExpressed\":\"0.99%\"},{\"lastName\":\"DECOURCELLE\",\"firstName\":\"Christophe\",\"sexe\":\"MASCULIN\",\"partiCode\":\"LR\",\"vote\":5218,\"voteByRegistered\":\"5.22%\",\"voteByExpressed\":\"6.93%\"},{\"lastName\":\"MAILLART-MÉHAIGNERIE\",\"firstName\":\"Laurence\",\"sexe\":\"FEMININ\",\"partiCode\":\"ENS\",\"vote\":25792,\"voteByRegistered\":\"25.82%\",\"voteByExpressed\":\"34.24%\"},{\"lastName\":\"VANHAECKE\",\"firstName\":\"Bérénice\",\"sexe\":\"FEMININ\",\"partiCode\":\"RN\",\"vote\":13130,\"voteByRegistered\":\"13.14%\",\"voteByExpressed\":\"17.43%\"},{\"lastName\":\"LAHAIS\",\"firstName\":\"Tristan\",\"sexe\":\"MASCULIN\",\"partiCode\":\"UG\",\"vote\":30361,\"voteByRegistered\":\"30.39%\",\"voteByExpressed\":\"40.31%\"},{\"lastName\":\"HANNE\",\"firstName\":\"Olivier\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ECO\",\"vote\":71,\"voteByRegistered\":\"0.07%\",\"voteByExpressed\":\"0.09%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"4502\",\"department code\":\"45\",\"registered\":88601,\"voting\":58836,\"candidates\":[{\"lastName\":\"COLAS\",\"firstName\":\"Cyril\",\"sexe\":\"MASCULIN\",\"partiCode\":\"LR\",\"vote\":4527,\"voteByRegistered\":\"5.11%\",\"voteByExpressed\":\"7.86%\"},{\"lastName\":\"JANVIER\",\"firstName\":\"Caroline\",\"sexe\":\"FEMININ\",\"partiCode\":\"ENS\",\"vote\":13263,\"voteByRegistered\":\"14.97%\",\"voteByExpressed\":\"23.03%\"},{\"lastName\":\"MEGDOUD\",\"firstName\":\"Farida\",\"sexe\":\"FEMININ\",\"partiCode\":\"EXG\",\"vote\":388,\"voteByRegistered\":\"0.44%\",\"voteByExpressed\":\"0.67%\"},{\"lastName\":\"CARRANI\",\"firstName\":\"Bruno\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ECO\",\"vote\":1474,\"voteByRegistered\":\"1.66%\",\"voteByExpressed\":\"2.56%\"},{\"lastName\":\"DUPLESSY\",\"firstName\":\"Emmanuel\",\"sexe\":\"MASCULIN\",\"partiCode\":\"UG\",\"vote\":16148,\"voteByRegistered\":\"18.23%\",\"voteByExpressed\":\"28.03%\"},{\"lastName\":\"CHAILLOU\",\"firstName\":\"Yann\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVG\",\"vote\":1951,\"voteByRegistered\":\"2.20%\",\"voteByExpressed\":\"3.39%\"},{\"lastName\":\"BABIN\",\"firstName\":\"Elodie\",\"sexe\":\"FEMININ\",\"partiCode\":\"RN\",\"vote\":18957,\"voteByRegistered\":\"21.40%\",\"voteByExpressed\":\"32.91%\"},{\"lastName\":\"DUVILLARD\",\"firstName\":\"Marie-Odile\",\"sexe\":\"FEMININ\",\"partiCode\":\"REC\",\"vote\":716,\"voteByRegistered\":\"0.81%\",\"voteByExpressed\":\"1.24%\"},{\"lastName\":\"AACHBOUN\",\"firstName\":\"Ahmed\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVG\",\"vote\":178,\"voteByRegistered\":\"0.20%\",\"voteByExpressed\":\"0.31%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"5502\",\"department code\":\"55\",\"registered\":59230,\"voting\":38599,\"candidates\":[{\"lastName\":\"GOULET\",\"firstName\":\"Florence\",\"sexe\":\"FEMININ\",\"partiCode\":\"RN\",\"vote\":19011,\"voteByRegistered\":\"32.10%\",\"voteByExpressed\":\"50.63%\"},{\"lastName\":\"NORDEMANN\",\"firstName\":\"Pierre\",\"sexe\":\"MASCULIN\",\"partiCode\":\"EXG\",\"vote\":431,\"voteByRegistered\":\"0.73%\",\"voteByExpressed\":\"1.15%\"},{\"lastName\":\"LAFLOTTE\",\"firstName\":\"Johan\",\"sexe\":\"MASCULIN\",\"partiCode\":\"UG\",\"vote\":5391,\"voteByRegistered\":\"9.10%\",\"voteByExpressed\":\"14.36%\"},{\"lastName\":\"LAFUE\",\"firstName\":\"Valentine\",\"sexe\":\"FEMININ\",\"partiCode\":\"ECO\",\"vote\":742,\"voteByRegistered\":\"1.25%\",\"voteByExpressed\":\"1.98%\"},{\"lastName\":\"DUMONT\",\"firstName\":\"Jerome\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVD\",\"vote\":11976,\"voteByRegistered\":\"20.22%\",\"voteByExpressed\":\"31.89%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"6502\",\"department code\":\"65\",\"registered\":88496,\"voting\":62793,\"candidates\":[{\"lastName\":\"MEUNIER\",\"firstName\":\"François\",\"sexe\":\"MASCULIN\",\"partiCode\":\"EXG\",\"vote\":692,\"voteByRegistered\":\"0.78%\",\"voteByExpressed\":\"1.14%\"},{\"lastName\":\"BÉHAGUE\",\"firstName\":\"Jacques\",\"sexe\":\"MASCULIN\",\"partiCode\":\"LR\",\"vote\":3184,\"voteByRegistered\":\"3.60%\",\"voteByExpressed\":\"5.24%\"},{\"lastName\":\"DABAT\",\"firstName\":\"Jean-Marc\",\"sexe\":\"MASCULIN\",\"partiCode\":\"REG\",\"vote\":1486,\"voteByRegistered\":\"1.68%\",\"voteByExpressed\":\"2.45%\"},{\"lastName\":\"MOURNET\",\"firstName\":\"Benoit\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ENS\",\"vote\":15121,\"voteByRegistered\":\"17.09%\",\"voteByExpressed\":\"24.91%\"},{\"lastName\":\"FÉGNÉ\",\"firstName\":\"Denis\",\"sexe\":\"MASCULIN\",\"partiCode\":\"UG\",\"vote\":17055,\"voteByRegistered\":\"19.27%\",\"voteByExpressed\":\"28.09%\"},{\"lastName\":\"EL MARSNI\",\"firstName\":\"Ali\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DIV\",\"vote\":0,\"voteByRegistered\":\"0.00%\",\"voteByExpressed\":\"0.00%\"},{\"lastName\":\"MONTEIL\",\"firstName\":\"Olivier\",\"sexe\":\"MASCULIN\",\"partiCode\":\"RN\",\"vote\":22436,\"voteByRegistered\":\"25.35%\",\"voteByExpressed\":\"36.96%\"},{\"lastName\":\"ALVES DA CUNHA\",\"firstName\":\"Claude\",\"sexe\":\"MASCULIN\",\"partiCode\":\"REC\",\"vote\":735,\"voteByRegistered\":\"0.83%\",\"voteByExpressed\":\"1.21%\"}]},{\"label\":\"2ème circonscription\",\"number\":\"7502\",\"department code\":\"75\",\"registered\":74579,\"voting\":56908,\"candidates\":[{\"lastName\":\"JOLIVEAU\",\"firstName\":\"Charline\",\"sexe\":\"FEMININ\",\"partiCode\":\"EXG\",\"vote\":168,\"voteByRegistered\":\"0.23%\",\"voteByExpressed\":\"0.30%\"},{\"lastName\":\"DE WITTE\",\"firstName\":\"Melody\",\"sexe\":\"FEMININ\",\"partiCode\":\"RN\",\"vote\":6206,\"voteByRegistered\":\"8.32%\",\"voteByExpressed\":\"11.00%\"},{\"lastName\":\"SACASA\",\"firstName\":\"Clara\",\"sexe\":\"FEMININ\",\"partiCode\":\"EXG\",\"vote\":0,\"voteByRegistered\":\"0.00%\",\"voteByExpressed\":\"0.00%\"},{\"lastName\":\"HERZOG DE COSSÉ BRISSAC\",\"firstName\":\"Félicité\",\"sexe\":\"FEMININ\",\"partiCode\":\"DVD\",\"vote\":3792,\"voteByRegistered\":\"5.08%\",\"voteByExpressed\":\"6.72%\"},{\"lastName\":\"LE GENDRE\",\"firstName\":\"Gilles\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVC\",\"vote\":11071,\"voteByRegistered\":\"14.84%\",\"voteByExpressed\":\"19.62%\"},{\"lastName\":\"EVANGELISTA\",\"firstName\":\"Ornella\",\"sexe\":\"FEMININ\",\"partiCode\":\"REC\",\"vote\":778,\"voteByRegistered\":\"1.04%\",\"voteByExpressed\":\"1.38%\"},{\"lastName\":\"LAUSSUCQ\",\"firstName\":\"Jean\",\"sexe\":\"MASCULIN\",\"partiCode\":\"ENS\",\"vote\":13325,\"voteByRegistered\":\"17.87%\",\"voteByExpressed\":\"23.62%\"},{\"lastName\":\"LORANS\",\"firstName\":\"Cécile Marie\",\"sexe\":\"FEMININ\",\"partiCode\":\"ECO\",\"vote\":512,\"voteByRegistered\":\"0.69%\",\"voteByExpressed\":\"0.91%\"},{\"lastName\":\"MARSILY\",\"firstName\":\"Romain\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVD\",\"vote\":1229,\"voteByRegistered\":\"1.65%\",\"voteByExpressed\":\"2.18%\"},{\"lastName\":\"MAURIANGE\",\"firstName\":\"Frédéric\",\"sexe\":\"MASCULIN\",\"partiCode\":\"DVC\",\"vote\":430,\"voteByRegistered\":\"0.58%\",\"voteByExpressed\":\"0.76%\"},{\"lastName\":\"MAGNE\",\"firstName\":\"Elise\",\"sexe\":\"FEMININ\",\"partiCode\":\"DVG\",\"vote\":60,\"voteByRegistered\":\"0.08%\",\"voteByExpressed\":\"0.11%\"},{\"lastName\":\"ROSSET\",\"firstName\":\"Marine\",\"sexe\":\"FEMININ\",\"partiCode\":\"UG\",\"vote\":18845,\"voteByRegistered\":\"25.27%\",\"voteByExpressed\":\"33.40%\"}]}]}]}}"
        elections_results = self.__construct_elections_result()
        return None
    
    def __construct_elections_result(self):
        results = factory_elections_result([self.__construct_election()])
        return results
    
    def __construct_election(self): 
        districts = [self.__construct_district_502(), self.__construct_district_1502(), self.__construct_district_2502(), 
                     self.__construct_district_3502(), self.__construct_district_4502(), self.__construct_district_5502(), 
                     self.__construct_district_6502(), self.__construct_district_7502()]
        election = factory_election(2024, districts)
        return election        
    
    def __construct_district_502(self):
        first_candidate = factory_candidate("GUIGNARD", "Boris", "MASCULIN", "EXG", 394, 0.72, 1.02)
        second_candidate = factory_candidate("FINE", "Sébastien", "MASCULIN", "ENS", 10338, 18.96, 26.70)
        third_candidate = factory_candidate("ROSSI", "Valérie", "FEMININ", "UG", 12661, 23.22, 32.7)
        fourth_candidate = factory_candidate("MONDAIN", "Johann", "MASCULIN", "DIV", 2206, 4.05, 5.70)
        fifth_candidate = factory_candidate("ALBRAND", "Louis", "MASCULIN", "RN", 13115, 24.06, 33.88)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
        district = factory_district("2ème circonscription", 502, 5, 54517, 39716, candidates)
        return district
    
    def __construct_district_1502(self):
        first_candidate = factory_candidate("CHEIKHI", "Mona", "FEMININ", "EXG", 298, 0.57, 0.83)
        second_candidate = factory_candidate("PÉBAY", "Zoé", "FEMININ", "UG", 4919, 9.40, 13.62)
        third_candidate = factory_candidate("LACROIX", "Gilles", "MASCULIN", "RN", 11923, 22.79, 33.02)
        fourth_candidate = factory_candidate("VEYSSET-RAPAPORT", "Pascal", "MASCULIN", "REC", 220, 0.42, 0.61)
        fifth_candidate = factory_candidate("TILMANT-TATISCHEFF", "Vladimir", "MASCULIN", "ENS", 3019, 5.77, 8.36)
        sixth_candidate = factory_candidate("TOTY", "Louis", "MASCULIN", "DVD", 3348, 6.4, 9.27)
        seventh_candidate = factory_candidate("BONY", "Jean Yves", "MASCULIN", "DVD", 12383, 23.67, 34.29)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, 
                      sixth_candidate, seventh_candidate]
        district = factory_district("2ème circonscription", 1502, 15, 52310, 37078, candidates)
        return district
    
    def __construct_district_2502(self):
        first_candidate = factory_candidate("VOYNET", "Dominique", "FEMININ", "UG", 19160, 24.29, 34.16)
        second_candidate = factory_candidate("VUITTON", "Brigitte", "FEMININ", "EXG", 788, 1.00, 1.41)
        third_candidate = factory_candidate("FUSIS", "Eric", "MASCULIN", "RN", 16895, 21.42, 30.12)
        fourth_candidate = factory_candidate("VUILLEMIN", "Benoît", "MASCULIN", "ENS", 15026, 19.05, 26.79)
        fifth_candidate = factory_candidate("ROY", "Daniel", "MASCULIN", "LR", 4215, 5.34, 7.52)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate]
        district = factory_district("2ème circonscription", 2502, 25, 78875, 57350, candidates)
        return district

    def __construct_district_3502(self):
        first_candidate = factory_candidate("DEFRANCE", "Florence", "FEMININ", "EXG", 746, 0.75, 0.99)
        second_candidate = factory_candidate("DECOURCELLE", "Christophe", "MASCULIN", "LR", 5218, 5.22, 6.93)
        third_candidate = factory_candidate("MAILLART-MÉHAIGNERIE", "Laurence", "FEMININ", "ENS", 25792, 25.82, 34.24)
        fourth_candidate = factory_candidate("VUILLEVANHAECKEMIN", "Bérénice", "FEMININ", "RN", 13130, 13.14, 17.43)
        fifth_candidate = factory_candidate("LAHAIS", "Tristan", "MASCULIN", "UG", 30361, 30.39, 40.31)
        sixth_candidate = factory_candidate("HANNE", "Olivier", "MASCULIN", "ECO", 71, 0.07, 0.09)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
        district = factory_district("2ème circonscription", 3502, 35, 99900, 76790, candidates)
        return district  
    

    def __construct_district_4502(self):
        first_candidate = factory_candidate("COLAS", "Cyril", "MASCULIN", "LR", 4527, 5.11, 7.86)
        second_candidate = factory_candidate("JANVIER", "Caroline", "FEMININ", "ENS", 13263, 14.97, 23.03)
        third_candidate = factory_candidate("MEGDOUD", "Farida", "FEMININ", "EXG", 388, 0.44, 0.67)
        fourth_candidate = factory_candidate("CARRANI", "Bruno", "MASCULIN", "ECO", 1474, 1.66, 2.56)
        fifth_candidate = factory_candidate("DUPLESSY", "Emmanuel", "MASCULIN", "UG", 16148, 18.23, 28.03)
        sixth_candidate = factory_candidate("CHAILLOU", "Yann", "MASCULIN", "DVG", 1951, 2.20, 3.39)
        seventh_candidate = factory_candidate("BABIN", "Elodie", "FEMININ", "RN", 18957, 21.4, 32.91)
        eighth_candidate = factory_candidate("DUVILLARD", "Marie-Odile", "FEMININ", "REC", 716, 0.81, 1.24)
        nineth_candidate = factory_candidate("AACHBOUN", "Ahmed", "MASCULIN", "DVG", 178, 0.2, 0.31)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                      seventh_candidate, eighth_candidate, nineth_candidate]
        district = factory_district("2ème circonscription", 4502, 45, 88601, 58836, candidates)
        return district

    def __construct_district_5502(self):
        first_candidate = factory_candidate("GOULET", "Florence", "FEMININ", "RN", 19011, 32.10, 50.63)
        second_candidate = factory_candidate("NORDEMANN", "Pierre", "MASCULIN", "ENS", 13263, 14.97, 23.03)
        third_candidate = factory_candidate("MEGDOUD", "Farida", "FEMININ", "EXG", 431, 0.73, 1.15)
        fourth_candidate = factory_candidate("LAFLOTTE", "Johan", "MASCULIN", "UG", 5391, 9.10, 14.36)
        fifth_candidate = factory_candidate("LAFUE", "Valentine", "FEMININ", "ECO", 742, 1.25, 1.98)
        sixth_candidate = factory_candidate("DUMONT", "Jerome", "MASCULIN", "DVD", 11976, 20.22, 31.89)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate]
        district = factory_district("2ème circonscription", 5502, 55, 59230, 38599, candidates)               
        return district  
    
    def __construct_district_6502(self):
        first_candidate = factory_candidate("MEUNIER", "François", "MASCULIN", "EXG", 692, 0.78, 1.14)
        second_candidate = factory_candidate("BÉHAGUE", "Jacques", "MASCULIN", "LR", 3184, 3.60, 5.24)
        third_candidate = factory_candidate("DABAT", "Jean-Marc", "MASCULIN", "REG", 1486, 1.68, 2.45)
        fourth_candidate = factory_candidate("MOURNET", "Benoit", "MASCULIN", "ENS", 15121, 17.09, 24.91)
        fifth_candidate = factory_candidate("FÉGNÉ", "Denis", "MASCULIN", "UG", 17055, 19.27, 28.09)
        sixth_candidate = factory_candidate("EL MARSNI", "Ali", "MASCULIN", "DIV", 0, 0.00, 0.0)
        seventh_candidate = factory_candidate("MONTEIL", "Olivier", "MASCULIN", "RN", 22436, 25.35, 36.96)
        eighth_candidate = factory_candidate("ALVES DA CUNHA", "Claude", "MASCULIN", "REC", 735, 0.83, 1.21)        
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                      seventh_candidate, eighth_candidate]
        district = factory_district("2ème circonscription", 6502, 65, 88496, 62793, candidates)               
        return district
    
    def __construct_district_7502(self):
        first_candidate = factory_candidate("JOLIVEAU", "Charline", "FEMININ", "EXG", 168, 0.23, 0.30)
        second_candidate = factory_candidate("DE WITTE", "Melody", "FEMININ", "RN", 6206, 8.32, 11.00)
        third_candidate = factory_candidate("SACASA", "Clara", "FEMININ", "EXG", 0, 0.00, 0.00)
        fourth_candidate = factory_candidate("HERZOG DE COSSÉ BRISSAC", "Félicité", "FEMININ", "DVD", 3792, 5.08, 6.72)
        fifth_candidate = factory_candidate("LE GENDRE", "Gilles", "MASCULIN", "DVC", 11071, 14.84, 19.62)
        sixth_candidate = factory_candidate("EVANGELISTA", "Ornella", "FEMININ", "REC", 778, 1.04, 1.38)
        seventh_candidate = factory_candidate("LAUSSUCQ", "Jean", "MASCULIN", "RENSN", 13325, 17.87, 23.62)
        eighth_candidate = factory_candidate("LORANS", "Cécile Marie", "FEMININ", "ECO", 512, 0.68, 0.91)     
        nineth_candidate = factory_candidate("MARSILY", "Romain", "MASCULIN", "DVD", 1229, 1.65, 2.18)
        tenth_candidate = factory_candidate("MAURIANGE", "Frédéric", "MASCULIN", "DVC", 430, 0.58, 0.76)
        eleventh_candidate = factory_candidate("MAGNE", "Elise", "FEMININ", "DVG", 60, 0.08, 0.11)
        twelth_candidate = factory_candidate("ROSSET", "Marine", "FEMININ", "UG", 18845, 25.27, 33.4)
        candidates = [first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, 
                      seventh_candidate, eighth_candidate, nineth_candidate, tenth_candidate, eleventh_candidate, 
                      twelth_candidate]
        district = factory_district("2ème circonscription", 7502, 75, 74579, 56908, candidates)               
        return district                                                                                          