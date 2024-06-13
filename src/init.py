from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'many random bytes'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'admin123'
    app.config['MYSQL_DB'] = 'DATABASE_PRINC'

    mysql.init_app(app)

    from .routes.routes import init_routes

    init_routes(app)

    return app
