from sqlmodel import Session, SQLModel
from app.models.project import Project
from app.database import engine

def seed_db():
    # ESTO ES CLAVE: Crea las tablas antes de sembrar
    SQLModel.metadata.create_all(engine)
    
    projects = [
        Project(
            title="LexiQ", 
            description="Arquitectura RAG con Gemini 2.5",
            description_en="RAG Architecture with Gemini 2.5",
            explanation="Plataforma de IA para el análisis inteligente de documentos complejos.",
            explanation_en="AI platform for intelligent analysis of complex documents.",
            tech_stack="Python, FastAPI, Gemini", 
            category="AI"
        ),
        Project(
            title="FinQ", 
            description="Sistema de gestión financiera",
            description_en="Financial management system",
            explanation="Desarrollo Full Stack enfocado en control de flujo de caja y finanzas.",
            explanation_en="Full Stack development focused on cash flow and finance control.",
            tech_stack="Java, Spring Boot, Postgres", 
            category="Fullstack"
        ),
        Project(
            title="Bovisoft", 
            description="Software para gestión ganadera",
            description_en="Livestock management software",
            explanation="Interfaz de usuario optimizada para el control de inventarios y salud animal.",
            explanation_en="User interface optimized for inventory control and animal health.",
            tech_stack="Vue.js, Tailwind", 
            category="Frontend"
        )
    ]
    
    with Session(engine) as session:
        for p in projects:
            session.add(p)
        session.commit()
        
    print("✅ Base de datos recreada y poblada con éxito (Proyectos separados y bilingües)")

if __name__ == "__main__":
    seed_db()