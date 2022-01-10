from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length

class studentForm(FlaskForm):

    id_number = StringField('ID Number',
                           validators=[DataRequired(), Length(max=9)])

    lastName = StringField('Last Name',
                           validators=[DataRequired(), Length(max=100)])

    firstName = StringField('First Name',
                            validators=[DataRequired(), Length(max=100)])

    image_file = FileField('Profile Picture',
                        validators=[FileAllowed('image')])

    submit = SubmitField('Submit')