from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    #query che legge tutti i musei
    def read_all_musei(self):
        musei = [] #creo la lista dove andrò a inserire tutti i musei
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM museo"""
            cursor.execute(query)
            for row in cursor:
                museo = Museo(row["id"],row["nome"],row["tipologia"])
                musei.append(museo)
            cursor.close()
            cnx.close()
            return musei
    def read_musei_filtrati(self,nome_museo):
        # query che legge solo i musei corrispondenti al nome del museo selezionato
        musei = [] #creo la lista in cui inserirò i musei filtrati
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM museo WHERE nome = %s"""
            cursor.execute(query,(nome_museo,))
            for row in cursor:
                museo = Museo(row["id"],row["nome"],row["tipologia"])
                musei.append(museo)
            cursor.close()
            cnx.close()
            return musei