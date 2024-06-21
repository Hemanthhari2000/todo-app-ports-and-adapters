from typing import List

from adapters.db.schema import TodoTable
from adapters.db.session import DBSession
from domain.ports.todo import TodoPort


class TodoAdapter(TodoPort):

    def __init__(self) -> None:
        self.db_session = DBSession()

    def create(self, todo: TodoTable) -> None:
        with self.db_session.get_db() as db:
            db.add(todo)
            db.commit()

    def get_all(self) -> List[TodoTable]:
        with self.db_session.get_db() as db:
            return db.query(TodoTable).all()

    def get_todo_by_id(self, todo_id: str) -> TodoTable:
        with self.db_session.get_db() as db:
            return db.query(TodoTable).filter(TodoTable.id == todo_id).one_or_none()

    def update(self, todo: TodoTable) -> None:
        with self.db_session.get_db() as db:
            todo_to_update = self.get_todo_by_id(todo_id=str(todo.id))
            if todo_to_update is None:
                raise ValueError("Error: Item not found")

            todo_to_update.title = todo.title
            todo_to_update.description = todo.description
            todo_to_update.priority = todo.priority
            todo_to_update.is_completed = todo.is_completed

            db.add(todo_to_update)
            db.commit()

    def delete_todo_by_id(self, todo_id: str) -> None:
        with self.db_session.get_db() as db:
            todo = self.get_todo_by_id(todo_id=todo_id)
            db.delete(todo)
            db.commit()

    def delete_all(self) -> None:
        with self.db_session.get_db() as db:
            db.query(TodoTable).delete()
            db.commit()
