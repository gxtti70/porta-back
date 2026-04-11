from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # <-- NUEVO IMPORT
from sqlmodel import Session, select
from typing import List
import os  # <-- NUEVO IMPORT

# Importaciones locales
from .database import create_db_and_tables, get_session
from .models.project import Project
from .routers import ai

app = FastAPI(title="Santiago's Portfolio API")

# --- CONFIGURACIÓN PARA IMÁGENES LOCALES ---
# Esto crea la carpeta 'uploads' si no existe
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# "Montamos" la carpeta para que sea accesible vía URL
# Ahora: http://localhost:8000/static/imagen.jpg mostrará el archivo
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

# --- CONFIGURACIÓN DE CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Al arrancar, crea las tablas
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(ai.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "online", "message": "API Persistente Lista"}

@app.get("/projects", response_model=List[Project], tags=["Projects"])
def read_projects(session: Session = Depends(get_session)):
    projects = session.exec(select(Project)).all()
    return projects

@app.post("/projects", response_model=Project, tags=["Projects"])
def create_project(project: Project, session: Session = Depends(get_session)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project