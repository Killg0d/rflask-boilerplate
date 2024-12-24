from dataclasses import dataclass
from typing import Optional, Union

@dataclass(frozen=True)
class Task:
    id:str
    accountId:str
    title:str
    description:str

@dataclass(frozen=True)
class TaskErrorCode:
    NOT_FOUND:str = 'TASK_ERR_01'
    
@dataclass(frozen=True)
class GetAllTaskParams:
    accountId:str
    page: Optional[int] = 1
    size: Optional[int] = None

@dataclass(frozen=True)
class GetTaskParams:
    accountId:str
    taskId:str

@dataclass(frozen=True)
class PaginationParams:
    page:int
    size:int

@dataclass(frozen=True)
class CreateTaskParams:
  accountId: str
  description: str
  title: str

@dataclass(frozen=True)
class UpdateTaskParams:
  accountId: str
  description: str
  taskId: str
  title: str

@dataclass(frozen=True)
class DeleteTaskParams:
  accountId: str
  taskId: str