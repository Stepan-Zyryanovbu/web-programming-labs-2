from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1")
def lab():
    return """
<!doctype html>
<html>
    <head>
        <title>Зырянов Степан Павлович, Лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='Lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Flask — фреймворк для создания веб-приложений на языке программирования Python</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>

        <p><a href="/menu">Вернуться в меню</a></p>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/oak">Роут с дубом</a></li>
            <li><a href="/lab1/student">Роут студента</a></li>
            <li><a href="/lab1/python">Роут про Python</a></li>
            <li><a href="/lab1/drift">Роут про зимний дрифт</a></li>
        </ul>

        <footer>
            &copy; Зырянов Степан Павлович, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """

@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/Lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='lab1/oak.jpg') + '''">
    </body>
</html>
'''

@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/Lab1.css') + '''">
    </head>
    <body>
        <h1>Студент: Зырянов Степан Павлович</h1>
        <img src="''' + url_for('static', filename='lab1/nstu.jpg') + '''" alt="НГТУ лого">
    </body>
</html>
'''

@lab1.route('/lab1/python')
def python_info():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/Lab1.css') + '''">
    </head>
    <body>
        <h1>Про язык программирования Python</h1>
        <p>Python — это высокоуровневый язык программирования общего назначения, который известен своей читабельностью и простотой. Создан в 1991 году Гвидо ван Россумом.</p>
        <p>Python поддерживает несколько парадигм программирования, включая объектно-ориентированное, процедурное и функциональное программирование. Он широко используется в разработке веб-приложений, анализа данных, искусственного интеллекта и автоматизации.</p>
        <p>Благодаря огромному количеству библиотек, таких как Django, Flask, Pandas, и NumPy, Python стал одним из самых популярных языков программирования в мире.</p>
        <img src="''' + url_for('static', filename='lab1/python.jpg') + '''" alt="Python лого">
    </body>
</html>
'''

@lab1.route('/lab1/drift')
def drift():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1/Lab1.css') + '''">
    </head>
    <body>
        <h1>Зимний дрифт на Жигулях</h1>
        <p>Зимний дрифт на классических автомобилях Жигули — это захватывающее развлечение, которое стало популярным в России. Благодаря особенностям зимнего вождения и недостаточной управляемости заднеприводных автомобилей на скользкой дороге, дрифт становится и опасным, и интересным одновременно.</p>
        <p>Многие энтузиасты выбирают именно Жигули для дрифта, так как этот автомобиль доступен по цене и легко поддается доработкам. Дрифт на льду требует мастерства, но приносит массу удовольствия и зрелищности для наблюдателей.</p>
        <p>Проводятся даже специальные соревнования по зимнему дрифту, где автомобилисты демонстрируют свое мастерство и управление на льду.</p>
        <img src="''' + url_for('static', filename='lab1/dftz.jpg') + '''" alt="Зимний дрифт">
    </body>
</html>
'''