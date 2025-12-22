import unittest
from src.backend.domain.services.ProportionalDepartmentElection.MinimalVoteCongressPerson import MinimalVoteCongressPerson

class MinimalVoteCongressPersonTest(unittest.TestCase): 
    def test_one_congress_person_to_be_elected(self): 
        minimal_vote_congress_person = MinimalVoteCongressPerson()

        minimal = minimal_vote_congress_person.Calculate(1)

        self.assertEqual(50, minimal)

    def test_second_congress_person_to_be_elected(self):
        minimal_vote_congress_person = MinimalVoteCongressPerson()

        minimal = minimal_vote_congress_person.Calculate(2)

        self.assertEqual(35, minimal)


    def test_three_congress_person_to_be_elected(self):
        minimal_vote_congress_person = MinimalVoteCongressPerson()

        minimal = minimal_vote_congress_person.Calculate(3)

        self.assertEqual(25, minimal)


    def test_five_congress_person_to_be_elected(self):
        minimal_vote_congress_person = MinimalVoteCongressPerson()

        minimal = minimal_vote_congress_person.Calculate(5)

        self.assertEqual(15, minimal)


    def test_six_congress_person_to_be_elected(self):
        minimal_vote_congress_person = MinimalVoteCongressPerson()

        minimal = minimal_vote_congress_person.Calculate(6)

        self.assertEqual(11, minimal)

        