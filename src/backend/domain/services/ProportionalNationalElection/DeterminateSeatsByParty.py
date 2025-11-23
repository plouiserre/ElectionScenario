import math

class DeterminateSeatsByParty : 
    def __init__(self, seats_in_total):
        self.seats_in_total = seats_in_total
        self.results_seats = {}
        self.percentages_for_parties_importants = {}
        self.seats_remaining = 0

    def Calculate(self, percentages_for_parties_importants):
        self.percentages_for_parties_importants = percentages_for_parties_importants
        self.percentages_for_parties_importants = self.__ordered_percentages_for_parties_importants()
        self.__first_calcul_seat()
        self.__calculate_seats_remaining()
        self.__affect_all_seats_remaining()
        return self.results_seats

    def __first_calcul_seat(self): 
        for party in self.percentages_for_parties_importants :
            percentage = self.percentages_for_parties_importants[party]
            number_seats = percentage * self.seats_in_total / 100
            self.results_seats[party] = math.floor(number_seats)

    def __ordered_percentages_for_parties_importants(self) :
        new_ordered_percentages = dict(sorted(self.percentages_for_parties_importants.items(), key=lambda x: x[1], reverse= True))
        return new_ordered_percentages


    def __calculate_seats_remaining(self):
        seats_affected = 0
        for party in self.results_seats :
            seats_affected += self.results_seats[party] 
        self.seats_remaining = self.seats_in_total - seats_affected

    def __affect_all_seats_remaining(self):
        while self.seats_remaining > 0 :
            self.__affect_seats_remaining()

    def __affect_seats_remaining(self):
        for party in self.results_seats : 
            if self.seats_remaining > 0 :
                self.results_seats[party] += 1
                self.seats_remaining -= 1
        