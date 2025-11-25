def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def num_words(file_contents):
    split_words = file_contents.split()
    num = len(split_words)
    return num 

def num_char(file_contents):
    split_chars = {}
    words = file_contents
    for char in words:
        low_char = char.lower()
        if low_char not in split_chars:
            split_chars[low_char] = 0
        split_chars[low_char] += 1
    return split_chars

def helper(items):
    return items["num"]

def sort_dict(items):
    items.sort(reverse=True, key=helper)
    return items

def chars_list_to_sorted_dict(split_chars):
    result = []
    for ch, count in split_chars.items():
        new_dict = {"char": ch, "num": count}
        result.append(new_dict)
    sorted_result = sort_dict(result)
    return sorted_result

