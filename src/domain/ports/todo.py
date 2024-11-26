from typing import List, Protocol

from adapters.db.schema import TodoTable


class TodoPort(Protocol):

    def create(self, todo: TodoTable) -> None:
        """Create a new todo"""

    def get_all(self) -> List[TodoTable]:
        """Get list of all todos"""

    def get_todo_by_id(self, todo_id: str) -> TodoTable:
        """Get todo by unique todo id"""

    def update(self, todo: TodoTable) -> None:
        """Update existing todo with updated values"""

    def delete_todo_by_id(self, todo_id: str) -> None:
        """Delete a single existing todo with todo Id"""

    def delete_all(self) -> None:
        """Delete all existing todos"""
