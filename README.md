# listaTarefas
Sistema composto por uma tabela em que são armazenados dados de tarefas.
Sistema criado na linguagem python, sendo utilizada a biblioteca flask para integração da linguagem com o banco de daos e a web.

##Organização:
-[main](main.py): Nesse arquivo consta o executável do app criado, ele conecta as demais pastas e arquivos;
-[src](src): Nesse diretório estão os scripts do sistema;
  *[sql](src/sql): Nesse repositório encontra-se o sscript sql utilizado para criação da tabela no banco de dados;
  *[db](src/db): Nesse repositório encontra-se apenas a conexão com o banco de dados MySQL;
  *[model](src/model): Nesse diretório encontra-se a classe da lista de tarefas;
  *[controller](src/controller): Nesse diretório encontra-se a classe controladora, responsável por realizar inserção, alteração, listagem e exclusão dos registros na tabela;
    - Exemplo CRUD, ControllerTaskList:
    ```python
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
    ```
  *[routes](src/routes): Aqui encontram-se as rotas utilizadas para realizar a conexão do backend, do MySQL e das páginas criadas;
    - Exemplo de rota:
    ```python
    @rota_bp.route("/", methods=['GET', 'POST'])
    def home():
      if request.method == 'POST':
        ControllerTaskList.atualizarTask()
        return redirect(url_for('rota.home'))
      else:
        lista = ControllerTaskList.listarDoadores()
        return render_template("home.html", titulo='taskList', taskList = lista)
    ```
  *[templates](src/templates): Nesse repositórico encontram-se os arquivos .html utilizados para criação das páginas web;
  *[static](src/static): Nesse repositório encontra-se o arquivo .css utilizado para estilizar as páginas web criadas;
  *[init.py](src/init.py): Nesse arquivo é feita a ligação da biblioteca flask, do python, com o banco de dados MySQL e as rotas;
