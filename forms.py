from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired(),NumberRange(min=1,max=None,message="quantity must be 1 or more")])
    description = StringField('description', validators=[DataRequired()])

