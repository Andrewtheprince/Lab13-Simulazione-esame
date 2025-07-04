import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._annoSelezionato = None

    def fillDDYear(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(key = anno, data = anno, on_click=self.handleDDYearSelection))
        self._view.update_page()

    def handleDDYearSelection(self, e):
        self._annoSelezionato = e.control.data
        print(f"Selezionato anno {self._annoSelezionato}")

    def handleCreaGrafo(self,e):
        if self._annoSelezionato is None:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text("Seleziona prima un anno!", color = "red"))
            return
        self._model.buildGraph(self._annoSelezionato)
        n,a = self._model.getGraphDetails()
        bestDriver = self._model.getMigliorPilota()
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi:{n}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi:{a}"))
        self._view.txt_result.controls.append(ft.Text(bestDriver))
        self._view.update_page()


    def handleCerca(self, e):
        k = self._view._txtIntK.value
        kint = int(k)
        path, scoretot = self._model.getDreamTeam(kint)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Il Dream Team con il minor tasso di sconfitta pari a {scoretot} è:"))
        for p in path:
            self._view.txt_result.controls.append(ft.Text(p))
        self._view.update_page()