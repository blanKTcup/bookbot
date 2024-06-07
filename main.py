def main():
  book_path = "books/frankenstein.txt"
  book_text = get_text(book_path)
  word_count = get_num_words(book_text)
  char_count = get_num_chars(book_text)
  char_ordered_counts = convert_dict_to_sorted_list(char_count)
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print_char(char_count)
  print("--- End report ---")

def get_num_chars(book_text):
  lowercase_text = book_text.lower()
  char_count = {}
  for char in lowercase_text:
    if char.isalpha() == True:
      if char not in char_count:
        char_count[char] = 1
      else:
        char_count[char] += 1
  return char_count

def print_char(char_dict):
  for key, value in char_dict.items():
    print(f"The '{key}' character was found {value} times")

def sort_on(char_dict):
  char_value = next(iter(char_dict))
  return char_dict[char_value]

def convert_dict_to_sorted_list(char_dict):
  char_list = []
  for char in char_dict:
    char_item = {}
    char_item[char] = char_dict[char]
    char_list.append(char_item)
  char_list.sort(reverse=True, key=sort_on)
  print(char_list)

def get_num_words(book_text):
  word_count = len(book_text.split())
  return word_count

def get_text(path):
  with open(path) as f:
    return f.read()

main()