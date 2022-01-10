from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mysql_connector import MySQL
import cloudinary
import cloudinary.uploader
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS, SECRET_KEY, CLOUD_NAME, API_KEY, API_SECRET

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

    cloudinary.config(
        cloud_name = CLOUD_NAME,
        api_key = API_KEY,
        api_secret = API_SECRET,
        secure = 'true'
    )

    from .homepage import home
    from .student.student import student
    from .course.course import course
    from .college.college import college

    app.register_blueprint(home)
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)


    bootstrap = Bootstrap(app)
    mysql.init_app(app)

    return app

