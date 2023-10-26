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
    
def find_suffix(string, p):
    suffix_coutner = 0
    string_idx = len(string) - 1
    for char in p[::-1]:
        while string_idx >= 0 and string[string_idx] != char:
            string_idx -= 1
        if string_idx == -1:
            break
        suffix_coutner += 1
        string_idx -= 1
    return suffix_coutner
    
    
def main():
    string = get_word()
    q = get_number()
    for _ in range(q):
        p = get_word()
        print(find_suffix(string, p))
        

if __name__ == '__main__':
    main()