import unittest
from src.backend.domain.services.OneTurnElection.ConstructDepartmentalAssemblies import ConstructDepartmentalAssemblies
from tests.utils.data.catalogData import generate_datas, load_all_parties
from utils.assert_helper import assert_congress_person_with_district, assert_party

class ConstructDepartmentalAssembliesTest(unittest.TestCase):
    def test_constuct_6_departmental_assemblies(self):
        parties_info = generate_datas("party", "parties_info")
        datas = generate_datas("results_elections", "load_20_perfect_districts_results")
        all_parties = load_all_parties()["2024"]
        parties = self.__keep_only_useful_parties(all_parties, parties_info)
        departments = datas[2024].all_departments
        construct_dpt_assemblies = ConstructDepartmentalAssemblies()

        departmentals_assemblies = construct_dpt_assemblies.Build(parties_info, parties, departments)

        self.assertEqual("5", departmentals_assemblies[0].department_code)
        self.assertEqual("Hautes-Alpes", departmentals_assemblies[0].department_name)
        self.assertEqual(1, departmentals_assemblies[0].number_congress_persons)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", departmentals_assemblies[0].congress_persons[0], self)
        assert_party('Rassemblement National|RN|5|1', departmentals_assemblies[0].parties[0], self)
        assert_congress_person_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", departmentals_assemblies[0].parties[0].congress_persons[0], self)
        

        self.assertEqual("15", departmentals_assemblies[1].department_code)
        self.assertEqual("Cantal", departmentals_assemblies[1].department_name)
        self.assertEqual(1, departmentals_assemblies[1].number_congress_persons)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", departmentals_assemblies[1].congress_persons[0], self)     
        assert_party('Les Républicains|LR|4|1', departmentals_assemblies[1].parties[0], self)
        assert_congress_person_with_district("BONY|Jean-Yves|MASCULIN|LR|12383|34.29|2ème circonscription|1502|Cantal|15", departmentals_assemblies[1].parties[0].congress_persons[0], self)   

        self.assertEqual("25", departmentals_assemblies[2].department_code)
        self.assertEqual("Doubs", departmentals_assemblies[2].department_name)
        self.assertEqual(1, departmentals_assemblies[2].number_congress_persons)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", departmentals_assemblies[2].congress_persons[0], self)     
        assert_party('Union de la gauche|UG|2|1', departmentals_assemblies[2].parties[0], self)
        assert_congress_person_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", departmentals_assemblies[2].parties[0].congress_persons[0], self)  

        self.assertEqual("35", departmentals_assemblies[3].department_code)
        self.assertEqual("Ille-et-Vilaine", departmentals_assemblies[3].department_name)
        self.assertEqual(2, departmentals_assemblies[3].number_congress_persons)
        assert_congress_person_with_district("DECOURCELLE|Christophe|MASCULIN|LR|5218|6.93|2ème circonscription|3502|Ille-et-Vilaine|35", departmentals_assemblies[3].congress_persons[0], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", departmentals_assemblies[3].congress_persons[1], self)     
        assert_party('Les Républicains|LR|4|1', departmentals_assemblies[3].parties[0], self)
        assert_congress_person_with_district("DECOURCELLE|Christophe|MASCULIN|LR|5218|6.93|2ème circonscription|3502|Ille-et-Vilaine|35", departmentals_assemblies[3].parties[0].congress_persons[0], self)     
        assert_party('Union de la gauche|UG|2|1', departmentals_assemblies[3].parties[1], self)
        assert_congress_person_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", departmentals_assemblies[3].parties[1].congress_persons[0], self)
        
        self.assertEqual("65", departmentals_assemblies[4].department_code)
        self.assertEqual("Hautes-Pyrénées", departmentals_assemblies[4].department_name)
        self.assertEqual(1, departmentals_assemblies[4].number_congress_persons)
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", departmentals_assemblies[4].congress_persons[0], self)     
        assert_party('Rassemblement National|RN|5|1', departmentals_assemblies[4].parties[0], self)
        assert_congress_person_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", departmentals_assemblies[4].parties[0].congress_persons[0], self)      
        
        self.assertEqual("75", departmentals_assemblies[5].department_code)
        self.assertEqual("Paris", departmentals_assemblies[5].department_name)
        self.assertEqual(2, departmentals_assemblies[5].number_congress_persons)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", departmentals_assemblies[5].congress_persons[0], self)    
        assert_congress_person_with_district("LE GENDRE|Gilles|MASCULIN|DVC|11071|19.62|2ème circonscription|7502|Paris|75", departmentals_assemblies[5].congress_persons[1], self)     
        assert_party('Union de la gauche|UG|2|1', departmentals_assemblies[5].parties[0], self)
        assert_congress_person_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", departmentals_assemblies[5].parties[0].congress_persons[0], self)     
        assert_party('Divers centre|DVC|3|1', departmentals_assemblies[5].parties[1], self)
        assert_congress_person_with_district("LE GENDRE|Gilles|MASCULIN|DVC|11071|19.62|2ème circonscription|7502|Paris|75", departmentals_assemblies[5].parties[1].congress_persons[0], self)  


    def __keep_only_useful_parties(self, all_parties, parties_info) : 
        parties_needed = []
        for dpt_code in parties_info : 
            candidates = parties_info[dpt_code]
            for candidate in candidates : 
                for parti in all_parties : 
                    if parti.code == candidate.parti_code and parti not in parties_needed: 
                        parties_needed.append(parti)
                        break
        return parties_needed
