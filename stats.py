def count_book_symbols(path_to_book):
    
    with open(path_to_book) as f:
        book_text = f.read()
    book_text = book_text.lower()

    book_stats = {}

    for symbol in book_text:
        if symbol not in book_stats:
            book_stats[symbol] = 1
        else:
            book_stats[symbol] += 1

    return book_stats

def count_book_words(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()

    return len(book_text.split())