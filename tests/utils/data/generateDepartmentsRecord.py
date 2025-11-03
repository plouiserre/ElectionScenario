from src.backend.infrastructure.models.factory_record import factory_department_record

def generate_departments():
    first_department = factory_department_record("Hautes-Alpes", 5)
    second_department = factory_department_record("Cantal", 15)
    third_department = factory_department_record("Doubs", 25)
    fourth_department = factory_department_record("Ille-et-Vilaine", 35)
    fifth_department = factory_department_record("Loiret", 45)
    sixth_deparmtent = factory_department_record("Meuse", 55)
    seventh_department = factory_department_record("Hautes-Pyrénées", 65)
    eighth_department = factory_department_record("Paris", 75)
    departments =[first_department, second_department, third_department, fourth_department, fifth_department, sixth_deparmtent,
                    seventh_department, eighth_department]
    return departments