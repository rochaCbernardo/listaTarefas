from app.controller.controllerTasklist import ControllerTaskList
from flask import Blueprint, redirect, render_template, request, url_for, flash
from app import mysql

rota_bp = Blueprint('rota', __name__)

@rota_bp.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ControllerTaskList.atualizarTask()
        return redirect(url_for('rota.home'))
    else:
        lista = ControllerTaskList.listarDoadores()
        return render_template("home.html", titulo='taskList', taskList = lista)

@rota_bp.route("/cadastrarTask", methods=['GET', 'POST'])
def cadastrarTask():
    if request.method == 'POST':
        ControllerTaskList.cadastrarTask()
        return redirect(url_for('rota.home'))
    else:
        return render_template("cadastrarTask.html")

@rota_bp.route("/delete/<int:taskCod>", methods=['GET'])
def deletarTask(taskCod):
    ControllerTaskList.excluirDoador(taskCod)
    return redirect(url_for('rota.home'))

def init_routes(app):
    app.register_blueprint(rota_bp)
