from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required, current_user

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def lab():
    return render_template('lab9/lab9.html')

@lab9.route('/lab9/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('lab9.age'))
    return render_template('lab9/name.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('lab9.gender'))
    return render_template('lab9/age.html')

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')
        return redirect(url_for('lab9.preference1'))
    return render_template('lab9/gender.html')

@lab9.route('/lab9/preference1', methods=['GET', 'POST'])
def preference1():
    if request.method == 'POST':
        session['preference1'] = request.form.get('preference1')
        return redirect(url_for('lab9.preference2'))
    return render_template('lab9/preference1.html')

@lab9.route('/lab9/preference2', methods=['GET', 'POST'])
def preference2():
    if request.method == 'POST':
        session['preference2'] = request.form.get('preference2')
        return redirect(url_for('lab9.result'))
    return render_template('lab9/preference2.html')

@lab9.route('/lab9/result')
def result():
    name = session.get('name')
    age = int(session.get('age'))
    gender = session.get('gender')
    preference1 = session.get('preference1')
    preference2 = session.get('preference2')

    
    if age < 18:
        if gender == 'man':
            greeting = f"Поздравляю тебя, {name}, желаю, чтобы ты нашел свое призвание в этой жизни!"
        else:
            greeting = f"Поздравляю тебя, {name}, желаю, чтобы ты нашла свое призвание в этой жизни!"
    else:
        if gender == 'woman':
            greeting = f"Поздравляю вас, {name}, желаю счастья, терпения и стабильного ментального здоровья!"
        else:
            greeting = f"Поздравляю вас, {name}, желаю счастья, терпения и стабильного ментального здоровья!"

    if preference1 == 'tasty':
        if preference2 == 'sweet':
            image = 'sweet.jpg'
            gift = "Вот тебе подарок — мешочек конфет!"
        else:
            image = 'meal.jpg'
            gift = "Вот тебе подарок — новогодний ужин!"
    else:
        if preference2 == 'decor':
            image = 'decor.jpg'
            gift = "Вот тебе подарок — новогодние украшения!"
        else:
            image = 'tree.jpg'
            gift = "Вот тебе подарок — новогодняя елка!"

    return render_template('lab9/result.html', greeting=greeting, image=image, gift=gift)

