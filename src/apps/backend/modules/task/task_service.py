from modules.task.internal.task_reader import TaskReader
from modules.task.internal.task_writer import TaskWriter
from modules.task.types import (
    Task,
    CreateTaskParams,
    GetTaskParams,
    UpdateTaskParams,
    GetAllTaskParams
)

class TaskService:
    @staticmethod
    def create_task(*, params:CreateTaskParams)->Task:
        return TaskWriter.create_task(params=params)
    
    @staticmethod
    def get_tasks_for_account(*,params:GetAllTaskParams)->Task:
        return TaskReader.get_tasks_for_account(params=params)
    
    @staticmethod
    def update_task_for_account(*,params:UpdateTaskParams)->Task:
        updated_task = TaskWriter.update_task(params=params) 
        return updated_task

    @staticmethod
    def delete_task_for_account(*, task_id: str) -> bool:
        return TaskWriter.delete_task(task_id=task_id)