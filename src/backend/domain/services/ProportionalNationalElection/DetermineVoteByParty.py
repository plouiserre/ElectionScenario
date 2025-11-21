class DetermineVoteByParty : 
    def __init__(self):
        pass

    def Calculate(self, candidates):
        results = {}
        for candidate in candidates:
            parti_code = candidate.parti_code
            if parti_code == "REG":
                print("stop")
            if parti_code in results :
                results[parti_code] += candidate.vote
            else : 
                results[parti_code] = candidate.vote
        return results