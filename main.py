from stats import get_word_count, get_book_text, get_char_count, sort_char_dict
import sys
        
def main():
        arguments = sys.argv
        if len(arguments) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        book_location = arguments[1]
        text = get_book_text(book_location)
        print("============ BOOKBOT ============")
        
        print(f"Analysing book found at {book_location}...")
        
        print("----------- Word Count ----------")

        print(f"Found {get_word_count(text)} total words")
        print("--------- Character Count -------")
        #print(get_char_count(text))
        sorted_chars = sort_char_dict(get_char_count(text))
        for item in sorted_chars:
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")

main()