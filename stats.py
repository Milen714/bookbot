def get_book_text(path_to_file):
    
        with open(path_to_file) as f:
                return f.read()

def get_word_count(text):
        words = text.split()
        return len(words)

def get_char_count(text):
        char_dict = {}
        text = text.lower()
        for char in text:
                        if char in char_dict:
                                char_dict[char] += 1
                        else:
                                char_dict[char] = 1
        return char_dict

def sort_on(items):
        return items["num"]

def sort_char_dict(char_dict):
        char_list = []
        for char, count in char_dict.items():
                if char.isalpha():
                        char_list.append({"char": char, "num": count})
                
        return sorted(char_list, key=sort_on, reverse=True)
        

