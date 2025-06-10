from stats import *

def main():
    non_alpha_removed_dict = dict_non_alpha_removed(count_book_symbols("books/frankenstein.txt"))
    list_of_dict = dict_to_dictlist(non_alpha_removed_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_book_words("books/frankenstein.txt")} total words")
    print("--------- Character Count -------")
    for dict in list_of_dict:
        print(f"{dict["char"]}: {dict["num"]}")

main()