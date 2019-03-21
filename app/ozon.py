def create_book(title, author, price, tags):
    return {
        'title': title,
        'author': author,
        'price': price,
        'tags': tags,
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_book(container, title):
    title_lowercased = title.strip().lower()
    result = []
    for book in container:
        if title_lowercased in book['title'].lower():
            result.append(book)
            continue

        if title_lowercased in book['author'].lower():
            result.append(book)
            continue

        for tag in book['tags']:
            if title_lowercased in tag:
                result.append(book)
                continue
    return result
