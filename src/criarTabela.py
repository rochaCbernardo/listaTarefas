from db.db import ConexionMysql

def criarTabelas(query: str):
    list_of_commands = query.split(";")

    mysql = ConexionMysql()
    mysql.connect()

    for command in list_of_commands:
        if len(command) > 0:
            print(command)
            try:
                mysql.executeDDL(command)
                print("Executado com sucesso!")
            except Exception as e:
                print(e)

with open("C:/Users/berna/workspacePython/desafioToDoList/sql/taskList.sql") as f:
    query_create = f.read()

print("Criando as tabelas...")
criarTabelas(query_create)
print("Tabelas criadas com sucesso!")