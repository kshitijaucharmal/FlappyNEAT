from node import Node
from gene import Gene
import random

class Genome:
    def __init__(self, gh):
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

        if random.random() < 0.2:
            self.gh.highest_hidden += 1

        n = Node(self.total_nodes, random.randint(2, self.gh.highest_hidden))
        self.total_nodes += 1

        g = random.choice(self.genes)
        l1 = g.in_node.layer
        l2 = g.out_node.layer
        if l2 == 1:
            l2 = 1000000

        while l1 > n.layer or l2 < n.layer:
            g = random.choice(self.genes)
            l1 = g.in_node.layer
            l2 = g.out_node.layer
            if l2 == 1:
                l2 = 1000000

        self.connect_nodes(g.in_node, n)
        self.connect_nodes(n, g.out_node)
        self.genes[-1].weight = 1.0
        self.genes[-2].weight = g.weight
        g.enabled = False
        self.nodes.append(n)
        pass

    def get_info(self) -> str:
        s = 'Genome -----------------------\n'
        for g in self.genes:
            s += g.get_info()

        s += '------------------------------'
        return s

    def __str__(self) -> str:
        return self.get_info()

    def show(self, ds):
        # Set Positions
        w, h = ds.get_size()
        vert_gap = h / (self.n_inputs + 1)
        for i in range(self.n_inputs):
            self.nodes[i].pos = [50, self.nodes[i].number * vert_gap + vert_gap]
        vert_gap = h / (self.n_outputs + 1)
        for i in range(self.n_inputs, self.n_inputs + self.n_outputs):
            self.nodes[i].pos = [w - 50, (self.nodes[i].number - self.n_inputs) * vert_gap + vert_gap]

        # For hidden nodes
        hidden_nodes = self.nodes[(self.n_inputs + self.n_outputs):]
        vert_gap = h / (len(hidden_nodes) + 1)
        for i, n in enumerate(hidden_nodes):
            if n.pos[0] == 0:
                n.pos = [w / 2, n.number - (self.n_inputs + self.n_outputs + 1) * vert_gap + vert_gap]

        for g in self.genes:
            g.show(ds)
        for n in self.nodes:
            n.show(ds)
        pass
