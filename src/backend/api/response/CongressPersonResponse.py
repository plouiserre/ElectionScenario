from api.response.DistrictResponse import DistrictResponse

class CongressPersonResponse : 
    def __init__(self):
        self.district = DistrictResponse()
        self.last_name = ''
        self.first_name= ''
        self.vote = 0
        self.vote_percentage = 0.0