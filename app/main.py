from fastapi import FastAPI, Depends, HTTPException, Header 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  
from sqlmodel import Session, select
from typing import List
import os  

# Importaciones locales
from .database import create_db_and_tables, get_session
from .models.project import Project
from .routers import ai

app = FastAPI(title="Santiago's Portfolio API")

# --- CONFIGURACIÓN PARA IMÁGENES LOCALES ---
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

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

# --- ENDPOINT BILINGÜE MEJORADO ---
@app.get("/projects", tags=["Projects"])
def read_projects(
    session: Session = Depends(get_session),
    accept_language: str = Header(default="es") 
):
    projects = session.exec(select(Project)).all()
    
    # 1. Limpieza del Header: Tomamos solo el primer idioma de la lista
    # Esto evita errores cuando el navegador manda: "en-US,en;q=0.9,es;q=0.8"
    primary_lang = accept_language.split(',')[0].lower()
    is_english = primary_lang.startswith("en")
    
    # DEBUG: Revisa tu terminal de Python para ver qué llega del Front
    print(f"--- DEBUG: Idioma recibido: {primary_lang} | ¿Es inglés?: {is_english} ---")

    translated_projects = []
    
    for p in projects:
        # Convertimos a diccionario para trabajar sobre una copia
        project_dict = p.model_dump() if hasattr(p, "model_dump") else p.dict()
        
        if is_english:
            # Si es inglés, intentamos usar los campos _en
            project_dict["description"] = project_dict.get("description_en") or project_dict.get("description")
            project_dict["explanation"] = project_dict.get("explanation_en") or project_dict.get("explanation")
        else:
            # Si es español o cualquier otro, nos aseguramos de usar los campos base
            project_dict["description"] = project_dict.get("description")
            project_dict["explanation"] = project_dict.get("explanation")
        
        translated_projects.append(project_dict)
                
    return translated_projects

@app.post("/projects", response_model=Project, tags=["Projects"])
def create_project(project: Project, session: Session = Depends(get_session)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project 