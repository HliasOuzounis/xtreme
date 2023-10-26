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
    
    
def binary_search(array, value, cached_value):
    if len(array) == 0:
        return -1, -1
    if array[-1] <= value:
        return array[-1], len(array) - 1
    if array[0] > value:
        return -1, -1
    
    if len(array) == 1:
        return array[0], -1

    l = 0
    r = len(array) - 1 if cached_value == -1 else cached_value
    while l <= r:
        m = (l + r) // 2
        if array[m] <= value < array[m + 1]:
            return array[m], m
        if array[m] < value:
            l = m + 1
        else:
            r = m - 1            
    return -1, -1
    
    
def find_suffix(string, p, char_helper):
    char_cache = {char: -1 for char in "abcdefghijklmnopqrstuvwxyz"}
    suffix_coutner = 0
    string_idx = len(string) - 1
    for char in p[::-1]:
        if string_idx < 0:
            return suffix_coutner
            
        string_idx, cache_val = binary_search(char_helper[char], string_idx, char_cache[char])
        
        string_idx -= 1
        char_cache[char] = cache_val
                
        if string_idx >= -1:
            suffix_coutner += 1
    return suffix_coutner


def parse_string(string):
    chars_dict = {char: [] for char in "abcdefghijklmnopqrstuvwxyz"}
    for idx, char in enumerate(string):
        chars_dict[char].append(idx)
    return chars_dict

    
def main():
    string = get_word()
    q = get_number()
    chars_dict = parse_string(string)
    for _ in range(q):
        p = get_word()
        print(find_suffix(string, p, chars_dict))
        

if __name__ == '__main__':
    main()