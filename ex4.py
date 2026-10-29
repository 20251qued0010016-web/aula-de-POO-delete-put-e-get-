from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
funcionario_bd = []


@app.route("/funcionario", methods=["POST"])
def cadastrar_funcionario():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    cargo = dados.get("cargo")
    salario  = dados.get("salario")
    funcionario ={"id": id, "nome": nome, "cargo": cargo, "salario": salario}
    funcionario_bd.append(funcionario)
    return jsonify(funcionario), 201

if __name__ == "__main__":
    app.run(debug=True)

