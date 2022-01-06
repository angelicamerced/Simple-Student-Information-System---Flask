from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length


class courseForm(FlaskForm):

    course_code = StringField('Course Code',
                              validators=[DataRequired(), Length(max=50)])

    course_name = StringField('Course Name',
                              validators=[DataRequired(), Length(max=100)])

    submit = SubmitField('Submit')