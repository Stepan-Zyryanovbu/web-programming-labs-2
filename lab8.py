from flask import Blueprint, render_template, redirect, request
from db import db
from db.models import users,articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab8 = Blueprint('lab8', __name__)
@lab8.route('/lab8/')
def lab():
    return render_template('lab8/lab8.html')