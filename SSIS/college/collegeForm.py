from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length
from SSIS.models.collegeRepo import College


class collegeForm(FlaskForm):

    college_code = StringField('College Code',
                              validators=[DataRequired(), Length(max=50)])

    college_name = StringField('College Name',
                              validators=[DataRequired(), Length(max=100)])

    submit = SubmitField('Submit')

    def validate_college_code(self, college_code):
        cc = College.collegebyCode(college_code.data)
        if cc:
            raise validators.ValidationError('College code already taken.')