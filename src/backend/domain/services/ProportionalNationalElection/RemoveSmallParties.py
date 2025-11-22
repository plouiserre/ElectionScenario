class RemoveSmallParties : 
    def __init__(self):
        pass

    def Choose(self, results):
        results_kept = {}
        for key in results : 
            value = results[key]
            if  value >= 5 :
                results_kept[key] = value
        return results_kept