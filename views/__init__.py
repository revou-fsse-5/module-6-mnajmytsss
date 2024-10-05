# views/__init__.py
from .auth import login, register
from .users import get_users, get_user_by_id

__all__ = ['login', 'register', 'get_users', 'get_user_by_id']
