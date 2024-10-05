from flask import Blueprint
from views.auth import login, register

# Buat Blueprint untuk auth
auth_blueprint = Blueprint('auth', __name__)

# Rute login
auth_blueprint.route('/login', methods=['POST'])(login)

# Rute registrasi
auth_blueprint.route('/register', methods=['POST'])(register)
