from flask import Blueprint, redirect, url_for, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name') or 'аноним'
    age = request.cookies.get('age') or 'неизвестен'
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, age=age, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie() :
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie( 'name_color' )
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей.
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара - на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get ('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')  # Получение стоимости из параметра
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    
    # Создаем ответ с редиректом, чтобы установить cookies
    resp = make_response(redirect('/lab3/settings'))
    
    # Устанавливаем cookies для цвета текста, цвета фона и размера шрифта, если они заданы
    if color:
        resp.set_cookie('color', color)
    if bg_color:
        resp.set_cookie('bg_color', bg_color)
    if font_size:
        resp.set_cookie('font_size', font_size)
    
    # Если нет новых параметров, загружаем страницу с текущими значениями cookies
    if not (color or bg_color or font_size):
        color = request.cookies.get('color')
        bg_color = request.cookies.get('bg_color')
        font_size = request.cookies.get('font_size')
        resp = make_response(render_template('lab3/settings.html', color=color, bg_color=bg_color, font_size=font_size))
    
    return resp


@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def train_ticket():
    if request.method == 'POST':
        # Получение данных из формы
        full_name = request.form.get('full_name')
        seat = request.form.get('seat')
        bed = 'bed' in request.form
        luggage = 'luggage' in request.form
        age = int(request.form.get('age', 0))
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        travel_date = request.form.get('travel_date')
        insurance = 'insurance' in request.form

        # Проверка на пустые поля
        if not all([full_name, seat, departure, destination, travel_date]) or age < 1 or age > 120:
            return render_template('lab3/train_ticket_form.html', error="Все поля обязательны и возраст должен быть от 1 до 120.")

        # Расчет стоимости билета
        price = 700 if age < 18 else 1000  # Детский или взрослый билет
        if seat in ['lower', 'side_lower']:
            price += 100
        if bed:
            price += 75
        if luggage:
            price += 250
        if insurance:
            price += 150

        # Определение типа билета
        ticket_type = "Детский билет" if age < 18 else "Взрослый билет"

        # Передача данных в шаблон результата
        return render_template('lab3/ticket_result.html', full_name=full_name, age=age,
                               ticket_type=ticket_type, seat=seat, departure=departure,
                               destination=destination, travel_date=travel_date, price=price)

    # Если метод GET, просто рендерим форму
    return render_template('lab3/train_ticket_form.html')




