import waitress
from flask import Flask, render_template, request, url_for, redirect

from app.ozon import create_book, add_book, search_book, create_empty_book, search_book_by_id, remove_book_by_id, update_book

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
            results = search_book(container, search)
            return render_template('index.html', books=results, search=search)
        return render_template('index.html', books=container)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        nonlocal container
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        tags = request.form['tags']
        if book_id == 'new':
            book = create_book(title=title, author=author, price=price, tags=tags)
            container = add_book(container, book)
        else:
            book = search_book_by_id(container, book_id)
            update_book(book, title=title, author=author, price=price, tags=tags)
            # pass  # TODO: сохранить измения
        return redirect(url_for('book_details', book_id=book['id']))

    @app.route('/books/<book_id>/edit')  # id = 0, новый объект, id <> 0 - существующий
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()
        else:
            book = search_book_by_id(container, book_id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<book_id>/remove', methods=['POST'])  # routing, mapping url -> конкретной функцией
    def book_remove(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9875, debug=True)


if __name__ == '__main__':
    start()
