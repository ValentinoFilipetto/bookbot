def main():
    frankestein_path = "books/frankestein.txt"
    print_report(frankestein_path)

# reads a text given a file path for that text
def get_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
# counts words in a given text  
def count_words(text):
    array_of_words = text.split()
    return len(array_of_words)


# returns a dictionary made of { character: number_of_occurrences }
def count_characters_occurrences(text_as_string):
    occurrences_dict = {}
    lowered_text = text_as_string.lower()
    array_of_characters = list(lowered_text)

    for character in array_of_characters:
        if character in occurrences_dict:
            occurrences_dict[character] += 1
        else:
            occurrences_dict.update({ character: 1})

    return occurrences_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries.
def sort_on(dict):
    return dict["num"]

# A function that sorts a dictionary of occurrences returning a sorted array.
def sort_occurrences_dict(dict):
    array_dict = []

    for key in dict:
        if key.isalpha():
            word_dict = { "character": key, "num": dict[key] }
            array_dict.append(word_dict)
    
    return sorted(array_dict, reverse=True, key=sort_on)

# prints a nice report about a text
def print_report(file_path):
    text = get_text(file_path)
    occurrences_as_array = sort_occurrences_dict(count_characters_occurrences(text))
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(text)} words were found in the document")
    print("\n")
    for letter in occurrences_as_array:
        print(f"The '{letter["character"]}' was found {letter["num"]} times")
    print("--- End report ---")

main()