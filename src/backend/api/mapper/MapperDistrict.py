from src.backend.api.response.DistrictResponse import DistrictResponse

def to_mapper_district(district_domain):
    response = DistrictResponse()
    response.code = district_domain.code
    response.department_code = district_domain.department_code
    response.department_name = district_domain.department_name
    response.name = district_domain.name
    return response