import waitress
from flask import Flask, render_template, request

from app.ozon import create_book, add_book, search_book

import os

def start():
    app = Flask(__name__)

    container = []  # FIXME: так делать будет нельзя
    wp = create_book('Война и мир', 'Лев Толстой', 1000, ['#война', '#безухов', '#дуб'])
    anna = create_book('Анна Каренина', 'Лев Толстой', 800, ['#поезд', '#любовь'])
    potter_phoenix = create_book('Гарри Поттер и Орден Феникса', 'Джоан Роулинг', 700,
                                 ['#волшебство', '#магия', '#драконы'])
    robinson = create_book('Робинзон Крузо', 'Даниэль Дефо', 500, ['#остров', '#одиночество', '#пятница'])
    musketeers = create_book('Три мушкетера', 'Александр Дюма', 900, ['#честь', '#миледи', '#шпага'])

    container = add_book(container, wp)
    container = add_book(container, anna)
    container = add_book(container, potter_phoenix)
    container = add_book(container, robinson)
    container = add_book(container, musketeers)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            # TODO: почистить
            results = search_book(container, search)
            return render_template('index.html', books=results, search=search)

        return render_template('index.html', books=container)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
