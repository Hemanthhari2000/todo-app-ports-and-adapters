import uuid

from fastapi import APIRouter, Depends

from adapters.todo_adapter import TodoAdapter
from domain.todo.model import (
    TodoCreateModel,
    TodoModel,
)
from domain.todo.service import TodoService

router = APIRouter()


def get_todo_service() -> TodoService:
    todo_adapter = TodoAdapter()
    return TodoService(todo_port=todo_adapter)


@router.get("/")
def get_all_todo(service: TodoService = Depends(get_todo_service)):
    return service.get_all()


@router.get("/{id}")
def get_todo_by_id(id: str, service: TodoService = Depends(get_todo_service)):
    return service.get_todo_by_id(todo_id=id)


@router.post("/create")
def create_todo(
    todo_model: TodoCreateModel, service: TodoService = Depends(get_todo_service)
):
    todo_id = str(uuid.uuid4())
    service.create(todo=TodoModel(**todo_model.model_dump(), id=todo_id))
    return {f"Todo Created with id: {todo_id}"}


@router.put("/update")
def update_todo(
    todo_model: TodoModel, service: TodoService = Depends(get_todo_service)
):
    service.update(todo=todo_model)
    return {f"Todo Updated, id: {todo_model.id}"}


@router.delete("/delete/{id}")
def delete_todo_by_id(_id: str, service: TodoService = Depends(get_todo_service)):
    service.delete_todo_by_id(todo_id=_id)
    return {f"Todo Deleted, id: {_id}"}


@router.delete("/delete-all")
def delete_all_todos(service: TodoService = Depends(get_todo_service)):
    service.delete_all_todos()
    return {f"All Todos are Deleted."}
