import sys 
from stats import num_words
from stats import get_book_text
from stats import num_char      
from stats import chars_list_to_sorted_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    txt = get_book_text(book_path)
    num = num_words(txt)
    chars = num_char(txt)
    sorted_chars = chars_list_to_sorted_dict(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {num}")
    print("============= END ===============")
    
main()

        
