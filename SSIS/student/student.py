from flask import Blueprint, render_template, redirect, url_for, request, flash
from SSIS.student.studentForm import studentForm
import SSIS.models.studentRepo as db
import SSIS.models.courseRepo as courseRepo
import cloudinary, cloudinary.uploader

student = Blueprint('student', __name__)

# Routing for Student Page

# Display Student Page
@student.route('/students')
def display_students():
    students = db.Student().getStudents()
    courses = courseRepo.Course().getCourses()
    studentform = studentForm()

    print(students)
    return render_template('student.html', students=students, options=courses, form=studentform)

# Add student
@student.route('/add_student', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':

        course_code = request.form['addcourse']
        yearLevel = request.form['addyear']
        gender = request.form['addgender']
        addForm = studentForm()

        image_url = ''
        if addForm.image_file.data:
            image_url = upload_image(addForm.image_file.data)

        info = db.Student.add_student(addForm.data, course_code, yearLevel, gender, image_url)

        if 1 in info:
            flash(f"'{info[1]} {info[2]}'has been successfully added.", "success")
        else:
            flash(f"{info[1]}", "error")

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

# Upload to cloudinary
def upload_image(image):
    uploadResult = cloudinary.uploader.upload(image, folder="ssis-images",
                                              eager=[{"width": 50, "height": 50, "crop": "fill"}])

    # return full image and thumbnail URLs
    return uploadResult['secure_url']
