

class Node:
    def __init__(self, n, l):
        self.number = n
        self.layer = l
        self.output = 0
        self.in_genes = []

        pass

    def clone(self):
        n = Node(self.number, self.layer)
        n.output = self.output
        return n

    def calculate(self):
        pass

    def show(self):
        pass
