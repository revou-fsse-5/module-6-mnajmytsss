from flask import jsonify

# Dummy data pengguna
dummy_users = [
    {"id": 1, "username": "administrator", "password": "admin"},
    {"id": 2, "username": "user2", "password": "password2"},
    {"id": 3, "username": "user3", "password": "password3"},
    {"id": 4, "username": "user4", "password": "password4"}
]

# Fungsi view untuk mendapatkan semua pengguna
def get_users():
    return jsonify(dummy_users), 200

# Fungsi view untuk mendapatkan pengguna berdasarkan ID
def get_user_by_id(user_id):
    user = next((user for user in dummy_users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found!'}), 404
