from node import Node
from gene import Gene
import random

class Genome:
    def __init__(self, gh) -> None:
        self.gh = gh
        self.n_inputs = gh.n_inputs
        self.n_outputs = gh.n_outputs
        self.total_nodes = 0
        
        self.nodes = []
        self.genes = []

        for _ in range(self.n_inputs):
            self.nodes.append(Node(self.total_nodes, 0))
            self.total_nodes += 1

        for _ in range(self.n_outputs):
            self.nodes.append(Node(self.total_nodes, 1))
            self.total_nodes += 1
        pass

    def exists(self, inno):
        for g in self.genes:
            if g.inno == inno:
                return True
        return False

    def connect_nodes(self, n1, n2):
        n1layer = n1.layer
        n2layer = n2.layer
        if n2.layer == 1:
            n2layer = 1000000

        if n1layer > n2layer:
            n1, n2 = n2, n1

        c = self.gh.exists(n1, n2)
        x = Gene(n1, n2)

        if c:
            x.inno = c.inno
            if not self.exists(x.inno):
                self.genes.append(x)
        else:
            x.inno = self.gh.global_inno
            self.gh.global_inno += 1
            self.gh.all_genes.append(x.clone())
            self.genes.append(x)
        pass

    def add_gene(self):
        n1 = random.choice(self.nodes)
        n2 = random.choice(self.nodes)

        while n1.layer == n2.layer:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)

        self.connect_nodes(n1, n2)
        pass

    def add_node(self):
        if len(self.genes) == 0:
            self.add_gene()

    def get_info(self):
        s = 'Genome -----------------------\n'
        for g in self.genes:
            s += g.get_info()

        s += '------------------------------'
        return s

    def __str__(self) -> str:
        return self.get_info()
