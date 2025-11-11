import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def handler_popola_musei(self):
        # inserisco i musei nelle opzioni della dropdown
        musei = self._model.get_musei()
        for museo in musei:
            self._view._dd_museo.options.append(ft.dropdown.Option(museo))
        self._view.page.update()

    def handler_popola_epoca(self):
        # inserisco le epoche nelle opzioni della dropdown
        epoche = self._model.get_epoche()
        for epoca in epoche:
            self._view._dd_epoche.options.append(ft.dropdown.Option(epoca))
        self._view.page.update()


    # CALLBACKS DROPDOWN
    def handler_musei_change(self,e):
        if self.museo_selezionato is None:
            self.museo_selezionato= self._view._dd_museo.value
        else:
            self.handler_popola_musei()

    def handler_epoca_change(self,e):
        if self.epoca_selezionata is None:
            self.epoca_selezionata = self._view._dd_epoche.value
        else:
            self.handler_popola_epoca()


    # AZIONE: MOSTRA ARTEFATTI
    def handler_mostra_artefatti(self,e):
        self._view._artefatti.controls.clear()
        self.museo_selezionato=self._view._dd_museo.value
        self.epoca_selezionata=self._view._dd_epoche.value
        artefatti_filtrati = self._model.get_artefatti_filtrati(self.museo_selezionato,self.epoca_selezionata)
        # alert se nessun artefatto soddisfa i criteri scelti
        if self.museo_selezionato != "Nessun filtro" and self.epoca_selezionata !="Nessun filtro" and artefatti_filtrati == []:
            self._view.alert.show_alert("ERRORE: Nessun artefatto soddisfa i criteri di filtraggio indicati")
        else:
            for artefatto in artefatti_filtrati:
                self._view._artefatti.controls.append(ft.Text(f"{artefatto}"))
            self._view.update()

    # devo mostrare gli artefatti in base al museo e all'epoca scelta