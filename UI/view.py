import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # creo dropdown sia per i musei sia per le epoche
        self._dd_museo = ft.Dropdown(label="Museo",
                                     options = [],
                                     width=500,
                                     padding = True,
                                     on_change = self.controller.handler_musei_change
                                     )
        self.controller.handler_popola_musei()

        self._dd_epoche = ft.Dropdown(label="Epoca",
                                     options= [],
                                     width=200,
                                     padding = True,
                                      on_change=self.controller.handler_epoca_change)
        self.controller.handler_popola_epoca()

        # Sezione 3: Artefatti
        # creo la listview e il bottone da schiacciare per mostrare gli artefatti filtrati
        self._artefatti = ft.ListView(expand = False, spacing = 10,padding = 20, auto_scroll=True)
        btn_mostra_artefatti=ft.ElevatedButton(text="Mostra Artefatti",
                                               width=200,
                                               on_click=self.controller.handler_mostra_artefatti)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(controls = [self._dd_museo,self._dd_epoche],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Artefatti
            ft.Row(controls = [btn_mostra_artefatti],
                   alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider(color = "black"),
            self._artefatti,
            ft.Divider(color = "black")
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
