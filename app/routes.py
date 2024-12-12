from flask import Blueprint, render_template, redirect, url_for
from .shipping_form import ShippingForm 
from .model import db, Package

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return 'Home Page'


@bp.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        package = Package(
            sender_name=form.sender_name.data,
            recipient_name=form.recipient_name.data,
            origin=form.origin.data,
            destination=form.destination.data,
            express_shipping=form.express_shipping.data
        )
        print(package.to_dict())
        db.session.add(package)
        db.session.commit()
        return redirect(url_for('routes.home'))
    return render_template('shipping_request.html', form=form)