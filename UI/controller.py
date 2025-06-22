import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):

        try:
            anno = int(self._view._txtAnno.value)
            print(anno)
            if not(1816<=anno and anno <= 2016):
                print("inserisci un anno valido")
                return
            else:
                grafo = self._model.calculate(anno)
                self._view.txt_result.controls.append(ft.Text(f"GRAFO CORRETTAMENTE CREATO!"))
                self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {len(grafo.nodes())} nodi"))
                self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {len(grafo.edges())} archi"))
                self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {len(list(nx.connected_components(grafo)))} componenti connesse"))

                for nodo in grafo.nodes():
                    self._view.txt_result.controls.append(ft.Text(f"Il nodo: {nodo.StateNme} ha {len(list(grafo.neighbors(nodo)))} vicini"))

                nodi = self._model.passaNodi()
                for nodo in nodi:
                    self._view._dropStato.options.append(ft.dropdown.Option(text=nodo.StateNme, key=nodo.CCode))
                self._view._dropStato.disabled = False
                self._view.update_page()


        except ValueError:
            print("inserire anno corretto")
            return

    def handleVicini(self, e):
        codice = int(self._view._dropStato.value)
        lista_bfs = self._model.calcola_componente_connessa_con_funzione(codice)
        lista_ricorsione = self._model.calcola_componente_connessa_con_ricorsione(codice)