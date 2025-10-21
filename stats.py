def get_num_words(text: str):
    return len(text.split())

def get_num_chars(text: str):
    num_chars_dict = {}
    for char in text.lower():
        num_chars_dict[char] = num_chars_dict.get(char, 0) + 1
    return num_chars_dict

def get_sorted_num_chars_list(num_chars_dict: dict):
    num_chars_dicts_list = []
    for key, value in num_chars_dict.items():
        num_chars_dicts_list.append({"char": key, "num": value})
    
    sorted_num_chars_dicts_list = sorted(num_chars_dicts_list, key=lambda item: item["num"], reverse=True)

    return sorted_num_chars_dicts_list