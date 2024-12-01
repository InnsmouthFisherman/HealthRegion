from pydantic import BaseModel

class Question(BaseModel):
    id: int
    title: str

