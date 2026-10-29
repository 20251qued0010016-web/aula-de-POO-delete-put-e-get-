from flask import Flask, request 
app=Flask (__name__)
id = 0 
filme_bd = []

@app.route("/filme", methods=["POST"])
def cadastrar_filme():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")
    filme ={"id": id, "nome": nome, "ano": ano, "diretor": diretor}
    filme_bd.append(filme)
    return jsonify(filme)

@app.route ("/filmes/<int:id>", methods = [PUT])
def editarFilmes(id):
    dados = request.get("nome")
    ano = dados.get ("ano ")
    diretor =dados.get("direitor")
    for filme in filme_db:
        if filme ["id"]== id :
           filme ["nome"] = nome 
           filme ["ano "]

