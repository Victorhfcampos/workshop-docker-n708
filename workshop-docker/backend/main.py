from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Workshop Docker API",
    description="API simples para cadastro e listagem de workshops",
    version="1.0.0"
)

# Liberar acesso de qualquer origem (para funcionar com frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados
class Workshop(BaseModel):
    id: int
    titulo: str
    descricao: str
    data: str

# Lista simulada como "banco de dados"
workshops_db = []

# Rota raiz
@app.get("/")
def home():
    return {"mensagem": "API do Workshop Docker está online!"}

# Listar todos os workshops
@app.get("/workshops", response_model=List[Workshop])
def listar_workshops():
    return workshops_db

# Adicionar novo workshop
@app.post("/workshops", response_model=Workshop)
def adicionar_workshop(workshop: Workshop):
    # Verifica se ID já existe
    for w in workshops_db:
        if w.id == workshop.id:
            raise HTTPException(status_code=400, detail="ID já cadastrado")
    workshops_db.append(workshop)
    return 