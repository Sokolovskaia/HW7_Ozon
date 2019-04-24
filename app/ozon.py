import uuid


def create_book(title, author, price, tags):
    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'price': price,
        'tags': tags,
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def create_empty_book():
    return {
        'id': str(uuid.uuid4()),
        'title': '',
        'author': '',
        'price': '',
        'tags': '',
    }


def update_book(book, title, author, price, tags):
    book['title'] = title
    book['author'] = author
    book['price'] = price
    book['tags'] = tags


def search_book(container, title):
    title_lowercased = title.strip().lower()
    result = []
    result_tm = []
    for book in container:
        if title_lowercased in book['title'].lower():
            result.append(book)
            continue

        elif title_lowercased in book['author'].lower():
            result.append(book)
            continue

        for tag in book['tags']:
            if title_lowercased in tag:
                result_tm.append(book)
        for book in result_tm:                        # удаляем дубликаты
            if book not in result:
                result.append(book)
            continue
    return result


def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book
    # return None


def remove_book_by_id(container, book_id):
    result = []
    for book in container:  # забегая вперёд - фильтрация
        if book['id'] != book_id:
            result.append(book)
    return result
