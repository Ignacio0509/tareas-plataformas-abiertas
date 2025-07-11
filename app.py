from flask import Flask, request

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def usuarios():
    user_id = request.args.get('id')  # Lee el parámetro 'id' desde la URL
    if user_id:
        return f"El id del usuario es {user_id}", 200
    else:
        return "Lista de todos los usuarios.", 200

if __name__ == '__main__':
    app.run(debug=True)
