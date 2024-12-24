from modules.task.internal.task_util import TaskUtil
from modules.task.internal.store.task_model import TaskModel
from modules.task.internal.store.task_repository import TaskRepository
from modules.task.types import Task,TaskErrorCode

class TaskReader:
    @staticmethod
    def get_task_of_account(*,account:str) -> TaskModel:
        pass

from typing import List, Optional
from bson import ObjectId
from modules.task.internal.store.task_model import TaskModel
from modules.task.internal.store.task_repository import TaskRepository
from modules.task.internal.task_util import TaskUtil
from modules.task.types import Task, GetAllTaskParams,TaskErrorCode, GetTaskParams, PaginationParams

class TaskReader:
    @staticmethod
    def get_task_for_account(params: GetTaskParams) -> Task:
        task = TaskRepository.collection().find_one({
            "_id": ObjectId(params.task_id),
            "account":  ObjectId(params.accountId),
            "active": True,
        })
        if not task:
            raise TaskErrorCode(f"Task with id {params.task_id} not found")

        return TaskUtil.convert_task_model_to_task(TaskModel(**task))

    @staticmethod
    def get_tasks_for_account(params: GetAllTaskParams) -> List[Task]:
       
        obj_id = ObjectId(params.accountId)

        total_tasks_count = TaskRepository.collection().count_documents({
            "account": obj_id,
        })
     

        pagination_params = PaginationParams(
            page=params.page if params.page else 1,
            size=params.size if params.size else total_tasks_count,
        )

        start_index = (pagination_params.page - 1) * pagination_params.size

        tasks = (
            TaskRepository.collection()
            .find({"account": obj_id})
            .skip(start_index)
            .limit(pagination_params.size)
        )

        return [TaskUtil.convert_task_model_to_task(TaskModel(**task)) for task in tasks]
