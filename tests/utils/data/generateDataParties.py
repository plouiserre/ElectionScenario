import json
from src.backend.domain.models.party import Party

def load_all_parties():
    json_parties = "{\"2022\":[{\"name\":\"Divers extrême gauche\",\"code\":\"DXG\"},{\"name\":\"Parti radical de gauche\",\"code\":\"RDG\"},{\"name\":\"Nouvelle union populaire écologique et sociale\",\"code\":\"NUP\"},{\"name\":\"Divers gauche\",\"code\":\"DVG\"},{\"name\":\"Ecologistes\",\"code\":\"ECO\"},{\"name\":\"Divers\",\"code\":\"DIV\"},{\"name\":\"Régionaliste\",\"code\":\"REG\"},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\"},{\"name\":\"Divers centre\",\"code\":\"DVC\"},{\"name\":\"Union des Démocrates et des Indépendants\",\"code\":\"UDI\"},{\"name\":\"Les Républicains\",\"code\":\"LR\"},{\"name\":\"Divers droite\",\"code\":\"DVD\"},{\"name\":\"Droite souverainiste\",\"code\":\"DSV\"},{\"name\":\"Reconquête !\",\"code\":\"REC\"},{\"name\":\"Rassemblement National\",\"code\":\"RN\"},{\"name\":\"Divers extrême droite\",\"code\":\"DXD\"}],\"2024\":[{\"name\":\"Extrême gauche\",\"code\":\"EXG\"},{\"name\":\"Parti communiste français\",\"code\":\"COM\"},{\"name\":\"La France insoumise\",\"code\":\"FI\"},{\"name\":\"Parti socialiste\",\"code\":\"SOC\"},{\"name\":\"Parti radical de gauche\",\"code\":\"RDG\"},{\"name\":\"Les Ecologistes\",\"code\":\"VEC\"},{\"name\":\"Divers gauche\",\"code\":\"DVG\"},{\"name\":\"Union de la gauche\",\"code\":\"UG\"},{\"name\":\"Ecologistes\",\"code\":\"ECO\"},{\"name\":\"Régionaliste\",\"code\":\"REG\"},{\"name\":\"Divers\",\"code\":\"DIV\"},{\"name\":\"Renaissance\",\"code\":\"REN\"},{\"name\":\"Modem\",\"code\":\"MDM\"},{\"name\":\"Horizons\",\"code\":\"HOR\"},{\"name\":\"Ensemble ! (Majorité présidentielle)\",\"code\":\"ENS\"},{\"name\":\"Divers centre\",\"code\":\"DVC\"},{\"name\":\"Union des Démocrates et Indépendants\",\"code\":\"UDI\"},{\"name\":\"Les Républicains\",\"code\":\"LR\"},{\"name\":\"Divers droite\",\"code\":\"DVD\"},{\"name\":\"Droite souverainiste\",\"code\":\"DSV\"},{\"name\":\"Rassemblement National\",\"code\":\"RN\"},{\"name\":\"Reconquête !\",\"code\":\"REC\"},{\"name\":\"Union de l'extrême droite\",\"code\":\"UXD\"},{\"name\":\"Extrême droite\",\"code\":\"EXD\"}]}"
    parties_obj = json.loads(json_parties)
    parties = __transform_to_parties_array(parties_obj)
    return parties 


def __transform_to_parties_array(parties_obj):
    all_parties = {}
    for year in parties_obj:
        all_parties[year] = []
        all_parties_this_year = parties_obj[year]
        for party_obj in all_parties_this_year:
            party = Party()
            party.code = party_obj["code"]
            party.name = party_obj["name"]
            all_parties[year].append(party)
    return all_parties

