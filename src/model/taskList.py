class TaskList:
    def __init__(self,
                taskCod: int = None,
                taskTitle: str = None,
                ownerName: str = None,
                createDate: str = None,
                finishDate: str = None,
                taskDescription: str = None):
        self.set_taskCod(taskCod)
        self.set_taskTitle(taskTitle)
        self.set_ownerName(ownerName)
        self.set_createDate(createDate)
        self.set_finishDate(finishDate)
        self.set_taskDescription(taskDescription)

        def set_taskCod(self, taskCod: int):
            self.taskCod = taskCod
        def set_taskTitle(self, taskTitle: str):
            self.taskTitle = taskTitle
        def set_ownerName(self, ownerName: str):
            self.ownerName = ownerName
        def set_createDate(self, createDate: str):
            self.createDate = createDate
        def set_finishDate(self, finishDate: str):
            self.finishDate = finishDate
        def set_taskDescription(self, taskDescription: str):
            self.taskDescription = taskDescription

        def get_taskCod(self) -> int:
            return self.taskCod
        def get_taskTitle(self) -> str:
            return self.taskTitle
        def get_ownerName(self) -> str:
            return self.ownerName
        def get_createDate(self) -> str:
            return self.createDate
        def get_finishDate(self) -> str:
            return self.finishDate
        def get_taskDescription(self) -> str:
            return self.taskDescription
        
        def to_String(self) -> str:
            return f"Código da tarefa: {self.taskCod}; Título da tarefa: {self.taskTitle()};Proprietário: {self.ownerTask()}; Data de criação: {self.createDate()}; Data de finalização: {self.finishDate()}; Descrição: {self.description()}"


