import random


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


def generate_codes(num):
    letters = "ABCDEFGHIJK"
    digits = "012345"
    set_codes, codes = set(), []
    while len(codes) < num:
        code = (
            "".join(random.sample(letters, 4))
            + "-"
            + "".join(random.sample(digits, 4))
            + "-"
            + "".join(random.sample(letters, 4))
        )
        if code in set_codes:
            continue

        codes.append(code)
        set_codes.add(code)

    return codes


def hamming_distance(string1, string2):
    return sum([xi != yi for xi, yi in zip(string1, string2)])


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_prime(n):
    # find prime number greater than n
    while not is_prime(n):
        n += 1
    return n


class Hashtable:
    def __init__(self, size) -> None:
        self.size = find_prime(size)
        self.table = [None] * self.size
        self.dulicates_found = [[] for _ in range(self.size)]

    def hash_function(self, value):
        hash_value = 17
    
        for c in value:
            # Multiply the current hash value by a prime number
            hash_value = hash_value * 31
            
            # Add the ASCII code of the current character to the hash value
            hash_value += ord(c)
        
        # Return the hash value
        return hash_value % self.size
        

    def insert(self, value, code):
        key = self.hash_function(value)

        if self.table[key] is None:
            self.table[key] = value
            self.dulicates_found[key].append(code)
            return

        while self.table[key] != value:
            key = (key + 1) % self.size
            if self.table[key] is None:
                self.table[key] = value
                self.dulicates_found[key].append(code)
                return

        self.dulicates_found[key].append(code)

        return

    def search(self, value):
        key = self.hash_function(value)
        if self.table[key] == value:
            return True
        else:
            return False

    def find_duplicates_pairs(self):
        s = 0
        for duplicates in self.dulicates_found:
            for i, code1 in enumerate(duplicates):
                for code2 in duplicates[i + 1 :]:
                    print(code1, code2)
                    s += 1
        return s


def main():
    nof_codes = get_number()

    codes = generate_codes(nof_codes)
    print("Starting Calculating")

    import time

    t = time.time()

    hashtable = Hashtable(nof_codes * 12 * 2)
    for i, code in enumerate(codes):
        # code = get_word()
        for index, char in enumerate(code):
            if char == "-":
                continue
            hashtable.insert(code[:index] + "?" + code[index + 1 :], code)

        # if _code > nof_codes//4: # 3.4 sec for the large examples => 14 sec total
        #     raise EOFError()
        if i % 1000 == 0:
            print(i)

    print(hashtable.find_duplicates_pairs())
    print(time.time() - t)


if __name__ == "__main__":
    main()
