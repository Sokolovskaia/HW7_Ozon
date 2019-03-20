def create_book(title, author, price, tags):
    return {
        'title': title,
        'author': author,
        'price': price,
        'tags': tags,
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)  # чисто
    return copy


def search_book(container, title):  # посик по заголовку и автору
    title_lowercased = title.strip().lower()
    result = []
    if title[0] == "#":
        for book in container:
            for tag in book['tags']:
                if title[1:] in tag:
                    result.append(book)
                    continue
    else:
        for book in container:
            if title_lowercased in book['title'].lower():
                result.append(book)
                continue

            if title_lowercased in book['author'].lower():
                result.append(book)
                continue

    return result
