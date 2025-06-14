def get_word_count(book_contents):
    words = book_contents.split()
    length_words = len(words)
    return length_words

def get_char_count(book_contents):
    char_count = {}
    for char in book_contents:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def sort_by_count(dictionary):
    return dictionary["num"]

def get_sorted_list(char_count):
    new_list = []
    for char, num in char_count.items():
        new_dict = {"char": char, "num": num}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_by_count)
    return new_list
    
    



