# 📋 API REST - TODO List

Uma API REST simples em Python com Flask para gerenciar tarefas.

## 🎯 Funcionalidades

- ✅ Listar todas as tarefas
- ✅ Buscar tarefa por ID
- ✅ Criar nova tarefa
- ✅ Atualizar tarefa
- ✅ Deletar tarefa

## 📦 Instalação

```bash
git clone https://github.com/AmynadabeLRocha/todo-api.git
cd todo-api
pip install -r requirements.txt

🚀 Como Usar

python app.py

A API estará em: http://localhost:5000

📚 Endpoints

curl http://localhost:5000/tarefas

POST /tarefas

curl -X POST http://localhost:5000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Minha tarefa", "descricao": "Descrição"}'

PUT /tarefas/<id>

curl -X PUT http://localhost:5000/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"concluida": true}'

DELETE /tarefas/<id>

curl -X DELETE http://localhost:5000/tarefas/1

🔗 Conecte-se Comigo
LinkedIn: Amynadabe L. Rocha
Instagram: @amynadabe.dev
GitHub: AmynadabeLRocha

Autor: Amynadabe L. Rocha | Versão: 1.0


