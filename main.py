from stats import count_words, get_occurances, get_report
import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    
    print(f"============ BOOKBOT ============\n")
    file_contents = get_book_text(path)
    print(f"Analyzing book found at {path}...\n")
    print(file_contents.split("\n")[0])
    count = count_words(file_contents)
    charDict = get_occurances(file_contents)
    get_report(charDict)
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




main()