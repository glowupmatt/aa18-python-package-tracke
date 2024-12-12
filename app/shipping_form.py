from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

class ShippingForm(FlaskForm):
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    recipient_name = StringField('Recipient Name', validators=[DataRequired()])
    origin = SelectField('Origin', choices=[(key, key) for key in map.keys()], validators=[DataRequired()])
    destination = SelectField('Destination', choices=[(key, key) for key in map.keys()], validators=[DataRequired()])
    express_shipping = BooleanField('Express Shipping')
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')