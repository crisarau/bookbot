def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_book_word_count(text))
    print(get_letter_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_book_word_count(text):
    return len(text.split())
def get_letter_count(text):
    answer = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in answer:
            answer[lower_char] += 1
        else:
            answer[lower_char] = 1
    return answer
main()
