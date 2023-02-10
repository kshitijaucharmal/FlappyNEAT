from genome import Genome
from geneh import GeneHistory

class Species:
    def __init__(self, mem):
        self.members = []
        self.members.append(mem)
        self.rep = self.members[0]
        self.threshold = 3.0
        pass

    def add(self, brain):
        cd = self.rep.calculate_compatibility(brain)
        if cd < self.threshold:
            self.members.append(brain)
            # TODO: Check fitness and set as rep
            return True
        return False
