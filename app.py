from flask import Flask
from routes.auth import auth_blueprint
from routes.users import users_blueprint

app = Flask(__name__)

# Mendaftarkan blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(users_blueprint, url_prefix='/users')

# Route utama
@app.route('/')
def home():
    return 'Hello, Gaessshhh! This is the main route.'

if __name__ == '__main__':
    app.run(debug=True)
