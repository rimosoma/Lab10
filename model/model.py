import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
                    #seleziono tutte le countries dalla tabella e creo l'oggetto
        self.grafo = nx.Graph()
        self.idMap={}

    def calculate(self, anno):
# prende nazione 1 e nazione 2 da ogni relazione, posso usare di nuovo least etc
        self.idMap = DAO.get_id_map_countires(anno)
        self.grafo.add_nodes_from(self.idMap.values())
        lista_tuple = DAO.get_tuple(anno)
        for tup in lista_tuple:
            stato1 = self.idMap[tup[0]]
            stato2 = self.idMap[tup[1]]
            self.grafo.add_edge(stato1, stato2)
        print(nx.connected_components(self.grafo))
        return self.grafo

    def passaNodi(self):
        return self.idMap.values()


    def calcola_componente_connessa_con_funzione(self, codiceNodo):
        stato = self.idMap[codiceNodo]
        tree = nx.dfs_tree(self.grafo, stato)
        a = list(tree.nodes)
        a.remove(stato)
        print(f"ecco gli {len(a)} stati raggiungibili da {stato}")
        return a


    def getRaggiungibiliRecursive(self, n):
        #inizializzo la lista dei visitati
        visited = []

        #chiamo la ricorsione con il nodo di partenza e la lista dei visitati vuota
        #RICORDIAMOCI CHE PASSANDO LA LISTA COSI VERRà MUTATA, ANCHE SE LA RICORSIONE NON RETURNA NULLA
        self._recursive_visit(n, visited)

        #pop del nodo di partenza dalla lista dei raggiungibili(solo perche non va considerato?)
        visited.remove(n)
        return visited

    def _recursive_visit(self, n, visited):
        #aggiungo lo stato di partenza alla stessa esatta lista dei visitati(non è una copia), LO VISITO
        visited.append(n)

        # Itero sui vicini del nodo di partenza
        for c in self._graph.neighbors(n):
            # Filtro: visito il vicino solo se non è gia stato visitato
            if c not in visited:
                #richiamo la
                self._recursive_visit(c, visited)


        """
        tree = nx.bfs_tree(self._graph, n)
        a = list(tree.nodes)
        a.remove(n)
        return a
        """

   """ def calcola_componente_connessa_con_ricorsione(self, codiceNodo):
        #stato di partenza
        stato = self.idMap[codiceNodo]
        #lista nodi visitati
        self.visitati = []
        #lista vicini
        vicini = stato.neighbors()

        #chiamo la ricorsione con la lista attuale, il nodo da inserire e i vicini del suddetto
        self.ricorsione(self.visitati, stato, vicini)

    def ricorsione(self, vis, s, vic):
        self.visitati.append(s)
        for vicino in vic:
            vicini = s.neighbors()
            self.ricorsione(self.visitati, vicino, vicini)
        self.visitati.remove(s)"""


