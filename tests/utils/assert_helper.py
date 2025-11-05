def assert_congress_person_with_district(datas, congress_person, unittest):
        __assert_person(datas, congress_person, unittest)

def assert_candidate_with_district(datas, candidates, unittest):
        __assert_person(datas, candidates, unittest)

def __assert_person(datas, persons, unittest):
        data = datas.split("|")
        unittest.assertEqual(data[0], persons.last_name)
        unittest.assertEqual(data[1], persons.first_name)
        unittest.assertEqual(data[2], persons.sexe)
        unittest.assertEqual(data[3], persons.parti_code)
        unittest.assertEqual(int(data[4]), persons.vote)
        unittest.assertEqual(float(data[5]), persons.vote_percentage)
        unittest.assertEqual(data[6], persons.district.name)
        unittest.assertEqual(int(data[7]), persons.district.code)
        unittest.assertEqual(data[8], persons.district.department_name)
        unittest.assertEqual(int(data[9]), persons.district.department_code)

def assert_congress_person_domain(datas, congress_person, unittest):
        data = datas.split("|")
        unittest.assertEqual(data[0], congress_person.last_name)
        unittest.assertEqual(data[1], congress_person.first_name)
        unittest.assertEqual(data[2], congress_person.sexe)
        unittest.assertEqual(data[3], congress_person.parti_code)
        unittest.assertEqual(int(data[4]), congress_person.vote)
        unittest.assertEqual(float(data[5]), congress_person.vote_by_expressed)



def assert_party(datas, party_info, unittest):
        data = datas.split("|")
        unittest.assertEqual(data[0], party_info.name)
        unittest.assertEqual(data[1], party_info.code)
        if(len(data) == 3):
                unittest.assertEqual(float(data[2]), party_info.percentage)