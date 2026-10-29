from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
restaurante_bd = []


@app.route("/restaurante", methods=["POST"])
def cadastrar_restaurante():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade  = dados.get("cidade")
    restaurante ={"id": id, "nome": nome, "tipo": tipo, "cidade": cidade}
    restaurante_bd.append(restaurante)
    return jsonify(restaurante), 201

if __name__ == "__main__":
    app.run(debug=True)

