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

        self.fitness = random.uniform(-2, 2)

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
        n1layer = n1.layer if n1.layer != 1 else 1000000
        n2layer = n2.layer if n2.layer != 1 else 1000000

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
    
    def mutate(self):
        if len(self.genes) == 0:
            self.add_gene()

        if random.random() < 0.8:
            for i in range(len(self.genes)):
                self.genes[i].mutate()
        if random.random() < 0.08:
            self.add_gene()
        if random.random() < 0.02:
            self.add_node()
        pass

    def connect_genes(self):
        for i in range(len(self.nodes)):
            self.nodes[i].in_genes.clear()

        # Add in_genes
        for i in range(len(self.genes)):
            self.genes[i].out_node.in_genes.append(self.genes[i])
        pass

    def get_outputs(self, inputs):
        if len(inputs) != self.n_inputs:
            print('Wrong number of inputs')
            return [-1]

        for i in range(self.n_inputs):
            self.nodes[i].output = inputs[i]

        self.connect_genes()

        for l in range(2, self.gh.highest_hidden + 1):
            nodes_in_layer = []
            for n in range(len(self.nodes)):
                if self.nodes[n].layer == l:
                    nodes_in_layer.append(self.nodes[n])

            for n in range(len(nodes_in_layer)):
                nodes_in_layer[n].calculate()

        final_outputs = []
        for n in range(self.n_inputs, self.n_inputs + self.n_outputs):
            self.nodes[n].calculate()
            final_outputs.append(self.nodes[n].output)

        return final_outputs

    def get_weight(self, inno):
        for g in self.genes:
            if g.inno == inno:
                return g.weight
        return -1

    def calculate_compatibility(self, partner):
        try:
            p1_highest_inno = max([(a.inno) for a in self.genes])
        except:
            p1_highest_inno = 0

        try:
            p2_highest_inno = max([(a.inno) for a in partner.genes])
        except:
            p2_highest_inno = 0
        highest_inno = max(p1_highest_inno, p2_highest_inno)

        matching = 0
        disjoint = 0
        excess = 0

        c1 = 1.0
        c2 = 1.0
        c3 = 0.4

        flag = 0

        total_weights = 0
        
        for i in range(highest_inno):
            e1 = self.exists(i)
            e2 = partner.exists(i)
            if e1 and e2:
                matching += 1
                flag = i
                total_weights += self.get_weight(i) - partner.get_weight(i)
                continue

        disjoint = (flag+1) - matching
        excess = highest_inno - flag

        if matching == 0:
            matching = 1
        avg_weights = total_weights / matching

        N = 1 if highest_inno < 20 else highest_inno
        excess_coeff = c1 * excess / N
        disjoint_coeff = c2 * disjoint / N
        weight_coeff = c3 * avg_weights

        cd = excess_coeff + disjoint_coeff + weight_coeff

        # print(matching, disjoint, excess)
        # print("Compatibility Distance", cd)
        return cd

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

    def __str__(self):
        return self.get_info()

    def show(self, ds):
        # Set Positions
        w, h = ds.get_size()
        vert_gap = h / (self.n_inputs+1)
        for i in range(self.n_inputs):
            self.nodes[i].pos = [30, self.nodes[i].number * vert_gap + vert_gap]
        vert_gap = h / (self.n_outputs+1)
        for i in range(self.n_inputs, self.n_inputs+self.n_outputs):
            self.nodes[i].pos = [w - 30, (self.nodes[i].number - self.n_inputs) * vert_gap + vert_gap]
        vert_gap = h / ((len(self.nodes) - (self.n_inputs + self.n_outputs)) + 1)
        for i in range(self.n_inputs+self.n_outputs, len(self.nodes)):
            self.nodes[i].pos = [w/2, (self.nodes[i].number - self.n_inputs - self.n_outputs) * vert_gap + vert_gap]

        # Show Genes
        for g in self.genes:
            g.show(ds)
        # Show nodes
        for n in self.nodes:
            n.show(ds)
        pass
