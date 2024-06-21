from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Text,
)

from adapters.db.session import Base


class TodoTable(Base):
    __tablename__ = "todos"

    id = Column(Text, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    is_completed = Column(Boolean, default=False)
