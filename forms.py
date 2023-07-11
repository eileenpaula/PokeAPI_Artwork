'''from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    index_poke_input = StringField('Pokemon Name', validators=[DataRequired(), Length(min=1])
    submit = SubmitField('Submit')'''