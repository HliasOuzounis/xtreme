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
        self.duplicates_found = [0] * self.size

    def hash_function(self, value):
        return hash(value) % self.size
        # random.seed(value)
        # return random.randint(0, self.size - 1)

    def insert(self, value, code):
        key = self.hash_function(value)

        if self.table[key] is None:
            self.table[key] = value
            self.duplicates_found[key] = 1
            return

        while self.table[key] != value:
            key = (key + 1) % self.size
            if self.table[key] is None:
                self.table[key] = value
                self.duplicates_found[key] += 1
                return

        self.duplicates_found[key] += 1

        return

    def search(self, value):
        key = self.hash_function(value)
        if self.table[key] == value:
            return True
        else:
            return False

    def find_duplicates_pairs(self):
        return sum(v * (v - 1)//2 for v in self.duplicates_found)


def main():
    nof_codes = get_number()


    hashtable = Hashtable(nof_codes * 12 * 2)
    
    for i in range(nof_codes):
        code = get_word()
        for index, char in enumerate(code):
            if char == "-":
                continue
            hashtable.insert(code[:index] + "?" + code[index + 1 :], code)

    print(hashtable.find_duplicates_pairs())


if __name__ == "__main__":
    main()
