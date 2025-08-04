def count_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)

    return word_count

def count_characters(book_text):
    book_lower_case = book_text.lower()
    all_characters = {}

    for char in book_lower_case:
            if char == " ":
                 continue
            elif char in all_characters:
                 all_characters[char] += 1
            else:
                 all_characters[char] = 1 
    
    all_characters_list = []
    for char in all_characters:
        count = all_characters[char]
        entry = {
             "char": char,
             "num": count
        }

        all_characters_list.append(entry)

    return all_characters_list

def sort_on(items):
     return items["num"]


          