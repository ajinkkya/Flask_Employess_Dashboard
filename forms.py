from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
    username = StringField('Employee Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone_no = IntegerField('Phone No',
                           validators=[DataRequired(), Length(min=10, max=13)])
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


class EmployeeDetailsForm(FlaskForm):
    emp_id = StringField('emp_id',
                           validators=[DataRequired()])
    emp_address = StringField('emp_address',
                           validators=[DataRequired(), Length(min=20, max=150)])
    emp_joining_date = StringField('Joining Date')
    emp_resigning_date = StringField('Resigning Date')
    emp_prev_company = StringField('Employyees Previous Company')
    emp_joining_salary = StringField('emp_joining_salary', validators=[DataRequired()])
    emp_current_salary = StringField('emp_current_salary', validators=[DataRequired()])
    emp_adhaar_no = StringField('emp_adhaar_no', validators=[Length(min=12, max=12)])
    submit = SubmitField('Save Employee Details')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')