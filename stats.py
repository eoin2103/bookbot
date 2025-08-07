# Counts number of words in the book text and returns the count
def word_count(text):
    words = text.split()
    return len(words)

# reads a book text file and returns its content
def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        book_text = file.read()
    return book_text

def letter_count(text):
    freq = {}
    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def sorted_characters(freq_dict: dict) -> list:
    """
    Converts a frequency dictionary into a sorted list of dictionaries.
    Each dictionary contains a character and its count, but only if it's an alphabet character.
    The output list is sorted from most to least frequent.
    """
    sorted_list = []
    for char, count in freq_dict.items():
        if char.isalpha():  # Only include alphabet characters
            sorted_list.append({"char": char, "num": count})

    # Sort the list in descending order by count
    sorted_list.sort(key=lambda item: item["num"], reverse=True)

    return sorted_list
