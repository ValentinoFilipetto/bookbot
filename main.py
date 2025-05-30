from stats import count_characters_occurrences, count_words, get_text, sort_occurrences_dict

def main():
    frankestein_path = "books/frankenstein.txt"
    print_report(frankestein_path)

# prints a nice report about a text
def print_report(file_path):
    text = get_text(file_path)
    occurrences_as_array = sort_occurrences_dict(count_characters_occurrences(text))
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(text)} words found in the document")
    print("\n")
    for letter in occurrences_as_array:
        print(f"The '{letter["character"]}' was found {letter["num"]} times")
    print("--- End report ---")

main()
