# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
    
    
def find_suffix(string, p, char_helper):
    suffix_coutner = 0
    string_idx = len(string) - 1
    for char in p[::-1]:
        char_id = get_char_id(char)
        if string_idx < 0:
            return suffix_coutner
        if char_helper[char_id][string_idx] == -1:
            return suffix_coutner
        string_idx = char_helper[char_id][string_idx] - 1
        suffix_coutner += 1
    return suffix_coutner


def get_char_id(char):
    return ord(char) - ord('a')

def parse_string(string):
    prev_characters = [[-1 for _ in string] for _ in range(26)]
    for idx, char in enumerate(string):
        for char_id in range(26):
            prev_characters[char_id][idx] = prev_characters[char_id][idx - 1]
        char_id = get_char_id(char)
        prev_characters[char_id][idx] = idx
    return prev_characters
    
    
def main():
    string = get_word()
    q = get_number()
    char_helper = parse_string(string)
    
    for _ in range(q):
        p = get_word()
        print(find_suffix(string, p, char_helper))
        

if __name__ == '__main__':
    main()