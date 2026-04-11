from sqlmodel import Session, SQLModel
from app.models.project import Project
from app.database import engine

def seed_db():
    # ESTO ES CLAVE: Crea las tablas antes de sembrar
    SQLModel.metadata.create_all(engine)
    
    projects = [
        Project(title="LexiQ", description="Arquitectura RAG con Gemini 2.5", tech_stack="Python, FastAPI, Gemini", category="AI"),
        Project(title="FinQ", description="Sistema de gestión financiera", tech_stack="Java, Spring Boot, Postgres", category="Fullstack"),
        Project(title="Bovisoft", description="Software para gestión ganadera", tech_stack="Vue.js, Tailwind", category="Frontend")
    ]
    with Session(engine) as session:
        for p in projects:
            session.add(p)
        session.commit()
    print("✅ Base de datos recreada y poblada con éxito")

if __name__ == "__main__":
    seed_db()
