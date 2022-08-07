from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Employee Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone_no = IntegerField('Phone No',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    creation_date = StringField('CreationDate', validators=[DataRequired()])
    created_by = StringField('Created By',
                           validators=[DataRequired(), Length(min=2, max=20)])
    updation_date = StringField('Updation Date')
    updated_by = StringField('Updated By',
                             validators=[Length(min=2, max=20)])
    
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    is_active = BooleanField('isActive')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')