from SSIS import mysql

class Course():
    def __init__(self, course_code=None, course_name=None, college_code=None):
        self.course_code = course_code
        self.course_name = course_name
        self.college_code = college_code

    # filter course data
    @staticmethod
    def coursebyCode(course_code):
        cursor = mysql.connection.cursor()
        cursor.execute(f'''
                       SELECT * FROM courses
                       WHERE course_code=%s
                       ''', (course_code,))
        exist = cursor.fetchone()
        cursor.close()
        return exist

    # request course data
    @staticmethod
    def add_course(addForm, college_code):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(f'''
                            INSERT INTO courses
                            VALUES ('{addForm['course_code']}',
                                    '{addForm['course_name']}',
                                    '{college_code}')
                            ''')
            mysql.connection.commit()
            info = [1, addForm["course_name"]]
            return info

        except Exception as e:
            info = [0, e]
            return info

    # update course data
    @staticmethod
    def update_course(updateForm, college_code):
        cursor= mysql.connection.cursor()
        cursor.execute(f'''
                        UPDATE courses
                        SET course_code='{updateForm["course_code"]}',
                            course_name='{updateForm["course_name"]}',
                            college_code='{college_code}'
                        WHERE course_code='{updateForm["course_code"]}'
                        ''')
        mysql.connection.commit()
        cursor.close()

    # delete course data
    @staticmethod
    def delete_course(course_code):
        cursor = mysql.connection.cursor()
        cursor.execute(f'''
                        DELETE FROM courses
                        WHERE course_code='{course_code}'
                        ''')
        mysql.connection.commit()
        cursor.close()

    # get course list
    @staticmethod
    def getCourses():
        cursor = mysql.connection.cursor()
        cursor.execute('''
                       SELECT * FROM courses
                       ''')
        courses = cursor.fetchall()
        cursor.close()
        return courses
