from SSIS import mysql

class Student():
    def __init__(self, id_number=None, first_name=None, last_name=None, course_code=None, year_level=None, gender=None):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.course_code = course_code
        self.year_level = year_level
        self.gender = gender

    # request student data
    @staticmethod
    def add_student(addForm, course_code, yearLevel, gender, image_url):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''
                        INSERT INTO students
                        VALUES ('{addForm["id_number"]}',
                                '{addForm["lastName"]}',
                                '{addForm["firstName"]}',
                                '{course_code}',
                                '{yearLevel}',
                                '{gender}',
                                '{image_url}')
                        ''')
            mysql.connection.commit()
            info = [1, addForm["firstName"], addForm["lastName"]]
            return info

        except Exception as e:
            info = [0, e]
            return info

    # update student data
    @staticmethod
    def update_student(updateForm, course_code, yearLevel, gender):
        cursor= mysql.connection.cursor()
        cursor.execute(f'''
                        UPDATE students
                        SET id_number='{updateForm["id_number"]}',
                            last_name='{updateForm["lastName"]}',
                            first_name='{updateForm["firstName"]}',
                            course_code='{course_code}',
                            year_level='{yearLevel}',
                            gender='{gender}'
                        WHERE id_number='{updateForm["id_number"]}'
                        ''')
        mysql.connection.commit()
        cursor.close()

    # update student photo
    @staticmethod
    def update_image(image_url, id_number):
        cur = mysql.connection.cursor()
        cur.execute(f'''
                    UPDATE students
                    SET image_url='{image_url}'
                    WHERE id_number='{id_number}'
                    ''')
        mysql.connection.commit()

    # delete student data
    @staticmethod
    def delete_student(id_number):
        cursor = mysql.connection.cursor()
        cursor.execute(f'''
                        DELETE FROM students
                        WHERE id_number='{id_number}'
                        ''')
        mysql.connection.commit()
        cursor.close()

    # get student list
    @staticmethod
    def getStudents():
        cursor = mysql.connection.cursor()
        cursor.execute('''
                       SELECT * FROM students
                       ''')
        students = cursor.fetchall()
        cursor.close()
        return students