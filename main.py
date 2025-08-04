from stats import count_words, count_characters, sort_on
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    num_characters.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range (0, len(num_characters) - 1):
        entry = num_characters[i]
        if entry["char"].isalpha:
            char = entry["char"]
            count = entry["num"]
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
main()

