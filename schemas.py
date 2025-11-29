from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

#Response
class Todo(TodoBase):
    id: int
    class Config:
        orm_mode=True

