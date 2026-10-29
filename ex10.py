from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
curso_bd = []


@app.route("/curso", methods=["POST"])
def cadastrar_jogos():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao  = dados.get("duracao")
    curso ={"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    curso_bd.append(curso)
    return jsonify(curso), 201

if __name__ == "__main__":
    app.run(debug=True)

