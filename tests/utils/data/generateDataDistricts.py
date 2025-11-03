from src.backend.domain.models.factory import factory_district

def build_first_district():
    district = factory_district("2ème circonscription", 502, "Hautes-Alpes", 5)
    return district

def build_second_district():
    district = factory_district("2ème circonscription", 1502, "Cantal", 15)
    return district

def build_third_district():
    district = factory_district("2ème circonscription", 2502, "Doubs", 25)
    return district

def build_fourth_district():
    district = factory_district("2ème circonscription", 3502, "Ille-et-Vilaine", 35)
    return district

def build_fifth_district():
    district = factory_district("2ème circonscription", 4502, "Loiret", 45)
    return district

def build_sixth_district():
    district = factory_district("2ème circonscription", 5502, "Meuse", 55)
    return district

def build_seventh_district():
    district = factory_district("2ème circonscription", 7502, "Paris", 75)
    return district
