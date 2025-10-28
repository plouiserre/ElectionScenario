import unittest
from src.backend.usecases.OneTurnElection.OneTurnElectionUseCase import OneTurnElectionUseCase

class OneTurnElectionUseCaseTest(unittest.TestCase):
    def test_one_turn_election_determinate_good_congress_mans(self):
        election = OneTurnElectionUseCase()
        
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
        self.__assert_congress_person_with_district("BOVET|Jorys|17810|34.33|2ème circonscription|302|Allier|3", rn_party.congress_persons[0])
        self.__assert_congress_person_with_district("BAUBRY|Romain|37493|49.48|15ème circonscription|1315|Bouches-du-Rhône|13", rn_party.congress_persons[1])
        self.__assert_congress_person_with_district("DIAZ|Edwige|34590|53.33|11ème circonscription|3311|Gironde|33", rn_party.congress_persons[2])
        self.__assert_congress_person_with_district("CHALUS|BENJAMIN|22290|31.62|4ème circonscription|6304|Puy-de-Dôme|63", rn_party.congress_persons[3])
        self.__assert_congress_person_with_district("BOCCALETTI|Frédéric|32748|48.3|7ème circonscription|8307|Var|83", rn_party.congress_persons[4])

    def __assert_lr(self, lr_party):
        self.assertEqual("Les Républicains", lr_party.name)
        self.assertEqual("LR", lr_party.code)
        self.__assert_congress_person_with_district("WAUQUIEZ|Laurent|27013|36.80|1ère circonscription|4301|Haute Loire|43", lr_party.congress_persons[0])
        self.__assert_congress_person_with_district("BONNIVARD|Emilie|21605|40.86|3ème circonscription|7304|Savoie|73", lr_party.congress_persons[1])

    def __assert_ens(self, ens_party):
        self.assertEqual("Ensemble ! (Majorité présidentielle)", ens_party.name)
        self.assertEqual("ENS", ens_party.code)
        self.__assert_congress_person_with_district("BANNIER|Géraldine|18746|35.17|2ème circonscription|5302|Mayenne|53", ens_party.congress_persons[0])

    def __assert_ug(self, ug_party):
        self.assertEqual("Union de la gauche", ug_party.name)
        self.assertEqual("UG", ug_party.code)
        self.__assert_congress_person_with_district("AUTIN|Clémentine|22209|62.65|11ème circonscription|9311|Seine-Saint-Denis|93", ug_party.congress_persons[0])

    def __assert_uxd(self, ug_party):
        self.assertEqual("Union de l\'extrême droite", ug_party.name)
        self.assertEqual("UXD", ug_party.code)
        self.__assert_congress_person_with_district("LENOIR|Bartolomé|20403|33.35|1ère circonscription|2301|Creuse|23", ug_party.congress_persons[0])


    def __assert_congress_person_with_district(self, datas, congress_person):
        data = datas.split("|")
        self.assertEqual(data[0], congress_person.last_name)
        self.assertEqual(data[1], congress_person.first_name)
        self.assertEqual(int(data[2]), congress_person.vote)
        self.assertEqual(float(data[3]), congress_person.vote_percentage)
        self.assertEqual(data[4], congress_person.district.name)
        self.assertEqual(data[5], congress_person.district.code)
        self.assertEqual(data[6], congress_person.district.department_name)
        self.assertEqual(int(data[7]), congress_person.district.department_code)
