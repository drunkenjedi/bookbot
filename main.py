import sys
from stats import words_in_book, unique_words_in_book, sort_char_dict

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words = words_in_book(book_text)
    unique_words = unique_words_in_book(book_text)
    sorted_chars = sort_char_dict(unique_words)

    print(f"Found {len(words)} total words")
    print("Character frequency count:")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")

main()
