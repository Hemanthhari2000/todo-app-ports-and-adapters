import uuid

from fastapi import APIRouter, status

from domain.todo.model import (
    TodoCreateModel,
    TodoModel,
)
from domain.todo.service import TodoService

router = APIRouter()

todo_service = TodoService()


@router.get("/")
def get_all_todo():
    return todo_service.get_all()


@router.get("/{id}")
def get_todo_by_id(id: str):
    return todo_service.get_todo_by_id(todo_id=id)


@router.post("/create")
def create_todo(todo_model: TodoCreateModel):
    todo_id = str(uuid.uuid4())
    todo_service.create(todo=TodoModel(**todo_model.model_dump(), id=todo_id))
    return {f"Todo Created with id: {todo_id}"}


@router.put("/update")
def update_todo(todo_model: TodoModel):
    todo_service.update(todo=todo_model)
    return {f"Todo Updated, id: {todo_model.id}"}


@router.delete("/delete/{id}")
def delete_todo_by_id(_id: str):
    todo_service.delete_todo_by_id(todo_id=_id)
    return {f"Todo Deleted, id: {_id}"}


@router.delete("/delete-all")
def delete_all_todos():
    todo_service.delete_all_todos()
    return {f"All Todos are Deleted."}
