import numpy as np
from genome import Genome
from geneh import GeneHistory

gh = GeneHistory(4, 2)
g = Genome(gh)

for i in range(200):
    g.add_gene()

print(g)
