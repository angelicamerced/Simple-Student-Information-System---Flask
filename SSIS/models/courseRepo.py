from config import DB_NAME, DB_HOST, DB_PASS, DB_USER
import mysql.connector

connection = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASS,
    database = DB_NAME
)

class Course():
    def __init__(self, course_code=None, course_name=None, college_code=None):
        self.course_code = course_code
        self.course_name = course_name
        self.college_code = college_code

    def add_course(self, course_code):
        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM courses WHERE course_code=%s''', (course_code,))
        exist = cursor.fetchone()
        cursor.close()
        return exist

    @classmethod
    def update_course(cls, course_code, course_name, college_code):
        cursor = connection.cursor()
        cursor.execute('''UPDATE courses SET course_name=%s, college_code=%s WHERE course_code=%s''', (course_name, college_code, course_code))
        connection.commit()
        cursor.close()

    @classmethod
    def delete_course(cls, course_code):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM courses WHERE course_code=%s", (course_code,))
        connection.commit()
        cursor.close()

    def all(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM courses ORDER BY college_code")
        courses = cursor.fetchall()
        cursor.close()
        return courses

    def options(self):
        cursor = connection.cursor()
        cursor.execute('''SELECT college_code FROM courses UNION SELECT college_code FROM colleges ORDER BY college_code ''')
        options = cursor.fetchall()
        cursor.close()
        return options
