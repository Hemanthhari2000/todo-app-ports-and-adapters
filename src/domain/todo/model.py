from typing import List

from pydantic import BaseModel, ConfigDict

from adapters.db.schema import TodoTable


class TodoCreateModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str = ""
    priority: int
    is_completed: bool


class TodoModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        # json_schema_extra={
        #     "examples": [
        #         {
        #             "title": "string",
        #             "description": "string",
        #             "priority": 0,
        #             "is_completed": "true",
        #         }
        #     ]
        # },
    )

    id: str = ""
    title: str
    description: str = ""
    priority: int
    is_completed: bool

    @staticmethod
    def from_db_model(todo: TodoTable | List[TodoTable]):
        if isinstance(todo, TodoTable):
            return TodoModel.model_validate(todo)
        return [TodoModel.model_validate(t) for t in todo]
