from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        musei = self._museo_dao.read_musei_filtrati(museo)
        artefatti = self._artefatto_dao.read_artefatti_filtrati(epoca)
        artefatti_completi = self._artefatto_dao.read_all_artefatti()
        lista_artefatti = []

        # se seleziono museo ed epoca diversi da Nessun filtro, deve aggiungere alla lista vuota gli artefatti corrispondenti
        # a museo ed epoca selezionati
        if museo !="Nessun filtro" and epoca!="Nessun filtro":
            for mus in musei:
                for artefatto in artefatti:
                    if mus.id==artefatto.id_museo:
                        lista_artefatti.append(artefatto)

        # se scelgo solo l'epoca aggiungo alla lista solo gli artefatti di quell'epoca
        elif museo=="Nessun filtro" and epoca!="Nessun filtro":
            for artefatto in artefatti:
                if artefatto.epoca ==epoca:
                    lista_artefatti.append(artefatto)

        # se scelgo solo museo aggiungo alla lista solo gli artefatti di quel museo
        elif museo!="Nessun filtro" and epoca=="Nessun filtro":
            for mus in musei:
                for artefatto in artefatti_completi:
                    if mus.id==artefatto.id_museo:
                        lista_artefatti.append(artefatto)

        # se scelgo nessun filtro per entrambi stampo tutti gli artefatti presenti
        elif museo =="Nessun filtro" and epoca=="Nessun filtro":
            for art in artefatti_completi:
                lista_artefatti.append(art)

        return lista_artefatti
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""


    def get_epoche(self):
        artefatti = self._artefatto_dao.read_all_artefatti()
        epoche = [] #lista che deve contenere tutte le epoche presenti
        epoche.append("Nessun filtro") # aggiungo alla lista l'opzione "Nessun filtro"
        for artefatto in artefatti:
            if artefatto.epoca not in epoche:
                epoche.append(artefatto.epoca)
                epoche = sorted(epoche)
        return epoche
        """Restituisce la lista di tutte le epoche."""

    # --- MUSEI ---
    def get_musei(self):
        musei = self._museo_dao.read_all_musei()
        nomi_musei = [] # lista che conterrà i nomi di tutti i musei presenti
        nomi_musei.append("Nessun filtro") #aggiungo l'opzione "Nessun filtro"
        for museo in musei:
            if museo.nome not in nomi_musei:
                nomi_musei.append(museo.nome)
                nomi_musei = sorted(nomi_musei)
        return nomi_musei
        """ Restituisce la lista di tutti i musei."""
