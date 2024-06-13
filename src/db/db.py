import mysql.connector
from pandas import DataFrame

class ConexionMysql:
    
    def connect(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='database_princ',
        )
        self.cursor = self.conexao.cursor()
        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()

    def executeDDL(self, query: str):
        self.cursor.execute(query)

    def sqlToDataFrame(self, query: str) -> DataFrame:
        cursor = ConexionMysql.connect(self)
        cursor.execute(query)
        rows = self.cursor.fetchall()
        return DataFrame(rows, columns=[col[0].lower() for col in self.cursor.description])
