'''

1 - OBJETIVO - api para permitir acessar, excluir , criar e editar livros

2 - URL - localhost

3 - ENDPOINTS

- localhost/livros/ id (GET)
- localhost/livros/ id (POST)
- localhost/livros/ id (PUT)
- localhost/livros/ id (DELETE)

4 - QUAIS RECURSOS - LIVROS

'''

from flask import Flask,jsonify,request

app = Flask(__name__)


livros = [

    {
    'id' : 1,
    'título' : "algebra",
    'autor' : 'xxxx'
    },

   {
    'id' : 2,
    'título' : "O mundo de norman",
    'autor' : 'xxxx'
   },

   {
        'id': 3,
        'título': "apostila de algebra",
        'autor': 'xxx'
   }
]

#consultar (todos)
@app.route('/livros',methods = ['GET'])
def obter_livros():
    return jsonify(livros)

#consultar (id)
@app.route('/livros/<int:id>',methods = ['GET'])
def obter_por_id(id):
    for elemento in livros:
        if elemento.get('id') == id:
            return jsonify(elemento)

@app.route('/livros/<int:id>',methods = ['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for índice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[índice].update(livro_alterado)
            return jsonify(livros[índice])
#criar
@app.route('/livros',methods = ['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods = ['DELETE'])
def excluir_livro(id):
    for índice, livro in enumerate(livros):
        if livro.get('id') == id:
              del livros[índice]
              return jsonify(livros)

app.run(port = 5000, host='localhost', debug= True)