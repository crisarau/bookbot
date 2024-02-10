def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_word_count(text)
    char_count_dict = get_char_count_dict(text)
    letter_count_dict = get_letter_count_list(char_count_dict)
    print_report(book_path, word_count,letter_count_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_book_word_count(text):
    return len(text.split())
def get_char_count_dict(text):
    answer = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in answer:
            answer[lower_char] += 1
        else:
            answer[lower_char] = 1
    return answer
def sort_on(dict):
    return dict["num"]
def get_letter_count_list(char_count_dict):
    answer = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            answer.append(
                {"letter": char, "num": count}
            )
    answer.sort(reverse=True, key=sort_on)
    return answer
def print_report(path, word_count, alpha_letter_count):
    print(f"--- Being report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for letter in alpha_letter_count:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
    print("--- End report ---")
main()
