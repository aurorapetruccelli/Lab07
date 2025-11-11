from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    #query che legge tutti gli artefatti
    def read_all_artefatti(self):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary = True)
            query = "SELECT * FROM artefatto"
            cursor.execute(query)
            for row in cursor:
                artefatto = Artefatto(row["id"],row["nome"],row["tipologia"],row["epoca"],row["id_museo"])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti

    #query che legge solo gli artefatti filtrati in base all'epoca sceleta
    def read_artefatti_filtrati(self,epoca_scelta):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary = True)
            query = "SELECT * FROM artefatto WHERE epoca = %s"
            cursor.execute(query,(epoca_scelta,))
            for row in cursor:
                artefatto = Artefatto(row["id"],row["nome"],row["tipologia"],row["epoca"],row["id_museo"])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti