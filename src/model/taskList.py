class TaskList:
    def __init__(self,
                taskCod: int = None,
                taskTitle: str = None,
                ownerName: str = None,
                createDate: str = None,
                modifyDate: str = None,
                taskDescription: str = None,
                taskStatus: str = None):
        self.set_taskCod(taskCod)
        self.set_taskTitle(taskTitle)
        self.set_ownerName(ownerName)
        self.set_createDate(createDate)
        self.set_finishDate(modifyDate)
        self.set_taskDescription(taskDescription)
        self.set_taskStatus(taskStatus)

        def set_taskCod(self, taskCod: int):
            self.taskCod = taskCod
        def set_taskTitle(self, taskTitle: str):
            self.taskTitle = taskTitle
        def set_ownerName(self, ownerName: str):
            self.ownerName = ownerName
        def set_createDate(self, createDate: str):
            self.createDate = createDate
        def set_modifyDate(self, modifyDate: str):
            self.modifyDate = modifyDate
        def set_taskDescription(self, taskDescription: str):
            self.taskDescription = taskDescription
        def set_taskStatus(self, taskStatus: str):
            self.taskStatus = taskStatus
        

        def get_taskCod(self) -> int:
            return self.taskCod
        def get_taskTitle(self) -> str:
            return self.taskTitle
        def get_ownerName(self) -> str:
            return self.ownerName
        def get_createDate(self) -> str:
            return self.createDate
        def get_fmodifyDate(self) -> str:
            return self.modifyDate
        def get_taskDescription(self) -> str:
            return self.taskDescription
        def get_taskStatus(self) -> str:
            return self.taskStatus
        
        def to_String(self) -> str:
            return f"Código da tarefa: {self.taskCod}; Título da tarefa: {self.taskTitle()};Proprietário: {self.ownerTask()}; Data de criação: {self.createDate()}; Data de finalização: {self.modifyDate()}; Descrição: {self.description()}; Status: {self.taskStatus()}"


