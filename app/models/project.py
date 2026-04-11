from sqlmodel import SQLModel, Field
from typing import Optional

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    # NUEVO: Para la página de detalles que creamos
    explanation: Optional[str] = None 
    tech_stack: str 
    category: str 
    # NUEVO: Aquí guardaremos el link http://localhost:8000/static/foto.png
    images: Optional[str] = None
    link_repo: Optional[str] = None
    link_demo: Optional[str] = None