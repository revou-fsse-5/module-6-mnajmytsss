from flask import request, jsonify

# Dummy data pengguna
dummy_users = [
    {"id": 1, "username": "administrator", "password": "admin"},
    {"id": 2, "username": "user2", "password": "password2"},
    {"id": 3, "username": "user3", "password": "password3"},
    {"id": 4, "username": "user4", "password": "password4"}
]

# Fungsi view untuk login
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    for user in dummy_users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful!', 'username': username, 'id': user['id']}), 200

    return jsonify({'message': 'Invalid username or password'}), 401

# Fungsi view untuk registrasi
def register(): 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    if any(user['username'] == username for user in dummy_users):
        return jsonify({'message': 'Username already exists!'}), 409

    new_user_id = len(dummy_users) + 1
    new_user = {
        "id": new_user_id,
        "username": username,
        "password": password
    }
    dummy_users.append(new_user)

    return jsonify({'message': 'User registered successfully!', 'username': username, 'id': new_user_id}), 201
