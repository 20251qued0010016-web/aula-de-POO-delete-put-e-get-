from flask import Flask, request, jsonify
app=Flask (__name__)
id = 0 
alunos_bd = []


@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():
    global id 
    id = id +1
    dados =request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade  = dados.get("idade")
    aluno ={"id": id, "nome": nome, "curso": curso, "idade": idade}
    alunos_bd.append(aluno)
    return jsonify(aluno), 201

if __name__ == "__main__":
    app.run(debug=True)
