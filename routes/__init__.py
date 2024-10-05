# routes/__init__.py
from .auth import auth_blueprint
from .users import users_blueprint

__all__ = ['auth_blueprint', 'users_blueprint']
