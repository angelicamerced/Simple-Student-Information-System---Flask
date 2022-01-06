from config import DB_NAME, DB_HOST, DB_PASS, DB_USER
import mysql.connector

connection = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASS,
    database = DB_NAME
)

class College():
    def __init__(self, college_code=None, college_name=None):
            self.college_code = college_code
            self.college_name = college_name

    # filter college data
    @staticmethod
    def collegebyCode(college_code):
        cursor = connection.cursor()
        cursor.execute(f'''
                       SELECT * FROM colleges
                       WHERE college_code=%s
                       ''', (college_code,))
        exist = cursor.fetchone()
        cursor.close()
        return exist

    # request college data
    @staticmethod
    def add_college(addForm):
        cursor = connection.cursor()
        cursor.execute(f'''
                        INSERT INTO colleges
                        VALUES ('{addForm['college_code']}',
                                '{addForm['college_name']}')
                        ''')
        connection.commit()
        data = [1, addForm['college_name']]
        return data

    # update college data
    @staticmethod
    def update_college(updateForm):
        cursor= connection.cursor()
        cursor.execute(f'''
                        UPDATE colleges
                        SET college_code='{updateForm["college_code"]}',
                            college_name='{updateForm["college_name"]}'
                        WHERE college_code='{updateForm["college_code"]}'
                        ''')
        connection.commit()
        cursor.close()

    # delete college data
    @staticmethod
    def delete_college(college_code):
        cursor = connection.cursor()
        cursor.execute(f'''
                        DELETE FROM colleges
                        WHERE college_code='{college_code}'
                        ''')
        connection.commit()
        cursor.close()

    # get college list
    @staticmethod
    def getColleges():
        cursor = connection.cursor()
        cursor.execute('''
                       SELECT * FROM colleges
                       ''')
        colleges = cursor.fetchall()
        cursor.close()
        return colleges