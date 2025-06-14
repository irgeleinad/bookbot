import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

def get_book_text(file_path_to_read):
    with open(file_path_to_read) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    word_count = get_word_count(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = get_char_count(book_contents)
    sorted_list = get_sorted_list(character_count)
    for char_dict in sorted_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()






