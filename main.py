def main():
  book_path = "books/frankenstein.txt"
  book_text = get_text(book_path)
  word_count = get_num_words(book_text)
  letter_count_dict_unordered = get_num_chars(book_text)
  letter_counts_ordered = convert_dict_to_sorted_list(letter_count_dict_unordered)
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print(" ")
  print_char(letter_counts_ordered)
  print("--- End report ---")

def get_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(book_text):
  word_count = len(book_text.split())
  return word_count

def get_num_chars(book_text):
  lowercase_text = book_text.lower() # make book text all lowercase
  letter_count_dict_unordered = {}
  for char in lowercase_text:
    if char.isalpha() == True: # exclude all characters that are not letters
      if char not in letter_count_dict_unordered:
        letter_count_dict_unordered[char] = 1
      else:
        letter_count_dict_unordered[char] += 1
  return letter_count_dict_unordered

def sort_on(letter_count_dict_unordered):
  letter_dict_key = next(iter(letter_count_dict_unordered))
  letter_dict_value = letter_count_dict_unordered[letter_dict_key]
  return letter_dict_value

def convert_dict_to_sorted_list(letter_count_dict_unordered):
  letter_count_list_ordered = []
  for letter in letter_count_dict_unordered: 
    letter_item = {} # separate each key, value into its own dictionary
    letter_item[letter] = letter_count_dict_unordered[letter]
    letter_count_list_ordered.append(letter_item) # append each separate dictionary to a new list of key,value dictionaries
  letter_count_list_ordered.sort(reverse=True, key=sort_on)
  return letter_count_list_ordered

def print_char(letter_counts_ordered):
  for dict in letter_counts_ordered:
    dict_key = next(iter(dict))
    dict_value = dict[dict_key]
    print(f"The '{dict_key}' character was found {dict_value} times")

main()