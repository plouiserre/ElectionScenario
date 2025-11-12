def assert_congress_person_with_district(datas, congress_person, unittest):
        __assert_person(datas, congress_person, unittest)

def assert_candidate_with_district(datas, candidates, unittest):
        __assert_person(datas, candidates, unittest)

def __assert_person(datas, person, unittest):
        data = datas.split("|")
        unittest.assertEqual(data[0], person.last_name)
        unittest.assertEqual(data[1], person.first_name)
        unittest.assertEqual(data[2], person.sexe)
        unittest.assertEqual(data[3], person.parti_code)
        unittest.assertEqual(int(data[4]), person.vote)
        unittest.assertEqual(float(data[5]), person.vote_percentage)
        unittest.assertEqual(data[6], person.district.name)
        unittest.assertEqual(data[7], str(person.district.code))
        unittest.assertEqual(data[8], person.district.department_name)
        unittest.assertEqual(data[9], str(person.district.department_code))

def assert_party(datas, party_info, unittest):
        data = datas.split("|")
        unittest.assertEqual(data[0], party_info.name)
        unittest.assertEqual(data[1], party_info.code)
        if(len(data) == 3):
                unittest.assertEqual(float(data[2]), party_info.elected_congress_persons)