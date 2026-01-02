import unittest
from src.backend.domain.services.ProportionalDepartmentElection.DeterminateSeatByPartyInDept import DeterminateSeatsByPartyInDept
from src.backend.domain.models.factory import factory_mode_design

class DeterminateSeatByPartyInDeptTest(unittest.TestCase):
    def test_choose_one_party_elected(self):
        mode_design = factory_mode_design("order", 12.5)
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        parties_votes = {"DIV" : 1.25, "DVD" : 22.12, "ENS" : 17.44, "EXG" : 1.57, "REC" : 0.81, "UG" : 23.47, "UXD" : 33.35}   

        seats_party = determinate_seats_by_party_in_dept.Determinate(parties_votes, mode_design, 1)
        
        self.assertEqual(1,len(seats_party))
        self.assertEqual(1,seats_party["UXD"])


    def test_choose_three_parties_elected(self):
        mode_design = factory_mode_design("order", 12.5)
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        parties_votes = {"DVD" : 2.16, "ENS" : 9.32, "UDI" : 0.79, "EXG" : 1.43, "LR" : 24.04, "REC":0.68, "RN" : 37.00, "UG" : 24.58}   

        seats_party = determinate_seats_by_party_in_dept.Determinate(parties_votes, mode_design, 3)
        
        self.assertEqual(3,len(seats_party))
        self.assertEqual(1,seats_party["RN"])
        self.assertEqual(1,seats_party["UG"])
        self.assertEqual(1,seats_party["LR"])


    def test_choose_ten_parties_elected(self):
        mode_design = factory_mode_design("order", 12.5)
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        parties_votes = {"DIV" : 0.12, "DVC" : 0.92, "DVD" : 0.54, "DVG" : 0.04, "ECO" : 0.37, "ENS":28.24, "EXG" : 1.23, "LR" : 2.06, "REC":0.69,
                         "RN":32.92, "UG":32.93}   

        seats_party = determinate_seats_by_party_in_dept.Determinate(parties_votes, mode_design, 12)
        
        self.assertEqual(3,len(seats_party))
        self.assertEqual(4,seats_party["UG"])
        self.assertEqual(4,seats_party["RN"])
        self.assertEqual(4,seats_party["ENS"])

    
    def test_choose_three_parties_elected_with_winner_bonus(self):
        mode_design = factory_mode_design("winner", 12.5)
        determinate_seats_by_party_in_dept = DeterminateSeatsByPartyInDept()
        parties_votes = {"DVD" : 2.16, "ENS" : 9.32, "UDI" : 0.79, "EXG" : 1.43, "LR" : 14.04, "REC":0.68, "RN" : 17.00, "UG" : 54.58}   

        seats_party = determinate_seats_by_party_in_dept.Determinate(parties_votes, mode_design, 3)
        
        self.assertEqual(2,len(seats_party))
        self.assertEqual(2,seats_party["UG"])
        self.assertEqual(1,seats_party["RN"])