from flask import Flask, render_template,request,redirect
from . import db

maine = Blueprint('main',__name__)

@maine.route('/')
def home():
    return render_template('layout.html')

@maine.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass
    return render_template('register.html')

@maine.route('/properties')
def view_properties():
    properties = Property.query.all()
    return render_template('properties.html',properties=properties)