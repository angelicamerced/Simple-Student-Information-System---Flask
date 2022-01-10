from flask import Blueprint, render_template, redirect, url_for, request, flash
from SSIS.course.courseForm import courseForm
import SSIS.models.courseRepo as db
import SSIS.models.collegeRepo as collegeRepo

course = Blueprint('course', __name__)

# Routing for Course Page

# Display Course Page
@course.route('/courses')
def display_courses():
    courses = db.Course().getCourses()
    colleges = collegeRepo.College().getColleges()
    courseform = courseForm()
    return render_template('course.html', courses=courses, options=colleges, form=courseform)

# Add course
@course.route('/add_course', methods=['POST'])
def create_course():
    if request.method == 'POST':

        college_code = request.form['addcollege']
        addForm = courseForm()
        info = db.Course.add_course(addForm.data,college_code)

        if 1 in info:
            flash(f"'{info[1]}'has been successfully added.", "success")
        else:
            flash(f"{info[1]}", "error")

        return redirect(url_for('course.display_courses'))

    else:
        return redirect(url_for('course.display_courses'))

# Update course
@course.route('/update_course', methods=['POST'])
def edit_course():
    if request.method == 'POST':

        college_code = request.form['updatecollege']
        updateForm = courseForm()
        db.Course.update_course(updateForm.data, college_code)
        flash("Course has been successfully updated!", "success")
        return redirect(url_for('course.display_courses'))

    else:
        return redirect(url_for('course.display_courses'))

# Delete course
@course.route('/delete_course/<string:course_code>')
def remove_course(course_code):
    db.Course.delete_course(course_code)
    flash("Course has been successfully removed.", "success")
    return redirect(url_for('course.display_courses'))
