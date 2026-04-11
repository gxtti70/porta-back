from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    id: int
    title: str
    description: str
    stack: List[str]
    category: str
