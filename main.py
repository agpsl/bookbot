def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = count_words(text)
    chars = char_occurrence(text)
    sorted_chars = sorted(chars, key=chars.get, reverse=True)
    print(sorted_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for c in sorted_chars:
        if c.isalpha() == True:
            print(f"The {c} character was found {chars[c]} times")
    print(f"--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def char_occurrence(text):
    char_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in char_dict:
            char_dict[char_lower] = 1
        else:
            char_dict[char_lower] += 1
    return char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()