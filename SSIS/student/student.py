from flask import Blueprint, render_template, redirect, url_for, request, flash
from SSIS.student.studentForm import studentForm
import SSIS.models.studentRepo as db
import SSIS.models.courseRepo as courseRepo

student = Blueprint('student', __name__)

# Routing for Student Page

# Display Student Page
@student.route('/students')
def display_students():
    students = db.Student().getStudents()
    courses = courseRepo.Course().getCourses()
    studentform = studentForm()
    return render_template('student.html', students=students, options=courses, form=studentform)

# Add student
@student.route('/add_student', methods=['POST'])
def create_student():
    if request.method == 'POST':

        course_code = request.form['addcourse']
        yearLevel = request.form['addyear']
        gender = request.form['addgender']
        addForm = studentForm()
        db.Student.add_student(addForm.data, course_code, yearLevel, gender)
        flash("Student has been successfully added.", "success")
        return redirect(url_for('student.display_students'))

    else:
        return redirect(url_for('student.display_students'))

# Update student
@student.route('/update_student', methods=['POST'])
def edit_student():
    if request.method == 'POST':

        course_code = request.form['updatecourse']
        yearLevel = request.form['updateyear']
        gender = request.form['updategender']
        updateForm = studentForm()
        db.Student.update_student(updateForm.data, course_code, yearLevel, gender)
        flash("Student has been successfully updated.", "success")
        return redirect(url_for('student.display_students'))

    else:
        return redirect(url_for('student.display_students'))

# Delete student
@student.route('/delete_student/<string:id_number>')
def remove_student(id_number):
    db.Student.delete_student(id_number)
    flash("Student has been successfully removed.", "success")
    return redirect(url_for('student.display_students'))

