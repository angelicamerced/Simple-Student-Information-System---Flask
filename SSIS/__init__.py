from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mysql_connector import MySQL
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS, SECRET_KEY

mysql = MySQL()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_HOST=DB_HOST,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_USER=DB_USER,
        MYSQL_PASSWORD=DB_PASS,
    )

    from SSIS.homepage import home
    # from .student import student
    # from .course import course
    from SSIS.college.college import college

    app.register_blueprint(home)
    # app.register_blueprint(student,  url_prefix="/")
    # app.register_blueprint(course,  url_prefix="/")
    app.register_blueprint(college)


    bootstrap = Bootstrap(app)
    mysql.init_app(app)

    return app

