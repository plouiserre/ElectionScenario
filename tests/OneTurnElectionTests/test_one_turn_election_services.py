import unittest
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from tests.utils.assert_helper import assert_congress_person_with_district

class OneTurnElectionServiceCaseTest(unittest.TestCase):
    def test_one_turn_election_determinate_good_congress_persons(self):
        election = OneTurnElectionService()
        
        congress = election.Determinate()

        self.__assert_congress(congress)

    
    def __assert_congress(self, congress):
        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.__assert_parties(congress.parties)

    def __assert_parties(self, parties):
        self.__assert_rn(parties[0])
        self.__assert_lr(parties[1])
        self.__assert_ens(parties[2])
        self.__assert_ug(parties[3])
        self.__assert_uxd(parties[4])

    def __assert_rn(self, rn_party):
        self.assertEqual("Rassemblement National", rn_party.name)
        self.assertEqual("RN", rn_party.code)
        assert_congress_person_with_district("BOVET|Jorys|MASCULIN|RN|17810|34.33|2ème circonscription|302|Allier|3", rn_party.congress_persons[0], self)
        assert_congress_person_with_district("BAUBRY|Romain|MASCULIN|RN|37493|49.48|15ème circonscription|1315|Bouches-du-Rhône|13", rn_party.congress_persons[1], self)
        assert_congress_person_with_district("DIAZ|Edwige|FEMININ|RN|34590|53.33|11ème circonscription|3311|Gironde|33", rn_party.congress_persons[2], self)
        assert_congress_person_with_district("CHALUS|BENJAMIN|MASCULIN|RN|22290|31.62|4ème circonscription|6304|Puy-de-Dôme|63", rn_party.congress_persons[3], self)
        assert_congress_person_with_district("BOCCALETTI|Frédéric|MASCULIN|RN|32748|48.3|7ème circonscription|8307|Var|83", rn_party.congress_persons[4], self)

    def __assert_lr(self, lr_party):
        self.assertEqual("Les Républicains", lr_party.name)
        self.assertEqual("LR", lr_party.code)
        assert_congress_person_with_district("WAUQUIEZ|Laurent|MASCULIN|LR|27013|36.80|1ère circonscription|4301|Haute Loire|43", lr_party.congress_persons[0], self)
        assert_congress_person_with_district("BONNIVARD|Emilie|FEMININ|LR|21605|40.86|3ème circonscription|7304|Savoie|73", lr_party.congress_persons[1], self)

    def __assert_ens(self, ens_party):
        self.assertEqual("Ensemble ! (Majorité présidentielle)", ens_party.name)
        self.assertEqual("ENS", ens_party.code)
        assert_congress_person_with_district("BANNIER|Géraldine|FEMININ|ENS|18746|35.17|2ème circonscription|5302|Mayenne|53", ens_party.congress_persons[0], self)

    def __assert_ug(self, ug_party):
        self.assertEqual("Union de la gauche", ug_party.name)
        self.assertEqual("UG", ug_party.code)
        assert_congress_person_with_district("AUTIN|Clémentine|FEMININ|UG|22209|62.65|11ème circonscription|9311|Seine-Saint-Denis|93", ug_party.congress_persons[0], self)

    def __assert_uxd(self, ug_party):
        self.assertEqual("Union de l\'extrême droite", ug_party.name)
        self.assertEqual("UXD", ug_party.code)
        assert_congress_person_with_district("LENOIR|Bartolomé|MASCULIN|UXD|20403|33.35|1ère circonscription|2301|Creuse|23", ug_party.congress_persons[0], self)


    # def test_one_turn_election_determinate_good_congress_persons(self):
    #     json_service = JsonResultsElection()
    #     elected_persons_by_district = DeterminateElectedPersonByDistrict()
    #     all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
    #     election = OneTurnElectionService(json_service, all_elected_persons)
        
    #     congress = election.Determinate()

    #     self.__assert_congress(congress)

    
    # def __assert_congress(self, congress):
    #     self.assertEqual(2024, congress.year)
    #     self.assertEqual("OneTurn", congress.mode)
    #     self.__assert_parties(congress.parties)

    # def __assert_parties(self, parties):
    #     self.__assert_rn(parties[0])
    #     self.__assert_ug(parties[1])
    #     self.__assert_dvd(parties[2])

    # def __assert_rn(self, rn_party):
    #     self.assertEqual("Rassemblement National", rn_party.name)
    #     self.assertEqual("RN", rn_party.code)
    #     assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", rn_party.congress_persons[0], self)
    #     assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", rn_party.congress_persons[1], self)                            
    #     assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", rn_party.congress_persons[2], self)                          
    #     assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", rn_party.congress_persons[3], self)
    #     assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", rn_party.congress_persons[4], self)

    # def __assert_ug(self, ug_party):
    #     self.assertEqual("Union de la gauche", ug_party.name)
    #     self.assertEqual("UG", ug_party.code)
    #     assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", ug_party.congress_persons[0], self)        
    #     assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", ug_party.congress_persons[1], self)
    #     assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", ug_party.congress_persons[2], self)

    # def __assert_dvd(self, dvd_party):
    #     self.assertEqual("Divers droite", dvd_party.name)
    #     self.assertEqual("DVD", dvd_party.code)
    #     assert_congress_person_with_district("BONY|Jean Yves|MASCULIN|DVD|12383|34.29|2ème circonscription|1502|Cantal|15", dvd_party.congress_persons[0], self)        
    