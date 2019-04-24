from app.ozon import create_book, add_book, search_book


# def test_create_book():
#     assert {'title': 'Война и мир', 'author': 'Лев Толстой', 'price': 1000,
#             'tags': ['#война', '#безухов', '#дуб']} == create_book('Война и мир', 'Лев Толстой', 1000,
#                                                                    ['#война', '#безухов', '#дуб'])


def test_add_book():
    data = []
    expected = [
        {'title': 'Война и мир', 'author': 'Лев Толстой', 'price': 1000, 'tags': ['#война', '#безухов', '#дуб']}, ]
    actual = add_book(data, {'title': 'Война и мир', 'author': 'Лев Толстой', 'price': 1000,
                             'tags': ['#война', '#безухов', '#дуб']})
    assert expected == actual


def test_search_book_by_title():
    data = [{'title': 'Война', 'author': 'Толстой', 'price': 1, 'tags': ['#война', '#дуб']},
            {'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 800, 'tags': ['#поезд', '#любовь']}]
    expected = [{'title': 'Война', 'author': 'Толстой', 'price': 1, 'tags': ['#война', '#дуб']}]
    actual = search_book(data, 'Война')
    assert expected == actual


def test_search_book_by_author():
    data = [{'title': 'Робинзон Крузо', 'author': 'Даниэль Дефо', 'price': 1, 'tags': ['#остров', '#одиночество']},
            {'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 800, 'tags': ['#поезд', '#любовь']}]
    expected = [{'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 800, 'tags': ['#поезд', '#любовь']}]
    actual = search_book(data, 'Толстой')
    assert expected == actual


def test_search_book_by_tags():
    data = [{'title': 'Робинзон Крузо', 'author': 'Даниэль Дефо', 'price': 1, 'tags': ['#остров', '#одиночество']},
            {'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 800, 'tags': ['#поезд', '#любовь']}]
    expected = [{'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 800, 'tags': ['#поезд', '#любовь']}]
    actual = search_book(data, '#любовь')
    assert expected == actual
