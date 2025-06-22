import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._annoSelezionato = None

    def fillDDYear(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(key = anno, data = anno, on_click=self.selezioneAnno))
        self._view.update_page()

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        pass

    def handleCerca(self, e):
        pass

    def selezioneAnno(self, e):
        self._annoSelezionato = e.control.data
        print(f"Selezionato anno {self._annoSelezionato}")