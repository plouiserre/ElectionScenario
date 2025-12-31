import unittest
from src.backend.domain.services.ProportionalDepartmentElection.ModeDesignCongressPerson import ModeDesignCongressPerson

class MinimalVoteCongressPersonTest(unittest.TestCase): 
    def test_one_congress_person_to_be_elected(self): 
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":37.5, "LR" : 5.6, "ENS" :31.6, "UG" : 35.2}

        mode = mode_design_congress_person.Calculate(1, percentage_vote)

        self.assertEqual("order", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_two_congress_persons_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":13.5, "LR" : 11.5, "ENS" :31.6, "UG" : 43.4}

        mode = mode_design_congress_person.Calculate(2, percentage_vote)

        self.assertEqual("order", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_two_congress_persons_with_big_differences_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":13.5, "LR" : 60.3, "ENS" :7.4, "UG" : 18.8}

        mode = mode_design_congress_person.Calculate(2, percentage_vote)

        self.assertEqual("winner", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_three_congress_persons_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":23.5, "LR" : 21.5, "ENS" :32.1, "UG" : 22.9}

        mode = mode_design_congress_person.Calculate(3, percentage_vote)

        self.assertEqual("order", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_three_congress_persons_with_big_differences_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":49.5, "LR" : 19.7, "ENS" :24.3, "UG" : 16.6}

        mode = mode_design_congress_person.Calculate(3, percentage_vote)

        self.assertEqual("winner", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_four_congress_persons_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":13.5, "LR" : 23.6, "ENS" :25.7, "UG" : 37.2}

        mode = mode_design_congress_person.Calculate(4, percentage_vote)

        self.assertEqual("order", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_four_congress_persons_with_big_differences_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":13.5, "LR" : 40.9, "ENS" :22.6, "UG" : 23}

        mode = mode_design_congress_person.Calculate(4, percentage_vote)

        self.assertEqual("winner", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_five_congress_persons_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":13.5, "LR" : 26.3, "ENS" :36.4, "UG" : 23.8}

        mode = mode_design_congress_person.Calculate(5, percentage_vote)

        self.assertEqual("order", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_five_congress_persons_with_big_differences_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":43.5, "LR" : 15.6, "ENS" :18.5, "UG" : 22.4}

        mode = mode_design_congress_person.Calculate(5, percentage_vote)

        self.assertEqual("winner", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

    def test_eighth_congress_persons_to_be_elected(self):
        mode_design_congress_person = ModeDesignCongressPerson()
        percentage_vote = {"RN":13.5, "LR" : 26.3, "ENS" :36.4, "UG" : 23.8}

        mode = mode_design_congress_person.Calculate(8, percentage_vote)

        self.assertEqual("order", mode.type)
        self.assertEqual(12.5, mode.minimal_vote)

        