from flask import Blueprint, render_template, redirect, request
from db import db
from werkzeug.security import check_password_hash, generate_password_hash

lab8 = Blueprint('lab8', __name__)
@lab8.route('/lab8/')
def lab():
    return render_template('lab8/lab8.html')