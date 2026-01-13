import json
from src.backend.domain.models.department import Department

def load_three_departments():
    json_data = "{\"departments\":[{\"name\":\"Allier\",\"code\":\"3\"},{\"name\":\"Cantal\",\"code\":\"15\"},{\"name\":\"Gironde\",\"code\":\"33\"}]}"
    json_departments = json.loads(json_data)
    departments = []
    for json_department in json_departments["departments"]:
        dpt = Department()
        dpt.code = json_department["code"]
        dpt.name = json_department["name"]
        departments.append(dpt)
    return departments