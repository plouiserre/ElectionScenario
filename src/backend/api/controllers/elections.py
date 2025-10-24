from fastapi import APIRouter
from api.factory import factory_congress_man, factory_district_response, factory_party

router = APIRouter()

@router.get("/elections/{year}/results/{mode}", tags=["elections"])
async def get_results_elections(year : str, mode : str):
    first_district = factory_district_response("10ème circonscription", "3310", "33", "Gironde")
    first_congress_man_first_district = factory_congress_man("BOUDIÉ",	"Florent", first_district) #ENS
    second_district = factory_district_response("4ème circonscription", "4204", "42", "Loire")
    second_congress_man_second_district = factory_congress_man("BONNET", "Sylvie", second_district) #LR
    third_district = factory_district_response("1ère circonscription", "4801", "48", "Lozère")
    third_congress_man_third_district = factory_congress_man("PANTEL","Sophie", third_district) #NFP
    fourth_district = factory_district_response("6ème circonscription", "5606", "56", "Morbihan")
    fourth_congress_man_fourth_district = factory_congress_man("JACQUES", "Jean-Michel", fourth_district) #ENS
    fifth_district = factory_district_response("3ème circonscription", "7503", "75", "Paris")
    fifth_congress_man_fitfh_district = factory_congress_man("BALAGE EL MARIKY", "Léa", fifth_district)
    first_party = factory_party("En Marche Ensemble", "ENS", 40.0, [first_congress_man_first_district, fourth_congress_man_fourth_district])
    second_party = factory_party("Nouveau Front Populaire", "NFP", 40.0, [second_congress_man_second_district, fifth_congress_man_fitfh_district])
    third_party = factory_party("Les Republicains", "LR", 20.0, third_congress_man_third_district)
    parties = [ first_party, second_party, third_party]
    return {"year": year, "mode": mode, "parties" : parties} 