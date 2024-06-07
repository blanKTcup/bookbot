def main():
  book_path = "books/frankenstein.txt"
  book_text = get_text(book_path)
  word_count = get_num_words(book_text)
  print(f"There are {word_count} words in this book")

def get_num_words(book_text):
  word_count = len(book_text.split())
  return word_count

def get_text(path):
  with open(path) as f:
    return f.read()

main()