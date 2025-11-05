import unittest
from src.backend.domain.services.OneTurnElection.BuildCongress import BuildCongress
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection
from tests.utils.assert_helper import assert_congress_person_with_district

class OneTurnElectionServiceCaseTest(unittest.TestCase):
    def test_one_turn_election_determinate_good_congress_persons(self):
        json_service = JsonResultsElection()
        build_congress = BuildCongress()
        elected_persons_by_district = DeterminateElectedPersonByDistrict()
        all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
        election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
        
        congress = election.Determinate(2024, "OneTurn")

        self.__assert_congress(congress)

    
    def __assert_congress(self, congress):
        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.__assert_parties(congress.parties)

    def __assert_parties(self, parties):
        self.__assert_rn(parties[0])
        self.__assert_ug(parties[1])
        self.__assert_dvd(parties[2])

    def __assert_rn(self, rn_party):
        self.assertEqual("Rassemblement National", rn_party.name)
        self.assertEqual("RN", rn_party.code)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", rn_party.congress_persons[0], self)
        assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", rn_party.congress_persons[1], self)                            
        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", rn_party.congress_persons[2], self)                          
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", rn_party.congress_persons[3], self)

    def __assert_ug(self, ug_party):
        self.assertEqual("Union de la gauche", ug_party.name)
        self.assertEqual("UG", ug_party.code)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", ug_party.congress_persons[0], self)        
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", ug_party.congress_persons[1], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", ug_party.congress_persons[2], self)

    def __assert_dvd(self, dvd_party):
        self.assertEqual("Divers droite", dvd_party.name)
        self.assertEqual("DVD", dvd_party.code)
        assert_congress_person_with_district("BONY|Jean Yves|MASCULIN|DVD|12383|34.29|2ème circonscription|1502|Cantal|15", dvd_party.congress_persons[0], self)        
    