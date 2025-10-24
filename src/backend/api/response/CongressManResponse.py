from api.response.DistrictResponse import DistrictResponse

class CongressManResponse : 
    def __init__(self):
        self.district = DistrictResponse()
        self.last_name = ''
        self.first_name= ''