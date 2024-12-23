from dataclasses import asdict

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.access_token.rest_api.access_auth_middleware import access_auth_middleware
from modules.task.task_service import TaskService
from modules.task.types import (
    CreateTaskParams,
    GetAllTaskParams,
    UpdateTaskParams,
)


class TaskView(MethodView):
    
    @access_auth_middleware
    def post(self) -> ResponseReturnValue:
        request_data = request.get_json()
        task_params= CreateTaskParams(accountId=request.account_id,**request_data)
        task = TaskService.create_task(params=task_params)
        task_dict = asdict(task)
        return jsonify(task_dict), 201

    @access_auth_middleware
    def get(self) -> ResponseReturnValue:
        request_data = request.get_json()
        task_params = GetAllTaskParams(accountId=request.account_id, **request_data)
        tasks = TaskService.get_tasks_for_account(params=task_params)
        task_dicts = [asdict(task) for task in tasks] 
        return jsonify(task_dicts), 200
    
    @access_auth_middleware
    def patch(self, task_id:str) -> ResponseReturnValue:
        request_data = request.get_json()  
        update_task_params = UpdateTaskParams(taskId=task_id, accountId=request.account_id, **request_data)
        updated_task = TaskService.update_task_for_account(params=update_task_params)
        updated_task_dict = asdict(updated_task)
        return jsonify(updated_task_dict), 200
    
    @access_auth_middleware
    def delete(self,task_id:str) -> ResponseReturnValue:
        is_deleted = TaskService.delete_task_for_account(task_id=task_id)
        
        if is_deleted:
            return jsonify({"message": "Task deleted successfully"}), 200
        else:
            return jsonify({"error": "Task not found or could not be deleted"}), 404
        