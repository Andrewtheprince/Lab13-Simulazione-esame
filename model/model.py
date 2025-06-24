import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}

    @staticmethod
    def getAnni():
        return DAO.getAllAnni()

    def buildGraph(self, anno):
        self._graph.clear()
        self._idMap.clear()
        nodi = DAO.getNodi(anno)
        self._graph.add_nodes_from(nodi)
        for nodo in nodi:
            self._idMap[nodo.driverId] = nodo
        archi = DAO.getArchi(anno)
        for arco in archi:
            if arco["driver1"] in self._idMap and arco["driver2"] in self._idMap:
                self._graph.add_edge(self._idMap[arco["driver1"]], self._idMap[arco["driver2"]], weight = arco["tot"])


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()
