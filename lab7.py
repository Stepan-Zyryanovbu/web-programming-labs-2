from flask import Blueprint, render_template, abort, request, jsonify

lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def lab():
    return render_template('lab7/lab7.html')