def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_book_word_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_book_word_count(text):
    return len(text.split())
main()
