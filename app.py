from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

tarefas = []
id_counter = 1

# GET - Listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    """Retorna todas as tarefas."""
    return jsonify(tarefas), 200

# GET - Buscar tarefa por ID
@app.route('/tarefas/<int:tarefa_id>', methods=['GET'])
def buscar_tarefa(tarefa_id):
    """Retorna uma tarefa específica."""
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            return jsonify(tarefa), 200
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# POST - Criar nova tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    """Cria uma nova tarefa."""
    global id_counter
    
    dados = request.get_json()
    
    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'Título é obrigatório'}), 400
    
    nova_tarefa = {
        'id': id_counter,
        'titulo': dados['titulo'],
        'descricao': dados.get('descricao', ''),
        'concluida': False,
        'data_criacao': datetime.now().isoformat()
    }
    
    tarefas.append(nova_tarefa)
    id_counter += 1
    
    return jsonify(nova_tarefa), 201

# PUT - Atualizar tarefa
@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    """Atualiza uma tarefa existente."""
    dados = request.get_json()
    
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['titulo'] = dados.get('titulo', tarefa['titulo'])
            tarefa['descricao'] = dados.get('descricao', tarefa['descricao'])
            tarefa['concluida'] = dados.get('concluida', tarefa['concluida'])
            
            return jsonify(tarefa), 200
    
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# DELETE - Deletar tarefa
@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    """Deleta uma tarefa."""
    for i, tarefa in enumerate(tarefas):
        if tarefa['id'] == tarefa_id:
            tarefas.pop(i)
            return jsonify({'mensagem': 'Tarefa deletada com sucesso'}), 200
    
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# Rota inicial
@app.route('/', methods=['GET'])
def home():
    """Rota inicial."""
    return jsonify({
        'mensagem': 'API de Tarefas - Bem-vindo!',
        'endpoints': {
            'GET /tarefas': 'Listar todas',
            'GET /tarefas/<id>': 'Buscar por ID',
            'POST /tarefas': 'Criar nova',
            'PUT /tarefas/<id>': 'Atualizar',
            'DELETE /tarefas/<id>': 'Deletar'
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
