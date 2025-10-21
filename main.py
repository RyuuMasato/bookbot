import sys
from stats import get_num_words, get_num_chars, get_sorted_num_chars_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text():
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text()
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_num_chars_list = get_sorted_num_chars_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for num_char in sorted_num_chars_list:
        if str.isalpha(num_char["char"]):
            print(f"{num_char["char"]}: {num_char["num"]}")

    print("============= END ===============")

main()