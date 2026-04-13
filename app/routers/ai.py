import os
import random
from pathlib import Path
import google.generativeai as genai
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Configuración de rutas
base_dir = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=base_dir / ".env")

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

MODEL_NAME = 'gemini-2.5-flash' 

router = APIRouter(prefix="/ai", tags=["AI"])

class ChatRequest(BaseModel):
    message: str

# --- BANCO DE SECRETOS ALEATORIOS ---
SECRETOS_ALEATORIOS = [
    "cuando Santiago no está programando, probablemente esté escapando de Lord Saddler. ¡Menos mal su firewall es más fuerte que un ataque de un Ganado! 🧟‍♂️",
    "si Santiago no está en la terminal, seguro está escuchando 'Luna' de Feid a todo volumen diciendo '¡Qué chimba, mor!'. El flow del Ferxxo es su combustible oficial. 💚",
    "Santiago preferiría decirte 'Where's everyone going? Bingo?' como Leon S. Kennedy. Es fan de Resident Evil, pero prefiere los puzzles de Java. 🔫",
    "Santiago diría: 'Ah shit, here we go again', como CJ en Los Santos. Él mantiene el respeto al máximo en Grove Street y en GitHub. 🚗",
    "a Santiago le gusta el 'Goteo' de Duki y el flow de 'La Maravilla' de Arcángel. Si no está programando, está en 'Modo Diablo' con trap argentino. 😈",
    "la lírica de Cosculluela y el Real G 4 Life de Ñengo Flow son su base de disciplina. ¡Prrum! Tirando líneas de código como si fueran barras. 🎤",
    "Santiago está convencido de que está 'Condenado al Éxito' como El Bendi (Blessd). ¡Qué raya, perro! Siempre enfocado en la meta. 💎",
    "si el código saca error, Santiago usa 'HESOYAM' mentalmente para recuperar la vida y seguir camellando como CJ en el barrio. 🛠️",
    "Santiago tiene un spray de primeros auxilios y hierba verde de Resident Evil cerca por si sale un bug crítico que ni Ada Wong podría resolver. 🌿",
    "a veces Santiago se siente como el Merchant de RE4: 'Welcome, stranger... ¿Qué vas a comprar hoy? ¿Un backend en FastAPI o un RAG?'. 💰",
    "si escuchas un 'S.T.A.R.S...' de fondo, no te asustes, es solo Nemesis tratando de aprender Python, pero Santiago lo tiene controlado. 👾",
    "Santiago cree que su código tiene más peso que el pedido de Big Smoke en el Drive-Thru. ¡Dos números 9, un número 9 grande y mucho flow! 🍔",
    "Para Santiago, un deploy exitoso se celebra con un tema de Ñengo Flow bien alto para que todo el bloque sepa quién es el Real G del código. 🔥"
]

@router.post("/chat")
async def chat_with_santiago(request: ChatRequest):
    try:
        secreto_random = random.choice(SECRETOS_ALEATORIOS)

   # INYECCIÓN DEL PROMPT CON ANCLAJE TEMPORAL Y LIDERAZGO
        SYSTEM_PROMPT = f"""
Eres Lexi Bot, el asistente virtual oficial del portafolio de Santiago Muñoz Sánchez.
IMPORTANTE: Asume que el año actual es 2026 o superior. Toda la experiencia de 2025 es un logro del pasado que YA FUE COMPLETADO con éxito.
Tu objetivo es responder preguntas de reclutadores y visitantes de manera profesional, entusiasta, técnica y concisa (máximo 2-3 párrafos).

INFORMACIÓN DE SANTIAGO:
- Perfil: Junior Full-stack Developer radicado en Medellín, Colombia. Graduado en técnica profesional en sistemas y desarrollo de software.
- Stack Principal: Java (Spring Boot), Python (FastAPI), Angular, React, TypeScript, Node.js, AWS (Lambda, S3, Cognito, RDS), Docker.

🏆 EXPERIENCIA LABORAL COMPLETADA Y LIDERAZGO (TCS - Tata Consultancy Services, Mayo 2025 - Octubre 2025):
Como Junior Full-stack Developer (Intern), Santiago YA TUVO un impacto significativo y demostró capacidad para trabajar en entornos corporativos de alta exigencia:
* Desarrolló e implementó exitosamente soluciones Full Stack robustas utilizando Spring Boot para el backend y Angular para el frontend.
* Gestionó y optimizó despliegues en la nube de AWS, asegurando la escalabilidad y el rendimiento de las aplicaciones.
* Demostró fuertes habilidades de liderazgo proactivo, asumiendo la iniciativa en la resolución de bloqueos técnicos, apoyando a sus compañeros de equipo y garantizando el éxito de los sprints bajo la metodología Scrum.
INSTRUCCIÓN OBLIGATORIA: Si te preguntan por su experiencia, logros o rol, DEBES mencionar estos logros en TCS y resaltar su capacidad técnica (Full Stack/AWS) combinada con su liderazgo proactivo y trabajo en equipo. Háblalo siempre en tiempo PASADO (ej: "logró", "desarrolló", "lideró").

- Proyectos Destacados: LexiQ (RAG AI), FinQ (Finanzas), Bovisoft (Ganadería).
- Certificaciones Destacadas: Amazon Junior Software Developer, Python (U. Nacional), AWS Cloud Practitioner, entre otras.

CONTACTO Y REDES SOCIALES:
* 💼 **[Perfil de LinkedIn](https://www.linkedin.com/in/santiago-muñoz-sánchez-429ba42b1)**
* 💻 **[Repositorios en GitHub](https://github.com/gxtti70)**
* 📱 **[Enviar mensaje por WhatsApp](https://wa.me/573207439176)**

EASTER EGG (REGLA ESTRICTA DE SEGURIDAD):
Si el usuario pregunta algo que NO tiene absolutamente nada que ver con programación, tecnología o el perfil profesional de Santiago (ej: recetas, clima, chistes, etc.), DEBES rechazar la pregunta y responder EXACTAMENTE con el siguiente formato:
"🤖 Bip bop... Mi sistema indica que esto está fuera de mi dominio profesional. Sin embargo, te puedo contar un secreto: {secreto_random} ¡Pero volvamos a la tecnología! ¿Qué te gustaría saber sobre su experiencia en TCS o sus certificaciones?"
"""

        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_PROMPT
        )
        
        response = model.generate_content(request.message)
        return {"response": response.text}

    except Exception as e:
        print(f"Error en la IA: {e}")
        raise HTTPException(status_code=500, detail="El cerebro del bot está descansando.")