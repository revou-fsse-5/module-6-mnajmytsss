from flask import Blueprint
from views.users import get_users, get_user_by_id

# Buat Blueprint untuk users
users_blueprint = Blueprint('users', __name__)

# Rute untuk mendapatkan semua pengguna
users_blueprint.route('/', methods=['GET'])(get_users)

# Rute untuk mendapatkan pengguna berdasarkan ID
users_blueprint.route('/<int:user_id>', methods=['GET'])(get_user_by_id)
