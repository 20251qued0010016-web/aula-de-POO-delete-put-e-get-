from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
musica_bd = []


@app.route("/musica", methods=["POST"])
def cadastrar_musica():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano  = dados.get("ano")
    musica ={"id": id, "nome": nome, "artista": artista, "ano": ano}
    musica_bd.append(musica)
    return jsonify(musica), 201


if __name__ == "__main__":
    app.run(debug=True)

