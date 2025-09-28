def words_in_book(book_text):
    return book_text.split()

def unique_words_in_book(book_text):
    book_text = book_text.lower()

    char_counts = {}

    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    
def sort_on(dict_item):
    return dict_item["num"]

def sort_char_dict(char_counts):
    char_list = []

    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=sort_on, reverse=True)

    return char_list
