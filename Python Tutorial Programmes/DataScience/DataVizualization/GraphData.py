# CSGraph stands for Compressed Sparse Graph,
# which focuses on Fast graph algorithms based on sparse matrix representations.

# A graph is just a collection of nodes, which have links between them.
# Graphs can represent nearly anything − social network connections,
# each node is a person and is connected to acquaintances; images,
# where each node is a pixel and is connected to neighbouring pixels; points in a high-dimensional distribution,
# where each node is connected to its nearest neighbours and practically anything else you can imagine

import numpy as np
from scipy.sparse import csr_matrix

G_dense = np.array([[0, 2, 1],
                    [2, 0, 0],
                    [1, 0, 0]])

G_masked = np.ma.masked_values(G_dense, 0)

G_sparse = csr_matrix(G_dense)
print(G_sparse.data)

from scipy.sparse.csgraph import csgraph_from_dense

G2_data = np.array([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print(G2_sparse.data)