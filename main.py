# main.py
import sys
from stats import word_count, get_book_text, letter_count, sorted_characters

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_content = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    num_words = word_count(book_content)
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    letter_freq = letter_count(book_content)
    sorted_report = sorted_characters(letter_freq)

    for entry in sorted_report:
        print(f"{entry['char']}: {entry['num']}")
     
    print("============= END ===============")   

main()