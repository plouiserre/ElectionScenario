# import unittest
# from src.backend.infrastructure.services.mapper_to_domain import mapper_results_elections_to_list_candidates_with_all_parties_and_all_departments
# from tests.utils.assert_helper import assert_candidate_with_district
# from tests.utils.generateData import get_results_elections_2024

# class MapperToDomainTest(unittest.TestCase):
#     def test_mapper_results_election_to_list_candidates(self): 
#         results = get_results_elections_2024()

#         all_candidates = mapper_results_elections_to_list_candidates_with_all_parties_and_all_departments(results)        

#         self.assertEqual(63, len(all_candidates))
#         assert_candidate_with_district("GUIGNARD|Boris|MASCULIN|EXG|394|1.02|2ème circonscription|502|Hautes-Alpes|5", all_candidates[0], self)
#         assert_candidate_with_district("FINE|Sébastien|MASCULIN|ENS|10338|26.70|2ème circonscription|502|Hautes-Alpes|5", all_candidates[1], self)
#         assert_candidate_with_district("ROSSI|Valérie|FEMININ|UG|12661|32.7|2ème circonscription|502|Hautes-Alpes|5", all_candidates[2], self)
#         assert_candidate_with_district("MONDAIN|Johann|MASCULIN|DIV|2206|5.70|2ème circonscription|502|Hautes-Alpes|5", all_candidates[3], self)
#         assert_candidate_with_district("ALBRAND|Louis|MASCULIN|RN|13115|33.88|2ème circonscription|502|Hautes-Alpes|5", all_candidates[4], self)
    
#         assert_candidate_with_district("CHEIKHI|Mona|FEMININ|EXG|298|0.83|2ème circonscription|1502|Cantal|15", all_candidates[6], self)
#         assert_candidate_with_district("PÉBAY|Zoé|FEMININ|UG|4919|13.62|2ème circonscription|1502|Cantal|15", all_candidates[7], self)
#         assert_candidate_with_district("LACROIX|Gilles|MASCULIN|RN|11923|33.02|2ème circonscription|1502|Cantal|15", all_candidates[8], self)
#         assert_candidate_with_district("VEYSSET-RAPAPORT|Pascal|MASCULIN|REC|220|0.61|2ème circonscription|1502|Cantal|15", all_candidates[9], self)    
#         assert_candidate_with_district("TILMANT-TATISCHEFF|Vladimir|MASCULIN|ENS|3019|8.36|2ème circonscription|1502|Cantal|15", all_candidates[10], self)    
#         assert_candidate_with_district("TOTY|Louis|MASCULIN|DVD|3348|9.27|2ème circonscription|1502|Cantal|15", all_candidates[11], self)        
#         assert_candidate_with_district("BONY|Jean Yves|MASCULIN|DVD|12383|34.29|2ème circonscription|1502|Cantal|15", all_candidates[12], self)        
    
#         assert_candidate_with_district("VOYNET|Dominique|FEMININ|UG|19160|34.16|2ème circonscription|2502|Doubs|25", all_candidates[13], self)        
#         assert_candidate_with_district("VUITTON|Brigitte|FEMININ|EXG|788|1.41|2ème circonscription|2502|Doubs|25", all_candidates[14], self)        
#         assert_candidate_with_district("FUSIS|Eric|MASCULIN|RN|16895|30.12|2ème circonscription|2502|Doubs|25", all_candidates[15], self)        
#         assert_candidate_with_district("VUILLEMIN|Benoît|MASCULIN|ENS|15026|26.79|2ème circonscription|2502|Doubs|25", all_candidates[16], self)        
#         assert_candidate_with_district("ROY|Daniel|MASCULIN|LR|4215|7.52|2ème circonscription|2502|Doubs|25", all_candidates[17], self)        
        
#         assert_candidate_with_district("DEFRANCE|Florence|FEMININ|EXG|746|0.99|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[18], self)                
#         assert_candidate_with_district("DECOURCELLE|Christophe|MASCULIN|LR|5218|6.93|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[19], self)                
#         assert_candidate_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|25792|34.24|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[20], self)                
#         assert_candidate_with_district("VUILLEVANHAECKEMIN|Bérénice|FEMININ|RN|13130|17.43|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[21], self)                
#         assert_candidate_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[22], self)                
#         assert_candidate_with_district("HANNE|Olivier|MASCULIN|ECO|71|0.09|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[23], self)                    
    
#         assert_candidate_with_district("DEFRANCE|Florence|FEMININ|EXG|746|0.99|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[24], self)                
#         assert_candidate_with_district("DECOURCELLE|Christophe|MASCULIN|LR|5218|6.93|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[25], self)                
#         assert_candidate_with_district("MAILLART-MÉHAIGNERIE|Laurence|FEMININ|ENS|25792|34.24|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[26], self)                
#         assert_candidate_with_district("VUILLEVANHAECKEMIN|Bérénice|FEMININ|RN|13130|17.43|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[27], self)                
#         assert_candidate_with_district("LAHAIS|Tristan|MASCULIN|UG|30361|40.31|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[28], self)                
#         assert_candidate_with_district("HANNE|Olivier|MASCULIN|ECO|71|0.09|2ème circonscription|3502|Ille-et-Vilaine|35", all_candidates[29], self)                    
    
#         assert_candidate_with_district("COLAS|Cyril|MASCULIN|LR|4527|7.86|2ème circonscription|4502|Loiret|45", all_candidates[30], self)                    
#         assert_candidate_with_district("JANVIER|Caroline|FEMININ|ENS|13263|23.03|2ème circonscription|4502|Loiret|45", all_candidates[31], self)                        
#         assert_candidate_with_district("MEGDOUD|Farida|FEMININ|EXG|388|0.67|2ème circonscription|4502|Loiret|45", all_candidates[32], self)                        
#         assert_candidate_with_district("CARRANI|Bruno|MASCULIN|ECO|1474|2.56|2ème circonscription|4502|Loiret|45", all_candidates[33], self)                            
#         assert_candidate_with_district("DUPLESSY|Emmanuel|MASCULIN|UG|16148|28.03|2ème circonscription|4502|Loiret|45", all_candidates[34], self)                        
#         assert_candidate_with_district("CHAILLOU|Yann|MASCULIN|DVG|1951|3.39|2ème circonscription|4502|Loiret|45", all_candidates[35], self)                        
#         assert_candidate_with_district("BABIN|Elodie|FEMININ|RN|18957|32.91|2ème circonscription|4502|Loiret|45", all_candidates[36], self)                            
#         assert_candidate_with_district("DUVILLARD|Marie-Odile|FEMININ|REC|716|1.24|2ème circonscription|4502|Loiret|45", all_candidates[37], self)                                
#         assert_candidate_with_district("AACHBOUN|Ahmed|MASCULIN|DVG|178|0.31|2ème circonscription|4502|Loiret|45", all_candidates[38], self)                                
    
#         assert_candidate_with_district("GOULET|Florence|FEMININ|RN|19011|50.63|2ème circonscription|5502|Meuse|55", all_candidates[39], self)                                
#         assert_candidate_with_district("NORDEMANN|Pierre|MASCULIN|ENS|13263|23.03|2ème circonscription|5502|Meuse|55", all_candidates[40], self)                                
#         assert_candidate_with_district("MEGDOUD|Farida|FEMININ|EXG|431|1.15|2ème circonscription|5502|Meuse|55", all_candidates[41], self)                                
#         assert_candidate_with_district("LAFLOTTE|Johan|MASCULIN|UG|5391|14.36|2ème circonscription|5502|Meuse|55", all_candidates[42], self)                                    
#         assert_candidate_with_district("LAFUE|Valentine|FEMININ|ECO|742|1.98|2ème circonscription|5502|Meuse|55", all_candidates[43], self)                                    
#         assert_candidate_with_district("DUMONT|Jerome|MASCULIN|DVD|11976|31.89|2ème circonscription|5502|Meuse|55", all_candidates[44], self)                                    
    
#         assert_candidate_with_district("MEUNIER|François|MASCULIN|EXG|692|1.14|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[44], self)                                    
#         assert_candidate_with_district("BÉHAGUE|Jacques|MASCULIN|LR|3184|5.24|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[45], self)                                    
#         assert_candidate_with_district("DABAT|Jean-Marc|MASCULIN|REG|1486|2.45|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[46], self)                                    
#         assert_candidate_with_district("MOURNET|Benoit|MASCULIN|ENS|15121|24.91|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[47], self)                                    
#         assert_candidate_with_district("FÉGNÉ|Denis|MASCULIN|UG|17055|28.09|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[48], self)                                    
#         assert_candidate_with_district("EL MARSNI|Ali|MASCULIN|DIV|0|0.00|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[49], self)                                    
#         assert_candidate_with_district("MONTEIL|Olivier|MASCULIN|RN|22436|36.96|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[50], self)                                    
#         assert_candidate_with_district("ALVES DA CUNHA|Claude|MASCULIN|REC|735|1.21|2ème circonscription|6502|Hautes-Pyrénées|65", all_candidates[51], self)                                    
        
#         assert_candidate_with_district("JOLIVEAU|Charline|FEMININ|EXG|168|0.30|2ème circonscription|7502|Paris|75", all_candidates[52], self)                                    
#         assert_candidate_with_district("DE WITTE|Melody|FEMININ|RN|6206|11.00|2ème circonscription|7502|Paris|75", all_candidates[53], self)                                    
#         assert_candidate_with_district("SACASA|Clara|FEMININ|EXG|0|0.00|2ème circonscription|7502|Paris|75", all_candidates[54], self)                                    
#         assert_candidate_with_district("HERZOG DE COSSÉ BRISSAC|Félicité|FEMININ|DVD|3792|6.72|2ème circonscription|7502|Paris|75", all_candidates[55], self)                                    
#         assert_candidate_with_district("LE GENDRE|Gilles|MASCULIN|DVC|11071|19.62|2ème circonscription|7502|Paris|75", all_candidates[56], self)                                        
#         assert_candidate_with_district("EVANGELISTA|Ornella|FEMININ|REC|778|1.38|2ème circonscription|7502|Paris|75", all_candidates[57], self)                                        
#         assert_candidate_with_district("LAUSSUCQ|Jean|MASCULIN|ENS|13325|23.62|2ème circonscription|7502|Paris|75", all_candidates[58], self)                                        
#         assert_candidate_with_district("LORANS|Cécile Marie|FEMININ|ECO|512|0.91|2ème circonscription|7502|Paris|75", all_candidates[59], self)                                        
#         assert_candidate_with_district("MARSILY|Romain|MASCULIN|DVD|1229|2.18|2ème circonscription|7502|Paris|75", all_candidates[60], self)                                            
#         assert_candidate_with_district("MAURIANGE|Frédéric|MASCULIN|DVC|430|0.76|2ème circonscription|7502|Paris|75", all_candidates[61], self)                                            
#         assert_candidate_with_district("MAGNE|Elise|FEMININ|DVG|60|0.11|2ème circonscription|7502|Paris|75", all_candidates[62], self)                                            
#         assert_candidate_with_district("ROSSET|Marine|FEMININ|UG|18845|33.4|2ème circonscription|7502|Paris|75", all_candidates[63], self)                                                