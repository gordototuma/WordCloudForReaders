import networkx as nx
import matplotlib.pyplot as plt

class RelationshipGraph():

    def __init__(self, relationship):

        self._edges = relationship
        self._nodes = set()
        self._data_from_nodes()
        

    def _data_from_nodes(self):

        for x in self._edges:
            self._nodes.add(x[0])
            self._nodes.add(x[1])
    

    def graph(self):

        G = nx.DiGraph()
        G.add_nodes_from(list(self._nodes))
        G.add_edges_from(self._edges)
        nx.draw_circular(G, with_labels = True)
        plt.show()

    

