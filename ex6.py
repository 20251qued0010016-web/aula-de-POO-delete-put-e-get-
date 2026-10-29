from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
carros_bd = []


@app.route("/carros", methods=["POST"])
def cadastrar_carros():
    global id 
    id = id +1
    dados =request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano  = dados.get("ano")
    carros ={"id": id, "modelo": modelo, "marca": marca, "ano": ano}
    carros_bd.append(carros)
    return jsonify(carros), 201

if __name__ == "__main__":
    app.run(debug=True)

