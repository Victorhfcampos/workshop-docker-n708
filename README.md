# workshop-docker-n708
Aplicação web para cadastro de workshops com backend em FastAPI e frontend HTML5/JS

# Workshop Docker para Iniciantes

Projeto desenvolvido para a disciplina **N708 – Projeto Aplicado Multiplataforma (Parte 2)** da UNIFOR.

O objetivo foi criar uma aplicação web funcional e multiplataforma que simula o cadastro e listagem de workshops sobre Docker, com base em uma atividade extensionista já realizada com alunos do ensino médio técnico.

---

## 🔧 Tecnologias Utilizadas

- **Linguagem:** Python 3.9
- **Backend:** FastAPI
- **Frontend:** HTML5 + Bootstrap 5 + JavaScript
- **Execução local:** Uvicorn
- **Outras ferramentas:** Swagger, VS Code

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/workshop-docker.git
cd workshop-docker

### 2. Instale as dependências
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn

### 3. Rode o servidor FastAPI
uvicorn main:app --reload

Acesse a documentação Swagger no link gerado

Vá para o seu código front-end, abra o arquivo index.html no navegador
