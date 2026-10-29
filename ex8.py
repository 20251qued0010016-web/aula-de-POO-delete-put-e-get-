from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
jogos_bd = []


@app.route("/jogos", methods=["POST"])
def cadastrar_jogos():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano  = dados.get("ano")
    jogos ={"id": id, "nome": nome, "genero": genero, "ano": ano}
    jogos_bd.append(jogos)
    return jsonify(jogos), 201

if __name__ == "__main__":
    app.run(debug=True)

