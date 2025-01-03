from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2')
def lab_2():
    return render_template('lab2.html')

@lab2.route('/lab2/example')
def example():
    name = 'Зырянов Степан'
    tittlename = 'Зырянов Степан'
    group = 'ФБИ-24'
    course = '3 курс'
    r1 = (11 * 28)
    r2 = (3258 - 759)
    r3 = (8452 / 793)
    r4 = (458 ** 2)
    fruits = [
        {'name': 'яблоки','price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
        ]
    return render_template('example.html', name=name, group=group, course=course, r1=r1, r2=r2, r3=r3, r4=r4, tittlename=tittlename, fruits=fruits)

@lab2.route('/lab2/a/')
def a():
    return 'со слэшем'

@lab2.route('/lab2/a')
def a2():
    return 'без слэша'
    
flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if 0 <= flower_id < len(flower_list):
        flower = flower_list[flower_id]
        return f'''
        <!doctype html>
        <html>
            <body>
                <h1>Цветок №{flower_id + 1}</h1>
                <p>Название цветка: {flower}</p>
                <a href="/lab2/flowers">Посмотреть все цветы</a>
            </body>
        </html>
        '''
    else:
        return "<h1>Цветок не найден!</h1>", 404

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
    <!doctype html>
    <html>
        <body>
            <h1>Список цветов очищен</h1>
            <a href="/lab2/flowers">Посмотреть все цветы</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/add_flower/')
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    if not name:
        return "<h1>Ошибка 400: вы не задали имя цветка</h1>", 400
    flower_list.lab2end(name)
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Добавлен новый цветок</h1>
            <p>Название нового цветка: {name}</p>
            <p>Всего цветов: {len(flower_list)}</p>
            <p>Полный список: {', '.join(flower_list)}</p>
            <a href="/lab2/flowers">Посмотреть все цветы</a>
        </body>
    </html>
    '''
@lab2.route('/lab2/flowers')
def all_flowers():
    flower_list_html = ''.join(f'<li>{flower}</li>' for flower in flower_list)
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Все цветы</h1>
            <ul>{flower_list_html}</ul>
            <p>Всего цветов: {len(flower_list)}</p>
            <a href="/menu">Главное меню</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/')
def lab2_home():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    summation = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "На ноль делить нельзя"
    exponentiation = a ** b
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Результаты операций с числами {a} и {b}</h1>
            <p>Сумма: {a} + {b} = {summation}</p>
            <p>Вычитание: {a} - {b} = {subtraction}</p>
            <p>Умножение: {a} * {b} = {multiplication}</p>
            <p>Деление: {a} / {b} = {division}</p>
            <p>Возведение в степень: {a} ** {b} = {exponentiation}</p>
            <a href="/lab2/calc/1/1">Вернуться к значениям по умолчанию (1, 1)</a>
        </body>
    </html>
    '''

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))

@lab2.route('/lab2/calc/<int:a>')
def calc_with_one_param(a):
    return redirect(url_for('calc', a=a, b=1))

books = [
    {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'антиутопия', 'pages': 328},
    {'author': 'Федор Достоевский', 'title': 'Преступление и наказание', 'genre': 'роман', 'pages': 671},
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'исторический роман', 'pages': 1225},
    {'author': 'Дж. Р. Р. Толкин', 'title': 'Властелин колец', 'genre': 'фэнтези', 'pages': 1137},
    {'author': 'Рей Брэдбери', 'title': '451 градус по Фаренгейту', 'genre': 'фантастика', 'pages': 249},
    {'author': 'Джоан Роулинг', 'title': 'Гарри Поттер и философский камень', 'genre': 'фэнтези', 'pages': 223},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'роман', 'pages': 470},
    {'author': 'Эрнест Хемингуэй', 'title': 'Старик и море', 'genre': 'повесть', 'pages': 127},
    {'author': 'Габриэль Гарсиа Маркес', 'title': 'Сто лет одиночества', 'genre': 'магический реализм', 'pages': 417},
    {'author': 'Франц Кафка', 'title': 'Процесс', 'genre': 'экзистенциальная проза', 'pages': 224}
]

@lab2.route('/lab2/books')
def books_list():
    return render_template('books.html', books=books)

# Список ягод с их изображениями и описаниями
berries = [
    {'name': 'Клубника', 'image': 'strawberry.jpg', 'description': 'Клубника — это сочная красная ягода, популярная в десертах и компотах.'},
    {'name': 'Малина', 'image': 'raspberry.jpg', 'description': 'Малина — сладкая ягода с мелкими косточками, часто используется для джемов и варений.'},
    {'name': 'Черника', 'image': 'blueberry.jpg', 'description': 'Черника — маленькие синие ягоды, известные своим вкусом и полезными свойствами.'},
    {'name': 'Смородина', 'image': 'currant.jpg', 'description': 'Смородина — кислые ягоды, которые часто используются в выпечке и напитках.'},
    {'name': 'Ежевика', 'image': 'blackberry.jpg', 'description': 'Ежевика — черные ягоды, которые прекрасно подходят для варенья и соусов.'}
]

@lab2.route('/lab2/berries')
def berries_list():
    return render_template('berries.html', berries=berries)
