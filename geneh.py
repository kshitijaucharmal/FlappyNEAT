

class GeneHistory:
    def __init__(self, n_inputs, n_outputs):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.all_genes = []
        self.global_inno = 0
        self.highest_hidden = 2
        pass

    def exists(self, n1, n2):
        for g in self.all_genes:
            if g.in_node.number == n1.number and g.out_node.number == n2.number:
                return g.clone()
        return None
