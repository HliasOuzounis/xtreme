def parser():
    while 1:
        data = list(input().split(" "))
        for number in data:
            if len(number) > 0:
                yield (number)


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


def main():
    nof_codes = get_number()

    hashtable = dict()
    
    for _i in range(nof_codes):
        code = get_word()
        for index, char in enumerate(code):
            if char == "-":
                continue
            if (code[:index] + "?" + code[index + 1 :]) in hashtable:
                hashtable[code[:index] + "?" + code[index + 1 :]] += 1
            else:
                hashtable[code[:index] + "?" + code[index + 1 :]] = 1
        
    print(sum(value * (value - 1)//2 for _key, value in hashtable.items()))
        
if __name__ == "__main__":
    main()
