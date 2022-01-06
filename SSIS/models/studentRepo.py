from config import DB_NAME, DB_HOST, DB_PASS, DB_USER
import mysql.connector

connection = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASS,
    database = DB_NAME
)

class Student():
    def __init__(self, id_number=None, first_name=None, last_name=None, course_code=None, year_level=None, gender=None):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.course_code = course_code
        self.year_level = year_level
        self.gender = gender

    def add_student(self, id_number):
        cursor = connection.cursor()
        cursor.execute('''SELECT COUNT(*) FROM students WHERE id_number=%s''', (id_number,))
        exist = cursor.fetchone()
        cursor.close()
        return exist

    def update_student(id_number, first_name, last_name, course_code, year_level, gender):
        cursor = connection.cursor()
        cursor.execute('''UPDATE students SET first_name=%s, last_name=%s, course_code=%s, year_level=%s, gender=%s WHERE id_number=%s''', (first_name, last_name, course_code, year_level, gender, id_number))
        connection.commit()
        cursor.close()

    def getbyID(self, id_number):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE id_number=%s", (id_number,))
        byID = cursor.fetchall()
        print(byID[0])
        cursor.close()
        return byID

    @classmethod
    def delete_student(cls, id_number):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id_number=%s", (id_number,))
        connection.commit()
        cursor.close()

    def all(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY id_number")
        students = cursor.fetchall()
        cursor.close()
        return students

    def options(self):
        cursor = connection.cursor()
        cursor.execute("SELECT course_code FROM students UNION SELECT course_code FROM courses ORDER BY course_code")
        options = cursor.fetchall()
        cursor.close()
        return options