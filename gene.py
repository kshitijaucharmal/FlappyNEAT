import random

class Gene:
    def __init__(self, i, o):
        self.in_node = i
        self.out_node = o
        self.weight = random.random() * 4 - 2
        self.inno = -1
        self.enabled = True
        pass

    def clone(self):
        g = Gene(self.in_node.clone(), self.out_node.clone())
        g.weight = self.weight
        g.enabled = self.enabled
        g.inno = self.inno
        return g

    def get_info(self):
        s = str(self.inno) + "] "
        s += str(self.in_node.number) + "(" + str(self.in_node.layer) + ") -> "
        s += str(self.out_node.number) + "(" + str(self.out_node.layer) + ") "
        s += str(self.weight) + " "
        s += str(self.enabled) + '\n'
        return s

    def __str__(self) -> str:
        return self.get_info()
    pass
