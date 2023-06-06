from flask import Flask, request
from user import User

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        if not request.is_json:
            return {"message": "Missing JSON in request"}, 400
        user = User.create(request.json)
        return user.json(), 201
    else:
        return User.get_all(), 200

@app.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    user = User.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    if request.method == 'GET':
        return user.json(), 200
    elif request.method == 'PUT':
        user.update(request.json)
        return user.json(), 200
    elif request.method == 'DELETE':
        user.delete()
        return '', 204

if __name__ == "__main__":
    app.run(debug=True)