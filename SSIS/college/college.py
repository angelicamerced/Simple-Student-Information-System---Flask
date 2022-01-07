from flask import Blueprint, render_template, redirect, url_for, request, flash
from SSIS.college.collegeForm import collegeForm
import SSIS.models.collegeRepo as db

# College blueprint
college = Blueprint('college', __name__, template_folder='templates')

# Routing for College Page

# Display College Page
@college.route('/colleges')
def display_colleges():
    colleges = db.College().getColleges()
    form = collegeForm()
    return render_template('college.html', colleges=colleges, form=form)

# Add college
@college.route('/add_college', methods=['POST'])
def create_college():
    if request.method == 'POST':

        addForm = collegeForm()
        db.College.add_college(addForm.data)
        flash("College has been successfully added.", "success")
        return redirect(url_for('college.display_colleges'))

    else:
        return redirect(url_for('college.display_colleges'))

# Update college
@college.route('/update_college', methods=['POST'])
def edit_college():
    if request.method == 'POST':

        updateForm = collegeForm()
        db.College.update_college(updateForm.data)
        flash("College information has been successfully updated!", "success")
        return redirect(url_for('college.display_colleges'))

    else:
        return redirect(url_for('college.display_colleges'))

# Delete college
@college.route('/delete_college/<string:college_code>')
def remove_college(college_code):
    db.College.delete_college(college_code)
    flash("College has been successfully removed.", "success")
    return redirect(url_for('college.display_colleges'))
