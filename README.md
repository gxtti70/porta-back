# 🚀 Santiago Muñoz | Portafolio Backend (Core API)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

Este es el motor principal de mi ecosistema de portafolio. Una API robusta construida con **FastAPI** que gestiona la persistencia de proyectos y la integración de Inteligencia Artificial para el chatbot personalizado.

## 🛠️ Tecnologías y Arquitectura
* **Framework:** FastAPI (Python) por su alto rendimiento y tipado asíncrono.
* **Base de Datos:** SQLite (Producción inicial en Render) gestionada con SQLAlchemy.
* **IA:** Integración con la API de Google Gemini para el asistente virtual **Lexi Bot**.
* **Seguridad:** Configuración de CORS para comunicación segura con el frontend.

## ✨ Características Principales
* **Endpoints CRUD:** Gestión dinámica de proyectos (Título, Descripción, Imágenes, Tech Stack).
* **Agente de IA:** Chatbot con lógica personalizada que conoce mi trayectoria y proyectos.
* **Documentación Automática:** Swagger UI integrado para pruebas rápidas de endpoints.

## 💻 Instalación Local
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar entorno: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Win).
4. Instalar dependencias: `pip install -r requirements.txt`.
5. Ejecutar: `uvicorn main:app --reload`.

## 🌐 API Endpoints en Vivo
Accede a la documentación en: [https://porta-back.onrender.com/docs](https://porta-back.onrender.com/docs)
