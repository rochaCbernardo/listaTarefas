from app.db.db import ConexionMysql
from app.model.taskList import TaskList
from flask import request, flash
import datetime

data_hora = datetime.datetime.now()
data_formatada = data_hora.strftime("%Y-%m-%d")
hora_formatada = data_hora.strftime("%H:%M")

class ControllerTaskList:
    def __init__(self):
        pass

    def cadastrarTask() -> TaskList:
        mysql = ConexionMysql()
        mysql.connect()

        try:
            taskTitle = request.form['taskTitle']
            ownerName = request.form['ownerName']
            createDate = f'{data_formatada} {hora_formatada}'
            taskDescription = request.form['taskDescription']
            taskStatus = "Cadastrada"

            cadastrar = f'INSERT INTO TASKLIST(TASK_TITLE, OWNER_NAME, CREATE_DATE, TASK_DESCRIPTION, TASK_STATUS) VALUES ("{taskTitle}", "{ownerName}", "{createDate}", "{taskDescription}", "{taskStatus}")'
            mysql.cursor.execute(cadastrar)
            mysql.conexao.commit()

        except:
            return flash("Ocorreu um erro ao cadastrar tarefa, tente novamente.")
        
    def atualizarTask() -> TaskList:
        mysql = ConexionMysql()
        mysql.connect()

        taskCod = request.form['taskCod']
        try:
            taskTitle = request.form['taskTitle']
            ownerName = request.form['ownerName']
            modifyDate = f'{data_formatada} {hora_formatada}'
            taskDescription = request.form['taskDescription']
            taskStatus = request.form['taskStatus']

            atualizar = f'UPDATE TASKLIST SET TASK_TITLE = "{taskTitle}", OWNER_NAME = "{ownerName}", MODIFY_DATE = "{modifyDate}",TASK_DESCRIPTION = "{taskDescription}", TASK_STATUS = "{taskStatus}" WHERE COD_TASK = "{taskCod}"'
            mysql.cursor.execute(atualizar)
            mysql.conexao.commit()

            return flash("Tarefa atualizada com sucesso!")
        except:
            return flash("Ocorreu um erro ao atualizar tarefa, tente novamente.")
        
    def excluirDoador(taskCod) -> TaskList:
        mysql = ConexionMysql()
        mysql.connect()

        try:
            excluir = f'DELETE FROM TASKLIST WHERE COD_TASK = "{taskCod}"'
            mysql.cursor.execute(excluir)
            mysql.conexao.commit()

            return flash("Tarefa excluida com sucesso!")
        except:
            return flash("Ocorreu um erro ao excluir tarefa, tente novamente.")

    def listarDoadores() -> TaskList:
        mysql = ConexionMysql()
        mysql.connect()

        listar = f'SELECT COD_TASK, TASK_TITLE, OWNER_NAME, CREATE_DATE, MODIFY_DATE, TASK_DESCRIPTION, TASK_STATUS FROM TASKLIST'
        mysql.cursor.execute(listar)
        doadores = mysql.cursor.fetchall()
        return doadores
        
    
