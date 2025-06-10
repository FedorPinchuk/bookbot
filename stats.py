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

def dict_non_alpha_removed(dict_to_sort):
    
    sorted_dict = {}

    for key in dict_to_sort:
        if key.isalpha():
            sorted_dict[key] = dict_to_sort[key]
    
    return sorted_dict

def dict_to_dictlist(dict_to_modify):

    dictlist = []

    for key in dict_to_modify:
        modified_dict = {}
        modified_dict["char"] = key
        modified_dict["num"] = dict_to_modify[key]
        dictlist.append(modified_dict)

    return dictlist

def sort_on(dict):
    return dict["num"]