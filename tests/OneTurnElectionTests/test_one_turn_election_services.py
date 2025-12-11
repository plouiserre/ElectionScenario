import unittest
from unittest.mock import Mock
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.domain.services.OneTurnElection.DeterminateAllElectedPersons import DeterminateAllElectedPersons
from src.backend.domain.services.OneTurnElection.DeterminateElectedPersonByDistrict import DeterminateElectedPersonByDistrict
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection
from tests.utils.assert_helper import assert_congress_person_with_district
from tests.utils.data.catalogData import generate_datas


class OneTurnElectionServiceCaseTest(unittest.TestCase):
    def test_one_turn_election_2024_determinate_good_congress_persons(self):
        total_congress_persons = 8
        year = 2024
        json_files = Mock()
        json_files.get_elections_data.return_value = generate_datas("results_elections", "json_results")
        json_service = JsonResultsElection(json_files)
        representative_congress = RepresentativeCongress(total_congress_persons)
        stability_congress = StabilityCongress(total_congress_persons)
        build_congress = BuildCongress(stability_congress, representative_congress)
        elected_persons_by_district = DeterminateElectedPersonByDistrict()
        all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
        election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
        
        congress = election.Determinate(year)

        self.__assert_congress_2024(congress)

    
    def __assert_congress_2024(self, congress):
        self.assertEqual(2024, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("QUITE", congress.stability_majority)
        self.assertEqual("QUITE", congress.representative_congress)
        self.__assert_parties_2024(congress.parties)

    def __assert_parties_2024(self, parties):
        self.__assert_rn_2024(parties[0])
        self.__assert_ug_2024(parties[1])
        self.__assert_dvd_2024(parties[2])

    def __assert_rn_2024(self, rn_party):
        self.assertEqual("Rassemblement National", rn_party.name)
        self.assertEqual("RN", rn_party.code)
        self.assertEqual(4, rn_party.elected_congress_persons)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", rn_party.congress_persons[0], self)
        assert_congress_person_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", rn_party.congress_persons[1], self)                            
        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", rn_party.congress_persons[2], self)                          
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", rn_party.congress_persons[3], self)

    def __assert_ug_2024(self, ug_party):
        self.assertEqual("Union de la gauche", ug_party.name)
        self.assertEqual("UG", ug_party.code)
        self.assertEqual(3, ug_party.elected_congress_persons)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", ug_party.congress_persons[0], self)        
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", ug_party.congress_persons[1], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", ug_party.congress_persons[2], self)

    def __assert_dvd_2024(self, dvd_party):
        self.assertEqual("Divers droite", dvd_party.name)
        self.assertEqual("DVD", dvd_party.code)
        self.assertEqual(1, dvd_party.elected_congress_persons)
        assert_congress_person_with_district("BONY|Jean Yves|MASCULIN|DVD|12383|34.29|2ème circonscription|1502|Cantal|15", dvd_party.congress_persons[0], self)        
    
    
    def test_one_turn_election_2022_determinate_good_congress_persons(self):
        total_congress_persons = 8
        year = 2022
        json_files = Mock()
        json_files.get_elections_data.return_value = generate_datas("results_elections", "json_results")
        json_service = JsonResultsElection(json_files)
        representative_congress = RepresentativeCongress(total_congress_persons)
        stability_congress = StabilityCongress(total_congress_persons)
        build_congress = BuildCongress(stability_congress, representative_congress)
        elected_persons_by_district = DeterminateElectedPersonByDistrict()
        all_elected_persons = DeterminateAllElectedPersons(elected_persons_by_district)
        election = OneTurnElectionService(json_service, all_elected_persons, build_congress)
        
        congress = election.Determinate(year)

        self.__assert_congress_2022(congress)


    def __assert_congress_2022(self, congress):
        self.assertEqual(2022, congress.year)
        self.assertEqual("OneTurn", congress.mode)
        self.assertEqual("PERFECT", congress.stability_majority)
        self.assertEqual("LOW", congress.representative_congress)
        self.__assert_parties_2022(congress.parties)


    def __assert_parties_2022(self, parties):
        self.__assert_ens_2022(parties[0])
        self.__assert_nupes_2022(parties[1])
        self.__assert_lr_2022(parties[2])
        self.__assert_rn_2022(parties[3])


    def __assert_ens_2022(self, ens_party):
        self.assertEqual("Ensemble ! (Majorité présidentielle)", ens_party.name)
        self.assertEqual("ENS", ens_party.code)        
        self.assertEqual(5, ens_party.elected_congress_persons)
        assert_congress_person_with_district("GIRAUD|Joel|MASCULIN|ENS|10889|38.04|2ème circonscription|2|Hautes-Alpes|05", ens_party.congress_persons[0], self)
        assert_congress_person_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|22630|41.41|2ème circonscription|2|Ille-et-Vilaine|35", ens_party.congress_persons[1], self)                            
        assert_congress_person_with_district("JANVIER|Caroline|FEMININ|ENS|11978|29.1|2ème circonscription|2|Loiret|45", ens_party.congress_persons[2], self)                          
        assert_congress_person_with_district("MOURNET|Benoit|MASCULIN|ENS|10870|23.75|2ème circonscription|2|Hautes-Pyrénées|65", ens_party.congress_persons[3], self)
        assert_congress_person_with_district("LE GENDRE|Gilles|MASCULIN|ENS|15547|35.66|2ème circonscription|2|Paris|75", ens_party.congress_persons[4], self)

    def __assert_lr_2022(self, lr_party):
        self.assertEqual("Les Républicains", lr_party.name)
        self.assertEqual("LR", lr_party.code)
        self.assertEqual(1, lr_party.elected_congress_persons)   
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|10472|37.71|2ème circonscription|2|Cantal|15", lr_party.congress_persons[0], self)        
        
    def __assert_nupes_2022(self, nup_party):
        self.assertEqual("Nouvelle union populaire écologique et sociale", nup_party.name)
        self.assertEqual("NUP", nup_party.code)
        self.assertEqual(1, nup_party.elected_congress_persons)
        assert_congress_person_with_district("RAVACLEY|Stéphane|MASCULIN|NUP|13112|32.51|2ème circonscription|2|Doubs|25", nup_party.congress_persons[0], self)        
    
    def __assert_rn_2022(self, rn_party):
        self.assertEqual("Rassemblement National", rn_party.name)
        self.assertEqual("RN", rn_party.code)
        self.assertEqual(1, rn_party.elected_congress_persons)
        assert_congress_person_with_district("GOULET|Florence|FEMININ|RN|8693|32.68|2ème circonscription|2|Meuse|55", rn_party.congress_persons[0], self)            