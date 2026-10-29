from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
produtos_bd = []


@app.route("/produtos", methods=["POST"])
def cadastrar_produtos():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria  = dados.get("categoria")
    produto ={"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    produtos_bd.append(produto)
    return jsonify(produto), 201

if __name__ == "__main__":
    app.run(debug=True)

