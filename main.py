from stats import *
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    non_alpha_removed_dict = dict_non_alpha_removed(count_book_symbols(sys.argv[1]))
    list_of_dict = dict_to_dictlist(non_alpha_removed_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_book_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for dict in list_of_dict:
        print(f"{dict["char"]}: {dict["num"]}")

main()