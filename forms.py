from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CheckForm(FlaskForm):
    Step = StringField('Step:  ',validators=[DataRequired()])
    Type = StringField('Type of transaction:  ',validators=[DataRequired()])
    Amount = StringField('Amount of transaction:  ',validators=[DataRequired()])
    D_name = StringField('Name of Despositor:  ',validators=[DataRequired()])
    A_bal_before = StringField('Account balance of depositor before transaction:  ',validators=[DataRequired()])
    A_bal_after = StringField('Account balance of depositor after transaction:  ',validators=[DataRequired()])
    P_name = StringField('Name of Payee:  ',validators=[DataRequired()])
    P_bal_before = StringField('Account balance of Payee before transaction:  ',validators=[DataRequired()])
    P_bal_after = StringField('Account  balance of Payee after transaction:  ',validators=[DataRequired()])
    Submit=SubmitField('Submit')
